import random

"""
ZAD 3

Napisz program analizujący dane liczbowe.
Program powinien:
• wygenerować losową listę 20 liczb,
• obliczyć średnią wartość,
• znaleźć największą i najmniejszą liczbę,
• policzyć ile liczb jest większych od średniej.
Dodatkowo program powinien:
• wyświetlić tylko liczby parzyste,
• wyświetlić co drugi element listy używając slicing,
• znaleźć drugą największą liczbę.
"""

num_list = []
for i in range(20):
    num_list.append(random.randint(0, 100))

avg = sum(num_list) / len(num_list)
max_value = max(num_list)
min_value = min(num_list)

bigger_than_value = 0
for i in num_list:
    if i > avg:
        bigger_than_value += 1

even = []
for i in num_list:
    if i % 2 == 0:
        even.append(i)

unique = sorted(list(set(num_list)))

print(f"Średnia wartość: {avg}")
print(f"Największa liczba: {max_value}")
print(f"Najmniejsza liczba: {min_value}")
print(f"Ilość większych od średniej: {bigger_than_value}")
print(f"Parzyste: {even}")
print(f"Co drugi element: {num_list[::2]}")
print(f"Druga największa liczba: {unique[-2]}")
