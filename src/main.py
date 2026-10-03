from hashmap import HashMap
from probing import ProbingImplementation

hashmap = HashMap(size=5, probing_implementation=ProbingImplementation.QUADRATIC)

hashmap.insert("key", "value")
hashmap.insert("yek", "value 1")
hashmap.insert("yke", "value 1")

print(hashmap.map)

print(hashmap.loading_factor)
