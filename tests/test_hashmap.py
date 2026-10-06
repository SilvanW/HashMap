import pytest

from exceptions import HashMapFullError, HashMapSizeError
from hashmap import HashMap, HashMapChaining


@pytest.fixture
def hashmap() -> HashMap:
    return HashMap(size=5)


@pytest.fixture
def hashmap_chaining() -> HashMapChaining:
    return HashMapChaining(size=5)


def test_invalid_size():
    with pytest.raises(HashMapSizeError):
        HashMap(size=4)


def test_invalid_size_chaining():
    with pytest.raises(HashMapSizeError):
        HashMapChaining(size=4)


def test_simple_usecase(hashmap: HashMap):
    hashmap.insert("key", "value")

    result = hashmap.retrieve("key")

    assert result[0] == "value"


def test_simple_usecase_chaining(hashmap_chaining: HashMapChaining):
    hashmap_chaining.insert("key", "value")

    result = hashmap_chaining.retrieve("key")

    assert result[0] == "value"


def test_simple_usecase_invalid_key(hashmap: HashMap):
    hashmap.insert("key", "value")

    with pytest.raises(IndexError):
        hashmap.retrieve("invalid_key")


def test_simple_usecase_invalid_key_chaining(hashmap_chaining: HashMapChaining):
    hashmap_chaining.insert("key", "value")

    with pytest.raises(IndexError):
        hashmap_chaining.retrieve("invalid_key")


def test_probing(hashmap: HashMap):
    hashmap.insert("key", "value")
    hashmap.insert("yek", "value 1")

    key_result = hashmap.retrieve("key")
    yek_result = hashmap.retrieve("yek")

    assert key_result[0] == "value"
    assert yek_result[0] == "value 1"


def test_chaining(hashmap_chaining: HashMapChaining):
    hashmap_chaining.insert("key", "value")
    hashmap_chaining.insert("yek", "value 1")

    key_result = hashmap_chaining.retrieve("key")
    yek_result = hashmap_chaining.retrieve("yek")

    assert key_result[0] == "value"
    assert yek_result[0] == "value 1"


def test_comparison_counter(hashmap: HashMap):
    hashmap.insert("key", "value")
    hashmap.insert("yek", "value 1")

    key_result = hashmap.retrieve("key")
    yek_result = hashmap.retrieve("yek")

    assert key_result[1] == 1
    assert yek_result[1] == 2


def test_comparison_counter_chaining(hashmap_chaining: HashMapChaining):
    hashmap_chaining.insert("key", "value")
    hashmap_chaining.insert("yek", "value 1")

    key_result = hashmap_chaining.retrieve("key")
    yek_result = hashmap_chaining.retrieve("yek")

    assert key_result[1] == 1
    assert yek_result[1] == 2


def test_full_hashmap(hashmap: HashMap):
    for i in range(5):
        hashmap.insert(f"key{i}", "value")

    with pytest.raises(HashMapFullError):
        hashmap.insert("test", "value")


def test_full_hashmap_chaining(hashmap_chaining: HashMapChaining):
    for i in range(5):
        hashmap_chaining.insert(f"key{i}", "value")

    with pytest.raises(HashMapFullError):
        hashmap_chaining.insert("test", "value")
