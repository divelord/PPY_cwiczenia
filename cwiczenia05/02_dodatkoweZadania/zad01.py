"""
ZAD01

Napisz program, który w pętli (while) wczytuje linie z konsoli.
Każda linia zawiera jedną, dwie lub trzy liczby.
Dla każdej linii utwórz krotkę zawierającą:
• napis ‘S” (kwadrat), ‘R” (prostokąt) lub ‘C” (prostopadłościan)
  w zależności od liczby podanych wartości;
• krotkę z podanymi liczbami;
• liczbę będącą polem lub objętością odpowiedniej figury.
Przechowuj krotki w liście.
Pętla kończy się po wprowadzeniu pustej linii (ENTER), następnie wypisz listę.
"""

lst = []

while True:
    size_input = input("Enter sizes: ")

    if not size_input:
        break

    sizes_lst = list(map(int, size_input.split()))
    size_tuple = tuple(sizes_lst)

    if len(sizes_lst) == 1:
        area = size_tuple[0] * size_tuple[0]
        res_tuple = ("S", size_tuple, area)
        lst.append(res_tuple)
    elif len(sizes_lst) == 2:
        area = size_tuple[0] * size_tuple[1]
        res_tuple = ("R", size_tuple, area)
        lst.append(res_tuple)
    elif len(sizes_lst) == 3:
        area = size_tuple[0] * size_tuple[1] * size_tuple[2]
        res_tuple = ("C", size_tuple, area)
        lst.append(res_tuple)
    else:
        print("Invalid size")

print(lst)
