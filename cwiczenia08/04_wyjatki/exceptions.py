"""ZAD01"""


class FileEmptyException(Exception):
    def __init__(self, value=""):
        super().__init__("Plik jest pusty")


"""ZAD02, ZAD03, ZAD07, ZAD09"""


class NoRingException(Exception):
    def __init__(self, value=""):
        super().__init__("Brak pierścienia")


"""ZAD04, ZAD09"""


class NoBilboException(Exception):
    def __init__(self, value=""):
        super().__init__("Brak Bilba")


"""ZAD05"""


class LineTooLongException(Exception):
    def __init__(self, value=""):
        super().__init__("Linia za długa")


"""ZAD06"""


class NoPreciousException(Exception):
    def __init__(self, value=""):
        super().__init__("Nie znaleziono skarbu")


"""ZAD08"""


class NoNameException(Exception):
    def __init__(self, value=""):
        super().__init__("Brak imienia postaci")


"""ZAD10"""


class WrongFilePath(Exception):
    def __init__(self, value=""):
        super().__init__("Zły format pliku")
