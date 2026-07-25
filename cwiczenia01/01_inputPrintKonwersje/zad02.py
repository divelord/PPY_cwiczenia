"""
ZAD02

Użytkownik na wejściu podaje liczby a i b.
Celem programu jest podzielenie jednej liczby przez drugiej,
a następnie wykonania na tych samych liczbach operacji dzielenia całkowitego.
np.
print(a / b)
print(a // b)
Następnie sprawdzenia typu wartości podanej na wyjściu.
np.
print(type(a/b))
print(type(a//b))
Czemu typ się zmienił?
"""

x = int(input("Podaj liczbę: "))
y = int(input("Podaj liczbę: "))

print(x / y)
print(x // y)

print(type(x / y))  # float
print(type(x // y))  # int

# Typ zmienił się, ponieważ zwykłe dzielenie zawsze zwróci liczbę z częścią ułamkową,
# a dzielenie całkowite zawsze zwróci część całkowitą z dzielenia.
