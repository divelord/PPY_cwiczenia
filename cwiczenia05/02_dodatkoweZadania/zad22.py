"""
ZAD22

Napisz funkcję best3, która dla strumienia krotek (name, score) (reprezentowanego jako lista takich krotek)
na bieżąco śledzi trzech liderów (osoby i ich najlepsze wyniki) i zwraca końcową trójkę zwycięzców.
Od momentu, gdy liczba różnych osób osiągnie 3, wypisuj każdą zmianę w czołowej trójce.
"""


def best3(kr):
    leaders = {}
    top3 = []

    for name, score in kr:
        if name not in leaders or score > leaders[name]:
            leaders[name] = score

            new_top3 = sorted(leaders.items(), key=lambda x: x[1], reverse=True)[:3]

            if len(new_top3) >= 3 and new_top3 != top3:
                print(f"zmiana: {new_top3}")

            top3 = new_top3

    return top3


tuple_lst = [
    ("A", 10), ("B", 5), ("C", 15), ("D", 10),
    ("A", 5), ("B", 15), ("C", 20), ("D", 5)
]
print(best3(tuple_lst))
