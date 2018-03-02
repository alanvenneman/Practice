""""
Two dimensional list of students' marks for three different classrooms. Find the average grade in each class.

The array will need to be read using a nested for loop.
"""
import random


classroom = []
for i in range(3):
    classroom.append([])
    for j in range(10):
        classroom[i].append(random.randint(0, 100))

for i in range(len(classroom)):
    total = 0
    for j in range(len(classroom[i])):
        total += classroom[i][j]
    print("The Average for each classroom is: ", total/10)
