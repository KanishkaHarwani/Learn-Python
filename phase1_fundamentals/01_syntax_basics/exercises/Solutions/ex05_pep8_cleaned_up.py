import os
import sys


class Student:
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks

    def average(self):
        total = 0
        for mark in self.marks:
            total += mark
        return total / len(self.marks)


def print_student(student):
    print("Name:", student.name)
    print("Age:", student.age)
    print("Average:", student.average())


students = [
    Student("Alice", 20, [90, 85, 88]),
    Student("Bob", 21, [75, 80, 79]),
    Student("Charlie", 19, [95, 98, 100]),
]

for student in students:
    print_student(student)

if len(students) > 0:
    class_average = sum(student.average() for student in students) / len(students)
    print("Class Average:", class_average)