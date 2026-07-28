"""
ZAD03

Fibonacci do limitu
Napisz generator fib_limit_send(n), który:
• otrzymuje wartość logiczną przez send():
    – True = zwróć kolejny element ciągu Fibonacciego,
    – False = zakończ działanie generatora,
• generuje liczby Fibonacciego aż do limitu n.
"""


def fib_limit_send(n):
    a, b = 0, 1
    state = yield

    while state and n > 0:
        state = yield a
        a, b = b, a + b
        n -= 1

    yield "Koniec"


gen = fib_limit_send(10)
next(gen)
print(gen.send(True))
print(gen.send(True))
print(gen.send(True))
print(gen.send(True))
print(gen.send(True))
print(gen.send(True))
print(gen.send(True))
print(gen.send(False))
