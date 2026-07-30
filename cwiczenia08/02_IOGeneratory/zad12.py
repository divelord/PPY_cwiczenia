"""
ZAD12

Utwórz generator, który czyta plik fragmentami (np. po 1024 znaki).
"""


def read_file(file_path, size):
    with open(file_path, "r", encoding="utf-8") as file:
        while True:
            text = file.read(size)

            if not text:
                break

            yield text


gen = read_file("../THE_HOBBIT.txt", 1024)

for line in range(10):
    print(next(gen))
