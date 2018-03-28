"""
Write a program to get an item's price and quantity, calculate the sub total, calculate the sales tax (8.25%), find the
total and display the result.

Extend the program to catch possible exceptions that the program may have when it is running.

Example (Arithmetic Error, Value Error, etc)
"""


def calculate_sub_total():
    while True:
        try:
            price = eval(input("How much does the item cost?\n"))
            quantity = eval(input("How many would you like?\n"))
            subtotal = price * quantity
            print("Subtotal is: {}".format(round(subtotal, 2)))
            tax = subtotal * 0.0825
            total = tax + subtotal
            print("Your total is: {}".format(round(total, 2)))
        # If a number is followed by a letter
        except SyntaxError as e:
            print("Exception: {}".format(e))
        # When a string is entered
        except NameError as n:
            print("Exception: {}".format(n))
        # If the user tries to pass a tuple
        except TypeError as t:
            print("Exception: {}".format(t))


calculate_sub_total()
