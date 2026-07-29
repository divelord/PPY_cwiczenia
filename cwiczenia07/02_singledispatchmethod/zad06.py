"""
ZAD06

System logowania
Utwórz klasę Logger z metodą log(value):
• str → zapisuje komunikat,
• dict → zapisuje pary klucz-wartość,
• Exception → zapisuje szczegóły błędu.

Dodatkowo:
• Przechowuj logi wewnętrznie,
• Zaimplementuj __iter__(), aby umożliwić iterację po logach.
"""
from functools import singledispatchmethod


class Logger:
    def __init__(self):
        self.logs = []

    @singledispatchmethod
    def log(self, value):
        entry = f"[Unknown]: {str(value)}"
        self.logs.append(entry)

    @log.register(str)
    def _(self, value):
        entry = f"[msg]: {value}"
        self.logs.append(entry)

    @log.register(dict)
    def _(self, value):
        items = ", ".join([f"{k}:{v}" for k, v in value.items()])
        entry = f"[dict]: {items}"
        self.logs.append(entry)

    @log.register(Exception)
    def _(self, value):
        entry = f"[Exception]: {value}"
        self.logs.append(entry)

    def __iter__(self):
        return iter(self.logs)


logger = Logger()

try:
    logger.log("abc")
    logger.log({"a": 1, "b": 2})
    logger.log(1 / 0)
except Exception as e:
    logger.log(e)

for log in logger:
    print(log)
