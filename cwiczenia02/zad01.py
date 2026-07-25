import random

"""
ZAD 1

Napisz program, który powinien:
• wygenerować listę 50 losowych wyników studentów (0–100 punktów),
• przypisać oceny według skali:
    – 90–100 : 5
    – 75–89 : 4
    – 60–74 : 3
    – poniżej 60 : 2
• obliczyć średni wynik,
• policzyć ilu studentów zdało,
• znaleźć 5 najlepszych wyników używając sortowania oraz slicing.
"""

results = []
grades = []

for i in range(50):
    results.append(random.randint(0, 100))

for i in results:
    if i >= 90:
        grades.append(5)
    elif i >= 75:
        grades.append(4)
    elif i >= 60:
        grades.append(3)
    else:
        grades.append(2)

avg = sum(results) / len(results)

passed = 0
for i in grades:
    if i > 2:
        passed += 1

results_sorted = sorted(results, reverse=True)

print(f"Wyniki: {results}")
print(f"Oceny: {grades}")
print(f"Średni wynik: {avg}")
print(f"Zdało: {passed}")
print(f"Najlepsze 5 wyników: {results_sorted[0:5]}")
