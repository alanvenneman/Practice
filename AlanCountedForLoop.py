# AlanCountedForLoop.py
# Author: Alan Venneman
# Date: December 18, 2018
# Purpose: Prompts for the starting and ending number and loops through them using a counted for loop.
# Inputs: start = starting number
# end = ending number
# Outputs: None
##################################################
print("-" * 30)

# prompt for start and end numbers
start_num = raw_input("Enter starting number: ")
end_num = raw_input("Enter ending number: ")

# convert string inputs to numbers
start_int = int(start_num)
end_int = int(end_num)
print(type(start_int))
print(type(end_int))

# counted for loop and print values
for i in range (start_int, end_int):
    print i
# delete the variables
del start_num, end_num, start_int, end_int, i
