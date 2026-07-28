"""
ZAD15

Utwórz klasę Counter, która:
• posiada zmienną klasową zliczającą wszystkie utworzone obiekty
• zwiększa ją w konstruktorze
"""


class Counter:
    count = 0

    def __init__(self):
        Counter.count += 1


counter1 = Counter()
counter2 = Counter()
counter3 = Counter()
counter4 = Counter()
counter5 = Counter()
print(Counter.count)
