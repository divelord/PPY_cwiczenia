"""
ZAD09

Napisz funkcję, która sprawdza plik i zgłasza:
• NoRingException, jeśli brakuje słowa "ring"
• NoBilboException, jeśli brakuje słowa "Bilbo"
Zwróć sukces tylko wtedy, gdy oba słowa występują.
"""
from exceptions import NoRingException, NoBilboException


def check(path):
    found_ring = False
    found_bilbo = False

    with (open(path, "r", encoding="utf-8") as file):
        for line in file:
            word_lst = line.split()

            for word in word_lst:
                clean_word = word.strip(".,!?;:()\"'")

                if clean_word == "ring":
                    found_ring = True

                if clean_word == "Bilbo":
                    found_bilbo = True

            if found_ring and found_bilbo:
                print("Sukces")
                return

        if not found_ring:
            raise NoRingException()
        if not found_bilbo:
            raise NoBilboException()


try:
    check("../THE_HOBBIT.txt")
except NoRingException as e:
    print(e)
except NoBilboException as e:
    print(e)
