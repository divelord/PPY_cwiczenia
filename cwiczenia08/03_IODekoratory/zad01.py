"""
ZAD01

Napisz dekorator line_by_line, który przekształca funkcję tak,
aby przetwarzała plik w sposób leniwy przy użyciu generatora.
Funkcja udekorowana powinna:
• przyjmować ścieżkę do pliku jako argument
• wewnętrznie iterować po pliku linia po linii (z użyciem generatora)
• stosować oryginalną funkcję do każdej linii
Przetestuj dekorator na funkcji, która zlicza, ile linii zawiera słowo "Bilbo".
"""


def line_by_line(func):
    def wrapper(file_path):
        def generator(path):
            with open(path, "r", encoding="utf-8") as file:
                for line in file:
                    yield line

        return func(generator(file_path))

    return wrapper


@line_by_line
def word_count(lines):
    count = 0
    for line in lines:
        if "Bilbo" in line:
            count += 1
    return count


print(word_count("../THE_HOBBIT.txt"))
