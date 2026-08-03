"""
ZAD02

Napisz generator zwracający kolejne znaki napisu przekazanego jako argument.
"""


def get_chars(text):
    for ch in text:
        yield ch


for ch in get_chars("sd dfg dfg frgth"):
    print(ch)
