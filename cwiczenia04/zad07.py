"""
ZAD07

Z użyciem generatora, napisz nieskończoną pętlę for iterującą po liczbach
[0, 1, 2, ... , ∞ ]
"""


def num_generator():
    num = 0

    while True:
        yield num
        num += 1


for i, number in zip(range(10), num_generator()):
    print(number)
