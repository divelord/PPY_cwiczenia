"""
ZAD21

Utwórz klasę implementującą protokół iteratora (__iter__, __next__), która iteruje po kwadratach liczb do n.
"""


class Squares:
    def __init__(self, n):
        self.n = n
        self.current_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num <= self.n:
            result = self.current_num ** 2
            self.current_num += 1
            
            return result
        else:
            raise StopIteration


for i in Squares(5):
    print(i)
