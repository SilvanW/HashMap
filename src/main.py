from hashmap import HashMap

with open("data/corpus_1000.txt", "r") as fh:
    corpus = fh.readlines()

corpus: list[str] = [word for line in corpus for word in line.split(" ")]

print(len(corpus))

hashmap = HashMap(size=1069)

for word in corpus:
    hashmap.insert(word, word)

print(hashmap.loading_factor)
