from enum import Enum
from typing import Protocol

from custom_types import Item, Map
from exceptions import ProbingNotImplementedError, ProbingSearchNotImplementedError


class Probing(Protocol):
    def __call__(self, map: Map, index: int) -> int: ...


class ProbingSearch(Protocol):
    def __call__(self, map: Map, index: int, key: str) -> tuple[Item, int]: ...


def linear_probing(map: Map, index: int) -> int:
    map_size: int = len(map)
    for i in range(index + 1, index + 1 + map_size):
        new_index = i % map_size
        if map[new_index] is None:
            return new_index

    raise IndexError("Hashmap does not have any free indexes ")


def quadratic_probing(map: Map, index: int) -> int:
    map_size: int = len(map)
    for k in range(1, map_size + 1):
        new_index = (index + k**2) % map_size
        if map[new_index] is None:
            return new_index

    raise IndexError("Hashmap does not have any free indexes")


def linear_probing_search(map: Map, index: int, key: str) -> tuple[Item, int]:
    map_size: int = len(map)
    for counter, i in enumerate(range(index + 1, index + 1 + map_size)):
        new_index = i % map_size

        if map[new_index] is None:
            break

        if map[new_index][0] == key:
            return map[new_index], counter + 1

    raise IndexError(f"Hashmap does not contain key {key}")


def quadratic_probing_search(map: Map, index: int, key: str) -> tuple[Item, int]:
    map_size: int = len(map)
    for k in range(1, map_size + 1):
        new_index = (index + k**2) % map_size

        if map[new_index] is None:
            break

        if map[new_index][0] == key:
            return map[new_index], k

    raise IndexError(f"Hashmap does not contain key {key}")


class ProbingImplementation(Enum):
    LINEAR = "linear"
    QUADRATIC = "quadratic"


PROBING_LOOKUP: dict[ProbingImplementation, Probing] = {
    ProbingImplementation.LINEAR: linear_probing,
    ProbingImplementation.QUADRATIC: quadratic_probing,
}

PROBING_SEARCH_LOOKUP: dict[ProbingImplementation, ProbingSearch] = {
    ProbingImplementation.LINEAR: linear_probing_search,
    ProbingImplementation.QUADRATIC: quadratic_probing_search,
}


def get_probing_function(probing_implementation: ProbingImplementation) -> Probing:
    result = PROBING_LOOKUP.get(probing_implementation)

    if result is None:
        raise ProbingNotImplementedError(
            f"Probing function {probing_implementation} not implemented"
        )

    return result


def get_probing_search_function(
    probing_implementation: ProbingImplementation,
) -> ProbingSearch:
    result = PROBING_SEARCH_LOOKUP.get(probing_implementation)

    if result is None:
        raise ProbingSearchNotImplementedError(
            f"Probing search function {probing_implementation} not implemented"
        )

    return result
