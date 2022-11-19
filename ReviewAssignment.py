#!/bin/python3

class Student():
	def __init__(self, name,year):
		self.name = name
		self.year = year
		self.grades = []
		self.attendance =[]

	def add_grade(self, grade):
		if type(grade) == Grade:
			self.grades.append(grade.score)
		else:
			pass
	def get_average(self):
		total = 0
		student_grade = len(self.grades)
		for i in range(0,student_grade):
			total += self.grades[i].get_score()
		return total/len(self.grades)
		
class Grade():
	minimum_passing = 65
	def __init__(self,score):
		self.score = score


	def is_passing(self):
		if self.score >= Grade.minimum_passing:
			return " passing "
		else:
			return " fail"

	def get_score(self):
		return self.grades

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("pieter Bruegel the Elder", 8)

grade1 = Grade(100)
grade2 = Grade(60)
grade3 = Grade(50)

pieter.add_grade(grade1)
pieter.add_grade(grade2)
pieter.add_grade(grade3)

print(pieter.grades)
print(grade1.is_passing())
print(pieter.get_average())
