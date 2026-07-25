import random

"""
ZAD 6

Napisz program symulujący grę papier–kamień–nożyce pomiędzy użytkownikiem a komputerem.
Program powinien:
• utworzyć listę możliwych ruchów: ["papier", "kamień", "nożyce"],
• losowo wybrać ruch komputera przy użyciu modułu random,
• wczytać ruch użytkownika,
• porównać ruchy i wyświetlić wynik rundy (wygrana, przegrana, remis).
Zasady gry:
• gra trwa maksymalnie 3 rundy,
• jeśli użytkownik lub komputer przegra 2 rundy z rzędu, gra kończy się wcześniej (po drugiej rundzie).
Dodatkowo program powinien:
• zapisywać ruchy użytkownika w liście,
• zapisywać ruchy komputera w liście,
• po zakończeniu gry wyświetlić:
    – wszystkie ruchy użytkownika,
    – wszystkie ruchy komputera,
    – liczbę wygranych, przegranych oraz remisów.
"""

moves = ["papier", "kamien", "nozyce"]
playing = True
game_count = 0
draws = 0

comp_win = 0
comp_lose = 0
comp_moves = []
comp_streak = 0

user_win = 0
user_lose = 0
user_moves = []
user_streak = 0

while playing:
    computer = random.choice(moves)
    user = input("Podaj ruch [papier/kamien/nozyce]: ")

    if user not in moves:
        print("Niepoprawny ruch, sprobuj jeszcze raz")
        continue

    comp_moves.append(computer)
    user_moves.append(user)

    if computer == user:
        print("Remis")
        draws += 1
        comp_streak = 0
        user_streak = 0
    elif computer == "papier" and user == "kamien" or computer == "kamien" and user == "nozyce" or computer == "nozyce" and user == "papier":
        print("Wygrana komputera")
        comp_win += 1
        comp_streak += 1
        user_lose += 1
        user_streak = 0
    elif user == "papier" and computer == "kamien" or user == "kamien" and computer == "nozyce" or user == "nozyce" and computer == "papier":
        print("Wygrana użytkownika")
        user_win += 1
        user_streak += 1
        comp_lose += 1
        comp_streak = 0

    print("\nkomputer : użytkownik")
    print(f"{comp_win} : {user_win}\n")

    game_count += 1

    if user_streak == 2:
        playing = False
        print("Wygrywa użytkownik")
    elif comp_streak == 2:
        playing = False
        print("Wygrywa komputer")
    elif game_count == 3:
        playing = False

        if comp_win > user_win:
            print("Wygrana z powodu rozegrania 3 rund")
            print("Wygrywa komputer")
        elif comp_win < user_win:
            print("Wygrana z powodu rozegrania 3 rund")
            print("Wygrywa użytkownik")
        else:
            print("Koniec po 3 rundach. Cały mecz kończy się remisem")

print(f"Ruchy użytkownika: {user_moves}")
print(f"Ruchy komputera: {comp_moves}")
print(f"Liczba wygranych użytkownika: {user_win}")
print(f"Liczba wygranych komputera: {comp_win}")
print(f"Liczba przegranych użytkownika: {user_lose}")
print(f"Liczba przegranych komputera: {comp_lose}")
print(f"Liczba remisów: {draws}")
