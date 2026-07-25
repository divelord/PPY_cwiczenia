"""
ZAD06

Pobierz zdanie.
Sprawdź:
• czy zawiera słowo "Python"
• ile razy występuje litera "a"
• Zamień "Python"na "JAVA".
"""

text = input("Wprowadź zdanie: ")
print("Python" in text)
print(text.count("a"))
print(text.replace("Python", "JAVA"))
