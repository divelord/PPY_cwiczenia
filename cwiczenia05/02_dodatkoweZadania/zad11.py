"""
ZAD11

Napisz nieskończony generator zwracający naprzemienne wartości:
1,-1, 1,-1, 1,-1, ...
"""


def alter_sequence():
    result = 1

    while True:
        yield result
        result *= -1


for i, res in zip(range(10), alter_sequence()):
    print(res)
