"""
ZAD02

Napisz program zarządzający zbiorem użytkowników.
Program powinien:
• przechowywać nazwy użytkowników w zbiorze (set),
• umożliwić dodawanie nowych użytkowników,
• sprawdzać, czy dany użytkownik już istnieje w zbiorze,
• wyświetlić wszystkich użytkowników w kolejności alfabetycznej,
• wyświetlić liczbę unikalnych użytkowników.
Dodatkowo program powinien:
• utworzyć krotkę (tuple) zawierającą trzech pierwszych użytkowników po sortowaniu,
• znaleźć użytkownika o najdłuższej nazwie,
• sprawdzić, czy dwóch wybranych użytkowników znajduje się w zbiorze.
Dodatkowo program powinien:
• wyświetlić wybraną część listy użytkowników,
• znaleźć użytkownika o najdłuższej nazwie.
"""

users = set()

while True:
    user_input = input("Wprowadź użytkownika (wpisz 0 aby zakończyć): ")

    if user_input == "0":
        break

    if user_input in users:
        print("Użytkownik jest juz w systemie")
        continue
    else:
        users.add(user_input)

if users:
    users_sorted = sorted(list(users))
    users_tuple = tuple(users_sorted[:3])

    print(f"Użytkownicy alfabetycznie: {users_sorted}")
    print(f"Liczba unikalnych użytkowników: {len(users_sorted)}")
    print(f"Trzech pierwszych użytkowników: {users_tuple}")
    print(f"Użytkownik o najdłuższej nazwie: {max(users_sorted, key=len)}")

    user1 = input("Wprowadź użytkownika1: ")
    user2 = input("Wprowadź użytkownika2: ")

    if user1 in users_sorted and user2 in users_sorted:
        print("Obaj użytkownicy są na liście")
    else:
        print("Co najmniej jeden z użytkowników nie znajduje się na liście")

    if len(users_sorted) > 1:
        print(f"Zakres od 0 do {len(users_sorted) - 1}")
        begin = int(input("Wprowadź zakres początkowy: "))
        end = int(input("Wprowadź zakres końcowy: "))

        print(users_sorted[begin:end + 1])
else:
    print("Lista użytkowników jest pusta")
