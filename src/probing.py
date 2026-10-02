from typing import Protocol

from src.custom_types import Map


class Probing(Protocol):
    def __call__(self, map: Map, index: int) -> int: ...


def linear_probing(map: Map, index: int) -> int:
    map_size: int = len(map)
    for i in range(index + 1, index + 1 + map_size):
        new_index = i % map_size
        if map[new_index] == "":
            return new_index

    raise IndexError("Hashmap does not have any free indexes ")
