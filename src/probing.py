from typing import Protocol

from custom_types import Item, Map


class Probing(Protocol):
    def __call__(self, map: Map, index: int) -> int: ...


def linear_probing(map: Map, index: int) -> int:
    map_size: int = len(map)
    for i in range(index + 1, index + 1 + map_size):
        new_index = i % map_size
        if map[new_index] is None:
            return new_index

    raise IndexError("Hashmap does not have any free indexes ")


def linear_probing_search(map: Map, index: int, key: str) -> tuple[Item, int]:
    map_size: int = len(map)
    for counter, i in enumerate(range(index + 1, index + 1 + map_size)):
        new_index = i % map_size
        if map[new_index][0] == key:
            return map[new_index], counter + 1

    raise IndexError(f"Hashmap does not contain key {key}")
