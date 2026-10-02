import pytest

from hashmap import HashMap


@pytest.fixture
def hashmap() -> HashMap:
    return HashMap(size=5)


def test_invalid_size():
    with pytest.raises(ValueError):
        HashMap(size=4)


def test_simple_usecase(hashmap: HashMap):
    hashmap.insert("key", "value")

    result = hashmap.retrieve("key")

    assert result == "value"


def test_simple_usecase_invalid_key(hashmap: HashMap):
    hashmap.insert("key", "value")

    with pytest.raises(IndexError):
        hashmap.retrieve("invalid_key")


def test_probing(hashmap: HashMap):
    hashmap.insert("key", "value")
    hashmap.insert("yek", "value 1")

    key_result = hashmap.retrieve("key")
    yek_result = hashmap.retrieve("yek")

    assert key_result == "value"
    assert yek_result == "value 1"
