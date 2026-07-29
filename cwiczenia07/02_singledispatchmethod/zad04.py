"""
ZAD04

Ewaluator wyrażeń
Zdefiniuj klasę Evaluator z metodą evaluate(value) wykorzystującą @singledispatchmethod:
• int → zwraca wartość,
• str → zwraca długość napisu,
• list → zwraca sumę przetworzonych elementów (rekurencyjnie).

Dodatkowo:
• Poprawnie zaimplementuj rekurencję,
• Dodaj obsługę błędów dla nieobsługiwanych typów.
"""
from functools import singledispatchmethod


class Evaluator:
    @singledispatchmethod
    def evaluate(self, value):
        raise TypeError("Unknown type")

    @evaluate.register(int)
    def _(self, value):
        return value

    @evaluate.register(str)
    def _(self, value):
        return len(value)

    @evaluate.register(list)
    def _(self, value):
        return sum(self.evaluate(i) for i in value)


evaluator = Evaluator()

try:
    print(evaluator.evaluate(10))
    print(evaluator.evaluate("abc"))
    print(evaluator.evaluate([1, 2, "abc"]))
    print(evaluator.evaluate(1.5))
except TypeError as e:
    print(e)
