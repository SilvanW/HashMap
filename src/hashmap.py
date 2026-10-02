import sympy

from src.custom_types import Map
from src.hashing import ord_hashing
from src.probing import linear_probing


class HashMap:
    def __init__(self, size: int) -> None:

        if not sympy.isprime(size):
            raise ValueError(f"HashMap size {size} is invalid as it must be Prime.")

        self.size = size
        self.map: Map = [""] * size

    def insert(self, key: str, value: str) -> None:
        hash = ord_hashing(key)

        index = hash % self.size

        if self.map[index] != "" and self.map[index] != value:
            index = linear_probing(self.map, index)

        self.map[index] = value

    def retrieve(self, key: str) -> str:
        hash = ord_hashing(key)

        index = hash % self.size

        return self.map[index]

    @property
    def loading_factor(self) -> float:
        used = self.map.count("")

        return (self.size - used) / self.size
