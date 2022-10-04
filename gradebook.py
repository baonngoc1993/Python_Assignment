#!/bin/python3

#Task-1
subjects = ["physics","calculus", "poetry", "history"]

#Task-2
grades = [98, 97 ,85, 88]

#Task-3
gradebook = [[subjects[0], grades[0]],[subjects[1], grades[1]], [subjects[2], grades[2]], [subjects[3], grades[3]]]

#Task-4
gradebook.append(["computer science",100])
gradebook.append(["visual arts",93])

#Task-5
gradebook[-1][1] = 98
gradebook[2].append("Pass")
gradebook[2].remove(85)

#Task-6
last_semester_gradebook = [["subject1",90]]
full_gradebook = last_semester_gradebook + gradebook

print(full_gradebook) 

