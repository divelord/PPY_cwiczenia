"""
ZAD10

Napisz generator liczb pierwszych:
• od 1 do N
• od 1 do ∞
"""


def is_prime(n):
    if n < 2:
        return False
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True


def prime_to_n(n):
    num = 2
    while num <= n:
        if is_prime(num):
            yield num
        num += 1


def prime_to_inf():
    num = 2
    while True:
        if is_prime(num):
            yield num
        num += 1


for i in prime_to_n(10):
    print(i)
print()
for i, prime in zip(range(10), prime_to_inf()):
    print(prime)
