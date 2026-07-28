"""
ZAD02

Napisz generator pairs_send(), który:
• otrzymuje elementy jeden po drugim przez send() w nieskończoność.
• zwraca kolejne liczby w krotkach parami (current, previous).
"""


def pairs_send():
    previous = None
    current = yield

    while True:
        new = yield previous, current
        previous = current
        current = new


gen = pairs_send()
next(gen)
print(gen.send("abc"))
print(gen.send("cba"))
print(gen.send("wow"))
print(gen.send("that"))
print(gen.send("works"))
