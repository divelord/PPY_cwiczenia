"""
ZAD04

Wczytaj liczbę N od użytkownika. Wygeneruj, za pomocą range,
listę lst liczb całkowitych o długości dokładnie N.
Pierwszy wyraz powinien być różny od zera,
a krok (różnica ciągu) różny od 1.
Program powinien:
• zdefiniować dowolny predykat (funkcję zwracającą True lub False) przyjmujący
liczbę całkowitą,
• utworzyć listę liczb z lst, dla których dany predykat zwraca True,
• wydrukować tę listę.
Dodatkowo program powinien:
• utworzyć funkcję przyjmującą listę oraz predykat,
• funkcja powinna zwracać listę elementów spełniających dany predykat,
• wypróbować funkcję dla różnych predykatów.
"""


def is_even(n):
    if n % 2 == 0:
        return True
    return False


def is_divisible_by_3(n):
    if n % 3 == 0:
        return True
    return False


def predicate(lst, pred):
    res = []
    for i in lst:
        if pred(i):
            res.append(i)
    return res


n = int(input('Podaj długość listy: '))

while True:
    x = int(input('Podaj element początkowy listy (różny od 0): '))
    if x == 0:
        print("Element początkowy ma być różny od 0")
        continue
    break

while True:
    y = int(input('Podaj różnicę elementów listy (różny od 1): '))
    if y == 1:
        print("Różnica elementów ma być różna od 1")
        continue
    break

lst = list(range(x, x + n * y, y))
print(lst)

even_lst = [i for i in lst if is_even(i)]
print(even_lst)

print(predicate(lst, is_divisible_by_3))
