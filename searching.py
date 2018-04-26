from Project.Mixin import Mixin


class Searching(Mixin):
    def __init__(self):


        upperbound = eval(input("Enter an integer that will be the upper bound for the random list of numbers\n"
                                "The higher the number, the more difficult it will be to guess correctly: "))
        number = eval(input("Search for a number between 1 and {}: ".format(upperbound)))
        li = Mixin.listGeneration(self, 10, upperbound)
        print("Before search: ", li)
        print("After search:", Mixin.binarySearch(self, li, number))


Searching()
