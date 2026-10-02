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

    assert result[0] == "value"


def test_simple_usecase_invalid_key(hashmap: HashMap):
    hashmap.insert("key", "value")

    with pytest.raises(IndexError):
        hashmap.retrieve("invalid_key")


def test_probing(hashmap: HashMap):
    hashmap.insert("key", "value")
    hashmap.insert("yek", "value 1")

    key_result = hashmap.retrieve("key")
    yek_result = hashmap.retrieve("yek")

    assert key_result[0] == "value"
    assert yek_result[0] == "value 1"


def test_comparison_counter(hashmap: HashMap):
    hashmap.insert("key", "value")
    hashmap.insert("yek", "value 1")

    key_result = hashmap.retrieve("key")
    yek_result = hashmap.retrieve("yek")

    assert key_result[1] == 1
    assert yek_result[1] == 2
