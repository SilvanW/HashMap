from hashmap import HashMap, HashMapChaining
from probing import ProbingImplementation

hashmap = HashMap(size=5, probing_implementation=ProbingImplementation.DOUBLE_HASHING)

hashmap.insert("key", "value")
hashmap.insert("yek", "value 1")
hashmap.insert("yke", "value 2")

print(hashmap.map)

print(hashmap.loading_factor)

result = hashmap.retrieve("yek")

print(result)

chaining_hashmap = HashMapChaining(size=5)

chaining_hashmap.insert("key", "value")
chaining_hashmap.insert("yek", "value 1")
chaining_hashmap.insert("yke", "value 2")

print(chaining_hashmap.map)

print(chaining_hashmap.loading_factor)

result = chaining_hashmap.retrieve("yek")

print(result)
