"""
ZAD01

Generowanie wszystkich prefiksów:
Napisz funkcję generatora prefixes_send(), która:
• otrzymuje napis za pomocą metody send(),
• zwraca (yield) wszystkie prefiksy tego napisu.
"""


def prefixes_send():
    received = yield

    while True:
        prefix = ""
        result = ""

        for i in received:
            prefix += i
            result += prefix + "\n"

        received = yield result


gen = prefixes_send()
next(gen)
print(gen.send("abcdef"))
