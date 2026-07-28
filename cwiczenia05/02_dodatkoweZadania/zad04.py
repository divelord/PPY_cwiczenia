"""
ZAD04

Dany jest słownik miłośników książek.

1. Napisz funkcję, która przyjmuje słownik oraz imię osoby i zwraca:
    1. imię osoby mającej najwięcej wspólnych książek,
    2. liczbę wspólnych książek,
    3. zbiór książek do polecenia (książki, które ta osoba ma, a podana osoba nie).

2. Napisz funkcję, która zwraca:
    1. najpopularniejszą książkę posiadaną przez daną osobę,
    2. liczbę innych osób, które ją posiadają.

3. Napisz funkcję, która zwraca:
    1. najpopularniejszą książkę nieposiadaną przez daną osobę,
    2. liczbę osób, które ją posiadają.
"""


def zad1(bibliophiles, name):
    books = bibliophiles[name]
    best_match = None
    max_common_books_count = -1

    for key, value in bibliophiles.items():
        if key == name:
            continue

        common_books_count = len(books & value)

        if common_books_count > max_common_books_count:
            max_common_books_count = common_books_count
            best_match = key

    recommendations = bibliophiles[best_match] - books

    return best_match, max_common_books_count, recommendations


def zad2(bibliophiles, name):
    books = bibliophiles[name]
    owned_books_count = {}

    for i in books:
        owned_books_count[i] = 0

    for key, value in bibliophiles.items():
        if key == name:
            continue

        for i in value:
            if i in books:
                owned_books_count[i] += 1

    most_popular_book = max(owned_books_count, key=owned_books_count.get)

    return most_popular_book, owned_books_count[most_popular_book]


def zad3(bibliophiles, name):
    books = bibliophiles[name]
    unowned_books_count = {}

    for key, value in bibliophiles.items():
        if key == name:
            continue

        for i in value:
            if i not in books:
                unowned_books_count[i] = unowned_books_count.get(i, 0) + 1

    most_popular_book = max(unowned_books_count, key=unowned_books_count.get)

    return most_popular_book, unowned_books_count[most_popular_book]


bibliophiles = {
    "John": {1, 2, 7, 11, 29},
    "Mary": {7, 9, 11, 5},
    "Jane": {1, 4, 5},
    'Bill': {7, 11, 1, 2, 9},
    "Kate": {4, 5, 9, 11}
}
print(f"1. {zad1(bibliophiles, 'John')}")
print(f"2. {zad2(bibliophiles, 'John')}")
print(f"3. {zad3(bibliophiles, 'John')}")
