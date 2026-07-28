"""
ZAD19

Utwórz klasę Person oraz klasę dziedziczącą Employee z:
• dodatkowym atrybutem salary
• nadpisaną metodą __str__
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} {self.age}'


class Employee(Person):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = salary

    def __str__(self):
        return f'{self.name} {self.age} {self.salary}'


person = Person('XYZ', 18)
employee = Employee("ABC", 24, 1000)
print(person)
print(employee)
