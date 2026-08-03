"""
ZAD05

Utwórz klasę Student, zawierającą:
• atrybuty instancji: name, age,
• atrybut klasowy studentCount,
• metodę klasową howManyStudents(), zwracającą liczbę studentów.
"""


class Student:
    studentCount = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.studentCount += 1

    @classmethod
    def howManyStudents(cls):
        return cls.studentCount


s1 = Student("A", 10)

print(Student.howManyStudents())

s2 = Student("B", 20)
s3 = Student("C", 30)

print(Student.howManyStudents())
