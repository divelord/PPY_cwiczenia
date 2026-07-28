"""
ZAD02

Pewna liczba aktorów (numerowanych od 1) wystąpiła w filmach oznaczonych ‘a”, ‘b”, ‘c” itd.
W słowniku films kluczami są tytuły filmów, a wartościami listy aktorów.
Napisz funkcję, która przyjmuje taki słownik i zwraca nowy słownik, w którym:
• kluczami są identyfikatory aktorów,
• wartościami są listy filmów, w których wystąpili.
Wypisz wynik posortowany:
• malejąco według liczby filmów,
• rosnąco według identyfikatora aktora w przypadku remisu.
"""


def new_movie_dic(movies):
    actors = {}

    for key, value in movies.items():
        for i in value:
            if i not in actors:
                actors[i] = []
            actors[i].append(key)

    actors = dict(sorted(actors.items(), key=lambda x: (-len(x[1]), x[0])))

    return actors


movies_list = {
    "a": ["a1", "a2", "a3", "a4", "a5", "a6"],
    "b": ["a2", "a4", "a1"],
    "c": ["a6", "a3"]
}
print(new_movie_dic(movies_list))
