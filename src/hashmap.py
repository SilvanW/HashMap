import sympy

from custom_types import Map
from exceptions import HashMapFullError, HashMapSizeError
from hashing import HashingImplementation, get_hashing_function
from probing import (
    ProbingImplementation,
    get_probing_function,
    get_probing_search_function,
)


class HashMap:
    def __init__(
        self,
        size: int,
        probing_implementation: ProbingImplementation = ProbingImplementation.LINEAR,
        hashing_implementation: HashingImplementation = HashingImplementation.ORD,
    ) -> None:

        if not sympy.isprime(size):
            raise HashMapSizeError(
                f"HashMap size {size} is invalid as it must be Prime."
            )

        self.size = size
        self.map: Map = [None] * size

        self.probing_function = get_probing_function(
            probing_implementation=probing_implementation
        )
        self.probing_search_function = get_probing_search_function(
            probing_implementation=probing_implementation
        )

        self.hashing_function = get_hashing_function(
            hashing_implementation=hashing_implementation
        )

    @property
    def loading_factor(self) -> float:
        used = self.map.count(None)
        return (self.size - used) / self.size

    @property
    def remaining_space(self) -> int:
        return self.map.count(None)

    def insert(self, key: str, value: str) -> None:

        if self.loading_factor == 1:
            raise HashMapFullError(f"Hashmap of size {self.size} is full")

        hash = self.hashing_function(key)

        index = hash % self.size

        if self.map[index] is not None and self.map[index][1] != value:
            try:
                index = self.probing_function(self.map, index, key)
            except IndexError as e:
                print(self.remaining_space, self.loading_factor)
                raise IndexError from e

        self.map[index] = (key, value)

    def retrieve(self, key: str) -> tuple[str, int]:

        hash = self.hashing_function(key)

        index = hash % self.size

        if self.map[index] is None:
            raise IndexError(f"Hashmap does not contain key {key}")

        if self.map[index][0] == key:
            return self.map[index][1], 1

        result = self.probing_search_function(self.map, index, key)

        return result[0][1], result[1] + 1
