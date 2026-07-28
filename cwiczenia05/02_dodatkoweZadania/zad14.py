"""
ZAD14

Utwórz klasę Student z:
• imieniem i listą ocen
• metodą dodawania oceny
• metodą obliczania średniej
"""


class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade):
        self.grades.append(grade)

    def avg_grade(self):
        return sum(self.grades) / len(self.grades)

    def __str__(self):
        return f'{self.name}, {self.grades}, {round(self.avg_grade(), 2)}'


student = Student("XYZ", [2, 4, 3])
print(student)
student.add_grade(5)
student.add_grade(4)
print(student)
