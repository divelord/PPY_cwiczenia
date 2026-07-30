"""
ZAD04

Śledzenie Pierścienia Smeagola
Jedyny Pierścień rzadko jest nazywany wprost. Często pojawia się pod różnymi określeniami,
takimi jak "ring", "my precious" lub inne pośrednie odniesienia.
Napisz dekorator ring_tracker, który przekształca funkcję w generator przetwarzający tekst słowo po słowie.
Dekorator powinien:
• w sposób leniwy czytać plik hobbit.txt
• zwracać kolejne słowa
Udekorowana funkcja powinna:
• wykrywać odniesienia do Pierścienia, w tym:
    – słowo "ring" (bez uwzględniania wielkości liter)
    – wyrażenie "my precious"
    – inne podobne określenia (możesz zdefiniować własny zestaw słów kluczowych lub fraz)
• zwracać krótki kontekst (3 słowa przed i 3 słowa po każdym wystąpieniu)
Wskazówka: zastanów się, jak wykrywać frazy wielowyrazowe (np. "my precious")
podczas przetwarzania strumienia słów.
"""


def ring_tracker(func):
    def wrapper(file_path):
        def generator():
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    word_lst = line.split()
                    for word in word_lst:
                        clean_word = word.strip(",!?;:()\"'").lower()
                        if clean_word:
                            yield clean_word

        return func(generator())

    return wrapper


@ring_tracker
def find_ring(gen):
    word_lst = list(gen)

    for i in range(len(word_lst)):
        found = False
        match_len = 0

        if word_lst[i] == "ring" or word_lst[i] == "precious":
            found = True
            match_len = 1
        elif i + 1 < len(word_lst) and word_lst[i] == "my" and word_lst[i + 1] == "precious":
            found = True
            match_len = 2

        if found:
            start = max(0, i - 3)
            end = i + match_len + 3
            yield " ".join(word_lst[start:end])


for line in find_ring("../THE_HOBBIT.txt"):
    print(line)
