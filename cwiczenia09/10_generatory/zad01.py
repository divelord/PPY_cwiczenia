"""
ZAD01

Napisz generator, który zwraca kolejne liczby parzyste mniejsze od podanej wartości.
"""


def get_even_numbers(n):
    for i in range(0, n):
        if i % 2 == 0:
            yield i


for num in get_even_numbers(10):
    print(num)
