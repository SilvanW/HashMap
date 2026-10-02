import sympy


def hashing(key: str) -> int:
    return 1


class HashMap:
    def __init__(self, size: int) -> None:

        if not sympy.isprime(size):
            raise ValueError(f"HashMap size {size} is invalid as it must be Prime.")

        self.size = size
        self.map: list[str] = [""] * size

    def insert(self, key: str, value: str) -> None:
        hash = hashing(key)

        index = hash % self.size

        self.map[index] = value

    def retrieve(self, key: str) -> str:
        hash = hashing(key)

        index = hash % self.size

        return self.map[index]
