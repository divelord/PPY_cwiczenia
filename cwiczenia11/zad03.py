"""
ZAD03

Utwórz klasę TextTools ze statyczną metodą countVowels(text), która zlicza samogłoski w napisie.
Następnie dodaj kolejną statyczną metodę isPalindrome(text), która sprawdza, czy tekst jest palindromem.
Przed sprawdzeniem metoda powinna:
• zamienić wszystkie litery na małe,
• usunąć spacje,
• usunąć wszystkie znaki niebędące literami.

Na przykład poniższy tekst powinien zostać rozpoznany jako palindrom:
"k.a;jAk"

Wskazówki:
• Użyj str.lower().
• Użyj str.isalpha(), aby pozostawić tylko litery.
• Palindrom czyta się tak samo od początku i od końca.
"""


class TextTools:
    @staticmethod
    def countVowels(text):
        vowel_count = 0
        vowels = "aeiouy"

        for ch in text.lower():
            if ch in vowels:
                vowel_count += 1

        return vowel_count

    @staticmethod
    def isPalindrome(text):
        result_text = ""

        for ch in text.lower():
            if ch.isalpha():
                result_text += ch

        return result_text == result_text[::-1]


print(TextTools.countVowels("k.a;jAk"))
print(TextTools.isPalindrome("k.a;jAk"))
