"""
ZAD05

Drużyna Thorina
Krasnoludy, czarodzieje i hobbici pojawiają się w trakcie całej podróży.
Napisz dekorator character_stream, który:
• czyta plik w sposób leniwy
• zwraca słowa zapisane wielką literą (potencjalne imiona postaci)
Udekorowana funkcja powinna:
• odfiltrować słowa, które najprawdopodobniej nie są imionami (np. znajdują się
na początku zdań)
• policzyć, ile razy każda postać się pojawia
Wypisz 5 najczęściej występujących imion postaci.
"""


def character_stream(func):
    def wrapper(file_path):
        def generator(path):
            with open(path, "r", encoding="utf-8") as file:
                is_start_sentence = True

                for line in file:
                    word_lst = line.split()

                    for word in word_lst:
                        is_end_word = word[-1] in ".!?" if word else False
                        clean_word = word.strip(",!?;:()\"'")

                        if clean_word and clean_word[0].isupper():
                            yield clean_word, is_start_sentence

                        is_start_sentence = is_end_word

        return func(generator(file_path))

    return wrapper


@character_stream
def characters(stream):
    word_counts = {}

    for name, is_start_sentence in stream:
        if not is_start_sentence:
            word_counts[name] = word_counts.get(name, 0) + 1

    return sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:5]


gen = characters("../THE_HOBBIT.txt")

for name, count in gen:
    print(name, count)
