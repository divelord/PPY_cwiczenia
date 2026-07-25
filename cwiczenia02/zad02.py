import random

"""
ZAD 2

Napisz program symulujący grę w zgadywanie liczby.
Program powinien:
• wygenerować losową liczbę z zakresu od 1 do 100,
• umożliwić użytkownikowi zgadywanie liczby w pętli while,
• informować użytkownika, czy podana liczba jest zbyt mała czy zbyt duża,
• zakończyć działanie po odgadnięciu liczby.
Na końcu programu należy:
• wyświetlić liczbę prób,
• zapisać wszystkie zgadywane liczby w liście,
• wyświetlić ostatnie 3 próby używając slicing.
"""

x = random.randint(1, 100)
count = 0
guessed = []
isGuessed = False

while not isGuessed:
    y = int(input("Podaj liczbę: "))

    count += 1
    guessed.append(y)

    if x == y:
        print("Zgadłeś liczbę")
        isGuessed = True
    elif x < y:
        print("Twoja liczba jest większa, podaj mniejsza")
    else:
        print("Twoja liczba jest mniejsza, podaj większa")

print(f"Ilość prób: {count}")
print(f"Wszystkie twoje próby {guessed}")
print(f"Ostatnie 3 zgadywane liczby: {guessed[-3:]}")
