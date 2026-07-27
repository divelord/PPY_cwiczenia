"""
ZAD02

Zrób klasę FibonacciSequence(n), która generuje n pierwszych liczb w ciągu Fibonacciego.
Powinna zawierać metodę __iter__
• Zrób iterator jako osobną klasę.
• Dodaj opcję iterowania wstecz.
"""


class FibonacciSequence:
    def __init__(self, n):
        self.num_list = []
        a, b = 0, 1

        for num in range(n):
            self.num_list.append(a)
            a, b = b, a + b

    def __iter__(self):
        return iter(FibonacciIterator(self.num_list))

    def reversed(self):
        return iter(FibonacciIterator(self.num_list, reverse=True))


class FibonacciIterator:
    def __init__(self, num_list, reverse=False):
        self.num_list = num_list
        self.reverse = reverse
        self.index = 0 if not self.reverse else len(self.num_list) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if not self.reverse:
            if self.index >= len(self.num_list):
                raise StopIteration

            num = self.num_list[self.index]
            self.index += 1

            return num
        else:
            if self.index < 0:
                raise StopIteration

            num = self.num_list[self.index]
            self.index -= 1

            return num


fibonacci = FibonacciSequence(10)

print("Fibonacci:")
for i in fibonacci:
    print(i)

print("\nFibonacci wstecz:")
for i in fibonacci.reversed():
    print(i)
