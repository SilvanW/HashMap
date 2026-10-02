import sympy

from custom_types import Map
from hashing import ord_hashing
from probing import linear_probing, linear_probing_search


class HashMap:
    def __init__(self, size: int) -> None:

        if not sympy.isprime(size):
            raise ValueError(f"HashMap size {size} is invalid as it must be Prime.")

        self.size = size
        self.map: Map = [None] * size

    def insert(self, key: str, value: str) -> None:
        hash = ord_hashing(key)

        index = hash % self.size

        if self.map[index] is not None and self.map[index][1] != value:
            index = linear_probing(self.map, index)

        self.map[index] = (key, value)

    def retrieve(self, key: str) -> str:
        hash = ord_hashing(key)

        index = hash % self.size

        if self.map[index] is None:
            raise IndexError(f"Hashmap does not contain key {key}")

        if self.map[index][0] == key:
            return self.map[index][1]

        # TODO: must also search other indexes using probing strategy (write tests first)

        return linear_probing_search(self.map, index, key)[1]

    @property
    def loading_factor(self) -> float:
        used = self.map.count(None)

        return (self.size - used) / self.size
