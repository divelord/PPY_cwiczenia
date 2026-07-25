"""
ZAD01

Pobierz zdanie od użytkownika.
Wykonaj:
• wypisz długość (len)
• zamień wszystkie spacje na _
• podziel zdanie na listę słów (split)
• wypisz pierwsze 3 znaki (slicing)
• wypisz ostatnie 4 znaki
"""

text = input("Podaj zdanie: ")
print(len(text))
print(text.replace(" ", "_"))
print(text.split(" "))
print(text[0:3])
print(text[-4:])
