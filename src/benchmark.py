import random
from typing import TypedDict

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from mpmath import e1

from hashmap import HashMap
from probing import ProbingImplementation

with open("data/corpus_1000.txt", "r") as fh:
    corpus = fh.readlines()

corpus: list[str] = [word for line in corpus for word in line.split(" ")]

random.shuffle(corpus)

corpus = list(set(corpus))


class Scores(TypedDict):
    loading_factor: float
    num_comparisons: list[int]
    probing: str


dataset: list[Scores] = []

for implementation in ProbingImplementation:
    for target_loading_factor in range(1, 11, 1):
        hashmap = HashMap(size=373, probing_implementation=implementation)

        for i, word in enumerate(corpus):
            hashmap.insert(word, word)

            if (
                hashmap.loading_factor >= target_loading_factor / 10
                or hashmap.remaining_space == 0
            ):
                break

        inserted_words = corpus[: i + 1]

        num_comparisons: list[int] = [
            hashmap.retrieve(word)[1] for word in inserted_words
        ]

        dataset.append(
            Scores(
                loading_factor=target_loading_factor / 10,
                num_comparisons=num_comparisons,
                probing=implementation.value,
            )
        )

df = pd.DataFrame(
    {
        "loading_factor": score["loading_factor"],
        "num_comparisons": n,
        "probing": score["probing"],
    }
    for score in dataset
    for n in score["num_comparisons"]
)

sns.boxplot(data=df, x="loading_factor", y="num_comparisons", hue="probing")
plt.title("HashMap comparisons per loading factor")
plt.show()
