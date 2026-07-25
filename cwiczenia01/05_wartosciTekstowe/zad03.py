"""
ZAD03

Policz, ile cyfr znajduje się w tekście podanym przez użytkownika.
"""

text = input("Podaj tekst: ")
count = 0
for i in text:
    if i.isdigit():
        count += 1
print(count)
