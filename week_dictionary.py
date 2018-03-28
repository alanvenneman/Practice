"""
Create a dictionary that has a number following each day of the week. Repeat this dictionary 52 times each with a random
number after each day. Days are keys, the following numbers are values. After the dictionary is constructed, we will
need to have a program that totals the numbers by day of the week based on input from the user.
"""
import random

week = 1
year = {}
while week < 53:
    year.setdefault(week, {})['Sunday'] = random.randrange(0, 99)
    year.setdefault(week, {})['Monday'] = random.randrange(0, 99)
    year.setdefault(week, {})['Tuesday'] = random.randrange(0, 99)
    year.setdefault(week, {})['Wednesday'] = random.randrange(0, 99)
    year.setdefault(week, {})['Thursday'] = random.randrange(0, 99)
    year.setdefault(week, {})['Friday'] = random.randrange(0, 99)
    year.setdefault(week, {})['Saturday'] = random.randrange(0, 99)
    week += 1

day = input('Enter a day of the week ==> ')

for key, value in year.items():
    for k, v in value.items():
        if k == day:
            print(v)
