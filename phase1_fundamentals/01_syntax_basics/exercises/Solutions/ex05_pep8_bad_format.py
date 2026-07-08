import os,sys

class student:
 def __init__(self,name,age,marks):
  self.name=name;self.age=age;self.marks=marks

 def average(self):
      total=0
      for i in self.marks: total+=i
      return total/len(self.marks)

def PrintStudent(student):
 print("Name:",student.name)
 print("Age:",student.age)
 print("Average:",student.average())

students=[student("Alice",20,[90,85,88]),student("Bob",21,[75,80,79]),student("Charlie",19,[95,98,100])]

for s in students:
 PrintStudent(s)

if len(students)>0:
 print("Class Average:",sum([s.average() for s in students])/len(students))