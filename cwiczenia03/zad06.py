"""
ZAD06

Napisz program wczytujący liczbę N, a następnie dowolne liczby aż do momentu,
gdy użytkownik poda N różnych liczb.
Program powinien:
• wczytywać liczby od użytkownika,
• zakończyć wczytywanie, gdy liczba różnych podanych liczb osiągnie N.
Po zakończeniu wczytywania program powinien:
• wydrukować wszystkie różne liczby podane przez użytkownika,
• wydrukować liczby, które użytkownik podał więcej niż jeden raz.
"""

n = int(input("Podaj ile chcesz wpisać rożnych liczb: "))

unique_num = set()
repeated_num = set()

while len(unique_num) < n:
    num = int(input("Podaj liczbę: "))

    if num in unique_num:
        repeated_num.add(num)
    unique_num.add(num)

print(f"Podane różne liczby: {unique_num}")
print(f"Podane powtórzone liczby: {repeated_num}")
