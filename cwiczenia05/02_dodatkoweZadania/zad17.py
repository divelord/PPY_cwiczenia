"""
ZAD17

Utwórz klasę Stack wykorzystującą listę z metodami:
• push
• pop
• peek
• is_empty
"""


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        return str(self.items)


stack = Stack()
print(stack)
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack)
print(stack.pop())
print(stack)
print(stack.peek())
print(stack.is_empty())
