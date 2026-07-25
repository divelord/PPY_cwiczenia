"""
ZAD01

Napisz program wczytujący dane do zmiennej. Najpierw niech to będą dane tekstowe.
Spróbuj tą zmienną:
• dodać do innej wartości typu tekstowego.
• dodać do innej wartości typu liczbowego.
• pomnożyć przez liczbę.
• pomnożyć przez wartość tekstową.
• podzielić przez liczbę.
• podzielić przez wartość tekstową.
• odjąć wartość tekstową.
• odjąć liczbę.
Co zadziałało?
Tam, gdzie nie wystąpił błąd spróbuj użyć funkcji type() do sprawdzenia typu wyniku operacji.
Spróbuj zrzutować tę zmienną na wartość liczbową i ponowić wyżej wymienione czynności.
"""

a = "nie"
b = 2

x = input("Podaj tekst: ")

print(x + a)  # wykona
type(x + a)  # string
print(x + b)  # błąd

print(x * a)  # błąd
print(x * b)  # wykona
type(x * b)  # string

print(x / a)  # błąd
print(x / b)  # błąd

print(x - b)  # błąd
print(x - a)  # błąd

y = int(input("Podaj liczbę: "))

print(y + a)  # błąd
print(y + b)  # wykona
type(y + b)  # int

print(y * a)  # wykona
type(y * a)  # string
print(y * b)  # wykona
type(y * b)  # int

print(y / a)  # błąd
print(y / b)  # wykona
type(y / b)  # float

print(y - a)  # błąd
print(y - b)  # wykona
type(y - b)  # int
