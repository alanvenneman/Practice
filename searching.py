<<<<<<< HEAD
from module.Mixin import Mixin
=======
from Project.Mixin import Mixin
>>>>>>> 019139d9c4330293b87053aab7a29cc3cdfa3e20


class Searching(Mixin):
    def __init__(self):
<<<<<<< HEAD
=======
        Mixin.__init__(self)
>>>>>>> 019139d9c4330293b87053aab7a29cc3cdfa3e20


        upperbound = eval(input("Enter an integer that will be the upper bound for the random list of numbers\n"
                                "The higher the number, the more difficult it will be to guess correctly: "))
        number = eval(input("Search for a number between 1 and {}: ".format(upperbound)))
        li = Mixin.listGeneration(self, 10, upperbound)
        print("Before search: ", li)
        print("After search:", Mixin.binarySearch(self, li, number))


Searching()
