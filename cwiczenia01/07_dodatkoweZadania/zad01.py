"""
ZAD01

Napisz program, który powinien:
Pobierać liczbę od użytkownika.
Wypisać:
• czy jest dodatnia/ujemna/zero
• czy jest parzysta
• jej zapis binarny i hex
• jej kwadrat
"""

x = int(input("Wprowadź liczbę: "))

if x > 0:
    print("Liczba jest dodatnia")
elif x < 0:
    print("Liczba jest ujemna")
else:
    print("Liczba jest równa 0")

if x % 2 == 0:
    print("Liczba jest parzysta")
else:
    print("Liczba jest nieparzysta")

print(bin(x))
print(hex(x))

print(x ** 2)
