from src.hashmap import HashMap

hashmap = HashMap(size=5)

hashmap.insert("key", "value")

print(hashmap.map)

result = hashmap.retrieve("key")

print(result)
