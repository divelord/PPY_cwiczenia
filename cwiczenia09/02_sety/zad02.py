"""
ZAD02

Dany jest napis.
Utwórz zbiór wszystkich unikalnych znaków występujących w tym napisie,
pomijając spacje oraz ignorując wielkość liter.
"""


def get_unique_characters(text):
    st = set()

    for ch in text:
        if ch != " ":
            st.add(ch.lower())

    return st


text = "abc def abc def asdfg XCVBN"

print(get_unique_characters(text))
