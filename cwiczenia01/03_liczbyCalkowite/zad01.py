"""
ZAD01

Ustaw:n = 255
Wypisz:
• zapis binarny (bin)
• ósemkowy (oct)
• szesnastkowy (hex)
Zamień napisy:
"1111"
"FF"
"17"
na liczby całkowite, podając odpowiednią podstawę systemu.
"""

n = 255
print(bin(n))
print(oct(n))
print(hex(n))

a = "1111"
b = "FF"
c = "17"
print(int(a, 2))
print(int(b, 16))
print(int(c, 8))
