from typing import Protocol


class Hashing(Protocol):
    def __call__(self, key: str) -> int: ...


def ord_hashing(key: str) -> int:
    return sum([ord(char) for char in key])


def ord_hashing_position(key: str) -> int:
    return sum(ord(char) * i for i, char in enumerate(key))
