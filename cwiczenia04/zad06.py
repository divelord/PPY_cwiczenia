"""
ZAD06

Policz w liście:
lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
• Liczby podzielne przez 7
• Liczby pierwsze
"""


def numbers(main_list):
    for sub_list in main_list:
        for item in sub_list:
            yield item


def is_prime(n):
    if n < 2:
        return False
    for num in range(2, int(n ** 0.5) + 1):
        if n % num == 0:
            return False
    return True


lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
divisible_by_seven_count = 0
prime_count = 0

for i in numbers(lst):
    if i % 7 == 0:
        divisible_by_seven_count += 1
    if is_prime(i):
        prime_count += 1

print(f"Ilość liczb podzielnych przez 7: {divisible_by_seven_count}")
print(f"Ilość liczb pierwszych: {prime_count}")
