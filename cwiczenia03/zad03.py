import random

"""
ZAD03

Napisz program symulujący grę papier–kamień–nożyce pomiędzy użytkownikiem a komputerem.
Program powinien:
• przechowywać możliwe ruchy w słowniku (dict) mapującym nazwę ruchu na liczbę,
np. "papier"→ 1, "kamień"→ 2, "nożyce"→ 3,
• wczytać ruch użytkownika i sprawdzić, czy jest poprawny (czy znajduje się w słowniku),
• wylosować ruch komputera przy użyciu modułu random,
• przekształcić ruchy na wartości liczbowe przy użyciu słownika,
• porównać ruchy i określić wynik rundy,
• rozegrać maksymalnie 3 rundy gry.
Dodatkowo program powinien:
• zapisywać historię rund w postaci krotek (tuple) w formie:
    (ruch_użytkownika, ruch_komputera, wynik)
• przechowywać liczbę wygranych, przegranych i remisów w słowniku,
• po zakończeniu gry wyświetlić:
    – historię wszystkich rund,
    – liczbę wygranych, przegranych oraz remisów,
    – podsumowanie całej gry.
"""

moves = {"papier": 1, "kamien": 2, "nozyce": 3}
moves_for_num = {1: "papier", 2: "kamien", 3: "nozyce"}
stats = {"wygrane": 0, "przegrane": 0, "remis": 0}
move_history = []

game_count = 0
playing = True

while playing:
    user_input = input("Podaj ruch [papier/kamien/nozyce]: ")

    if user_input not in moves:
        print("niepoprawny ruch, sprobuj jeszcze raz")
        continue

    user_move = moves[user_input]
    comp_move = random.randint(1, 3)
    comp_move_for_num = moves_for_num[comp_move]
    result = ""

    if user_move == comp_move:
        result = "remis"
        stats["remis"] += 1
    elif user_move == 1 and comp_move == 2 or user_move == 2 and comp_move == 3 or user_move == 3 and comp_move == 1:
        result = "wygrana"
        stats["wygrane"] += 1
    elif comp_move == 1 and user_move == 2 or comp_move == 2 and user_move == 3 or comp_move == 3 and user_move == 1:
        result = "przegrana"
        stats["przegrane"] += 1

    print(f"wynik: {result}")
    move_history.append((user_input, comp_move_for_num, result))

    game_count += 1

    if game_count == 3:
        playing = False

print(f"Historia: {move_history}")
print(f"Statystyki: {stats}")

if stats["wygrane"] > stats["przegrane"]:
    print("Wygrał użytkownik")
elif stats["wygrane"] < stats["przegrane"]:
    print("Wygrał komputer")
else:
    print("Remis")
