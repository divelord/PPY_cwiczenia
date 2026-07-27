"""
ZAD11

Napisz generator tworzący losowe zdania typu Subject Verb Object używając list dostępnych słów.
Przykładowo:
subjects = ["We", "You", "I"]
verbs = ["like", "see", "know"]
objects = ["Python", "NAI", "Processor"]
"""

import random


def sentence_generator():
    subjects = ["We", "You", "I"]
    verbs = ["like", "see", "know"]
    objects = ["Python", "NAI", "Processor"]

    while True:
        s = random.choice(subjects)
        v = random.choice(verbs)
        o = random.choice(objects)

        yield f"{s} {v} {o}"


for i, sentence in zip(range(5), sentence_generator()):
    print(sentence)
