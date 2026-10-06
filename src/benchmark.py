import random
from math import floor
from typing import TypedDict

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from tqdm import tqdm

from hashing import HashingImplementation
from hashmap import HashMap, HashMapChaining
from probing import ProbingImplementation

HASHMAP_SIZE = 10007
HASHING_IMPLEMENTATION = HashingImplementation.ORD

with open("data/100000-words.txt", "r") as fh:
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
        hashmap = HashMap(
            size=HASHMAP_SIZE,
            probing_implementation=implementation,
            hashing_implementation=HASHING_IMPLEMENTATION,
        )

        inserted_words = []

        for i, word in tqdm(
            enumerate(corpus),
            desc=f"Inserting words for {implementation.value}",
            total=floor(HASHMAP_SIZE * (target_loading_factor / 10)),
        ):
            try:
                hashmap.insert(word, word)
            except IndexError as e:
                break

            inserted_words.append(word)

            if (
                hashmap.loading_factor >= target_loading_factor / 10
                or hashmap.remaining_space == 0
            ):
                break

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

for target_loading_factor in range(1, 11, 1):
    hashmap = HashMapChaining(
        size=HASHMAP_SIZE,
        hashing_implementation=HASHING_IMPLEMENTATION,
    )

    inserted_words = []

    for i, word in tqdm(
        enumerate(corpus),
        desc="Inserting words for chaining",
        total=floor(HASHMAP_SIZE * (target_loading_factor / 10)),
    ):
        try:
            hashmap.insert(word, word)
        except IndexError as e:
            break

        inserted_words.append(word)

        if (
            hashmap.loading_factor >= target_loading_factor / 10
            or hashmap.remaining_space == 0
        ):
            break

    num_comparisons: list[int] = [hashmap.retrieve(word)[1] for word in inserted_words]

    dataset.append(
        Scores(
            loading_factor=target_loading_factor / 10,
            num_comparisons=num_comparisons,
            probing="chaining",
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

fig, (ax_box, ax_line) = plt.subplots(1, 2, figsize=(16, 6))

sns.boxplot(
    data=df,
    x="loading_factor",
    y="num_comparisons",
    hue="probing",
    log_scale=True,
    ax=ax_box,
)
ax_box.set_title("Distribution per loading factor")

sns.lineplot(
    data=df,
    x="loading_factor",
    y="num_comparisons",
    hue="probing",
    estimator="mean",
    marker="o",
    ax=ax_line,
)
# ax_line.set_yscale("log")
ax_line.set_xticks(np.arange(0, 1.01, 0.1))
ax_line.set_title("Mean per loading factor")

fig.suptitle("HashMap comparisons per loading factor")
plt.tight_layout()
plt.show()
