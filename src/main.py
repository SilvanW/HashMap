import random

import matplotlib.pyplot as plt
import seaborn as sns

from hashmap import HashMap

TARGET_LOADING_FACTOR = 1

with open("data/corpus_1000.txt", "r") as fh:
    corpus = fh.readlines()

corpus: list[str] = [word for line in corpus for word in line.split(" ")]

random.shuffle(corpus)

corpus = list(set(corpus))

print(len(corpus))

hashmap = HashMap(size=373)


for i, word in enumerate(corpus):
    hashmap.insert(word, word)

    if hashmap.loading_factor >= TARGET_LOADING_FACTOR:
        break

inserted_words = corpus[: i + 1]

print(hashmap.loading_factor)

num_comparisons: list[int] = [hashmap.retrieve(word)[1] for word in inserted_words]

print(num_comparisons)

sns.violinplot(
    x=[hashmap.loading_factor] * len(num_comparisons), y=num_comparisons, cut=0
)
plt.show()
