"""
ZAD02

Pobierz od użytkownika liczbę.
Sprawdź:
• czy jest dodatnia i parzysta,
• czy jest ujemna lub większa od 100,
• użyj not w jednym warunku.
"""

x = int(input("Podaj liczbę: "))

if x > 0 and x % 2 == 0:
    print("Liczba jest dodatnie i parzysta")
if x < 0 or not x <= 100:
    print("Liczba jest ujemna lub wieksza od 100")
