"""
ZAD02

Napisz dekorator yield_words, który przekształca funkcję operującą na pojedynczym słowie
w funkcję opartą na generatorze przetwarzającą cały plik.
Dekorator powinien:
• otwierać plik hobbit.txt
• zwracać słowa jedno po drugim
• przekazywać każde słowo do udekorowanej funkcji
Wykorzystaj go do:
• filtrowania słów dłuższych niż 6 znaków
• policzenia, ile słów zaczyna się wielką literą
"""


def yield_words(func):
    def wrapper():
        with open("../THE_HOBBIT.txt", "r", encoding="utf-8") as file:
            for line in file:
                word_lst = line.split()
                for word in word_lst:
                    result = func(word)
                    if result is not None:
                        yield result

    return wrapper


@yield_words
def filter_words_longer_than_6(word):
    if len(word) > 6:
        return word
    return None


@yield_words
def count_upper_words(word):
    if word and word[0].isupper():
        return word
    return None


gen_fil = filter_words_longer_than_6()
print("Filtered words:")
for word in range(10):
    print(next(gen_fil))

upper_word_count = 0
for word in count_upper_words():
    upper_word_count += 1
print(f"Counted words: {upper_word_count}")
