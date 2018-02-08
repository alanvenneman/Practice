"""
Create a shape Class with one data member called side1 and two class methods called getArea and getPerimeter.
They are empty methods or abstract methods. You can write empty methods as

def  getArea(self):
    pass

Or

def getArea(self):
    …

Or

def getArea(self):
    return

Or

def getArea(self):
    return 0

I have added a sample in the Inheritance Module for Shape.

Create a Class called Square as a subclass of Shape and implement the data member and methods side1, getArea and
getPerimeter.

Create another Class called Rectangle as a subclass of Shape and implement Shape.side1 and Rectangle class’s side2.
Write the methods getArea and getPerimeter for Rectangle class.

Create another class called Triangle as a subclass of Shape and implement Shape.side1 and Triangle’s class’s side2 and
side3. Write the methods getArea and getPerimeter for Triangle class.

Please keep the scope of this assignment as simple as possible and learn the inheritance. That is the objective. Once
we get all the concepts, we can expand by adding more functionalities.
"""
import math


class Shapes:
    def __init__(self, side1):
        self.__side1 = side1

    def get_area(self, *args):
        return 0

    def get_perimeter(self, *args):
        return 0


class Square(Shapes):
    def __init__(self, side1):
        Shapes.__init__(self, side1)

    def get_area(self, side1):
        return float(side1) ** 2

    def get_perimeter(self, side1):
        return 4 * float(side1)


class Circle(Shapes):
    def __init__(self, side1):
        Shapes.__init__(self, side1)

    def get_area(self, radius):
        return round(math.pi * pow(float(radius), 2), 2)

    def get_perimeter(self, radius):
        return round(2 * math.pi * float(radius), 2)


class Rectangle(Shapes):
    def __init__(self, side1, side2):
        Shapes.__init__(self, side1)
        self.__side2 = side2

    def get_area(self, side1, side2):
        return float(side1) * float(side2)

    def get_perimeter(self, side1, side2):
        return float(side1) * 2 + float(side2) * 2


class Triangle(Shapes):
    def __init__(self, side1, side2, side3):
        Shapes.__init__(self, side1)
        self.__side2 = side2
        self.__side3 = side3

    def get_perimeter(self, side1, side2, side3, isrounded=False):
        if isrounded == True:
            return round(float(side1) + float(side2) + float(side3), 2)
        else:
            return float(side1) + float(side2) + float(side3)

    def get_area(self, side1, side2, side3):
        semiperimeter = Triangle.get_perimeter(self, side1, side2, side3) / 2
        return round(math.sqrt(semiperimeter * (semiperimeter - float(side1)) * semiperimeter * (semiperimeter - float(side2)) * semiperimeter * (semiperimeter - float(side3))), 2)
