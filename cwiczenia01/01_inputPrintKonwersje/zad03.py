"""
ZAD03

Zrób prosty "kalkulator". Pobierz od użytkownika dwie liczby.
Wypisz:
• ich sumę
• różnicę
• iloczyn
• dzielenie zwykłe (/)
• dzielenie całkowite (//)
• potęgowanie (**)
Użyj różnych wersji print:
• z przecinkami
• z dodawaniem napisów
• z f-string
"""

x = int(input("Podaj liczbę: "))
y = int(input("Podaj liczbę: "))

print("Suma: ", x + y)
print("Różnica: ", x - y)
print("Iloczyn: " + str(x * y))
print("Dzielenie: " + str(x / y))
print(f"Dzielenie całkowite: {x // y}")
print(f"Potęgowanie: {x ** y}")
