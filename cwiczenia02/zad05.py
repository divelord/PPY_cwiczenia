"""
ZAD 5

Napisz program zarządzający listą użytkowników.
Program powinien:
• przechowywać nazwy użytkowników w liście,
• dodawać nowych użytkowników oraz zapobiegać dodawaniu zduplikowanych nazw,
• umożliwiać wyszukiwanie użytkownika na liście,
• wyświetlać listę użytkowników posortowaną alfabetycznie.
Dodatkowo program powinien:
• wyświetlić pierwsze 5 nazw użytkowników używając slicing,
• znaleźć najdłuższą nazwę użytkownika.
"""

users = []

while True:
    inputUser = input("Wprowadź nazwę użytkownika (wpisz 0 aby zakończyć): ")

    if inputUser == "0":
        break

    if not inputUser:
        print("Nazwa nie może byc pusta")
        continue

    if inputUser in users:
        print("Użytkownik jest juz na liście")
    else:
        users.append(inputUser)

if users:
    while True:
        inputUser = input("Sprawdź, czy istnieje użytkownik (wpisz 0 aby zakonczyc): ")

        if inputUser == "0":
            break

        if inputUser in users:
            print("Użytkownik jest juz na liście")
        else:
            print("Użytkownika nie ma na liście")

    users_sorted = sorted(users)

    longest_username = users[0]

    for i in users:
        if len(i) > len(longest_username):
            longest_username = i

    print(f"Użytkownicy alfabetycznie: {users_sorted}")
    print(f"Pierwszych 5 użytkowników: {users[:5]}")
    print(f"Użytkownik z najdłuższą nazwą: {longest_username}")
else:
    print("Lista użytkowników jest pusta")
