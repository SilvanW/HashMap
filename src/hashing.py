from enum import Enum
from typing import Protocol

from exceptions import HashingNotImplementedError


class Hashing(Protocol):
    def __call__(self, key: str) -> int: ...


def ord_hashing(key: str) -> int:
    return sum([ord(char) for char in key])


def ord_hashing_position(key: str) -> int:
    return sum(ord(char) * i for i, char in enumerate(key))


def polynomial_hashing(key: str, base: int = 31) -> int:
    h = 0
    for char in key:
        h = (h * base + ord(char)) & 0xFFFFFFFF
    return h


def fnv1a_hashing(key: str) -> int:
    h = 0x811C9DC5  # FNV offset basis (32-bit)
    for char in key:
        h ^= ord(char)
        h = (h * 0x01000193) & 0xFFFFFFFF  # FNV prime (32-bit)
    return h


class HashingImplementation(Enum):
    ORD = "ord"
    ORD_POSITION = "ord_position"
    POLYNOMIAL = "polynomial"
    FNV1A = "fnv1a"


HASHING_LOOKUP: dict[HashingImplementation, Hashing] = {
    HashingImplementation.ORD: ord_hashing,
    HashingImplementation.ORD_POSITION: ord_hashing_position,
    HashingImplementation.POLYNOMIAL: polynomial_hashing,
    HashingImplementation.FNV1A: fnv1a_hashing,
}


def get_hashing_function(hashing_implementation: HashingImplementation) -> Hashing:
    result = HASHING_LOOKUP.get(hashing_implementation)

    if result is None:
        raise HashingNotImplementedError(
            f"Hashing function {hashing_implementation} not implemented"
        )

    return result
