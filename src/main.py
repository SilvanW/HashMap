from hashmap import HashMap
from probing import ProbingImplementation

hashmap = HashMap(size=5, probing_implementation=ProbingImplementation.DOUBLE_HASHING)

hashmap.insert("key", "value")
hashmap.insert("yek", "value 1")
hashmap.insert("yke", "value 2")

print(hashmap.map)

print(hashmap.loading_factor)

result = hashmap.retrieve("yek")

print(result)
