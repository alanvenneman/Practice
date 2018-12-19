# AlanGuessMyNumber.py
# Author: Alan Venneman
# Date: December 18, 2018
# Purpose: Guess a number between 1 and 10. Uses a while loop to let the user keep guessing until they get it right.
# Inputs: guess = the guess
# Outputs: feedback if the number is higher or lower.
##################################################
print("-" * 30)

# Set the number
ANSWER = 4

# Print instructions to the user and get the user's guess
print("Guess a number between 1 and 10\nKeep guessing until you get it right.")
guess = int(raw_input("Enter a guess: "))

# Check the users' guess by using a while loop to let them keep guessing until they get the correct answer
while ANSWER <> guess:
    if ANSWER < guess:
        print("Too high!")
    else:
        print("Too low!")
    print("Guess Again!")
    guess = int(raw_input("Enter another guess: "))
print("yo dude...")
print("{} is the answer!".format(guess))

# Delete the variables
del guess, ANSWER
