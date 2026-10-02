from src.hashmap import HashMap

hashmap = HashMap(size=5)

hashmap.insert("key", "value")
hashmap.insert("value", "key")
hashmap.insert("basic", "test")
hashmap.insert("yek", "value 1")


print(hashmap.map)

result = hashmap.retrieve("key")

print(result)

print(hashmap.loading_factor)
