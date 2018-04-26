# coding=utf-8
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
from BraveNewException import BraveNewException


class Shapes:
    """
    Only one property is created and it will be overridden in each subsequent class. Two methods will also be overridden
    by these classes. I set them up with the *args function because each will use a different number of arguments.
    Square: side1
    Circle: radius
    Rectangle: side1 and side2
    Triangle: side1, side2, and side3
    """
    def __init__(self, side1):
        self.__side1 = side1

    def get_area(self, *args):
        return 0

    def get_perimeter(self, *args):
        return 0


class Square(Shapes):
    """
    Inherit everything from Shapes. Override the __init__ method from shape and use it to create the side1 argument.
    The sides are passed as strings so they must be converted to floats to be used when the user inputs integers or
    floats.

    The Circle and Rectangle are similar classes.
    """
    def __init__(self, side1):
        Shapes.__init__(self, side1)

    def get_area(self, side1):
        if side1 <= 0:
            raise BraveNewException(side1)
        else:
            return side1 ** 2

    def get_perimeter(self, side1):
        if side1 <= 0:
            raise BraveNewException(side1)
        else:
            return 4 * side1


class Circle(Shapes):
    def __init__(self, side1):
        super().__init__(self, side1)
        # Shapes.__init__(self, side1)

    def get_area(self, radius):
        if radius <= 0:
            raise BraveNewException(radius)
        else:
            return round(math.pi * pow(float(radius), 2),2)

    def get_perimeter(self, radius):
        if radius <= 0:
            raise BraveNewException(radius)
        else:
            return round(2 * math.pi * float(radius), 2)


class Rectangle(Shapes):
    def __init__(self, side1, side2):
        Shapes.__init__(self, side1)
        self.__side2 = side2

    def get_area(self, side1, side2):
        if side1 <= 0 or side2 <= 0:
            raise BraveNewException(side1, side2)
        else:
            return side1 * side2

    def get_perimeter(self, side1, side2):
        if side1 <= 0 or side2 <= 0:
            raise BraveNewException(side1, side2)
        else:
            return side1 * 2 + side2 * 2


class Triangle(Shapes):
    """
    The major difference in the triangle class is the isrounded=False. I used math.sqrt and floats so that the precision
    are at the highest possible. get_perimeter is needed for get_area as described below.
    """
    def __init__(self, side1, side2, side3):
        Shapes.__init__(self, side1)
        self.__side2 = side2
        self.__side3 = side3

    def get_perimeter(self, side1, side2, side3, isrounded=False):
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise BraveNewException(side1, side2, side3)
        else:
            if isrounded is True:
                return round(side1 + side2 + side3, 2)
            else:
                return side1 + side2 + side3

    def get_area(self, side1, side2, side3):
        """
        I used an extra variable here because I wanted to try out Heron's formula. So the semiperimeter is created from
        the get_perimeter method. I left the isrounded argument set at the default - True. Now I get the full precision.
        Now the formula will be more precise before I decide to round the final answer.
        """
        if side1 <= 0 or side2 <= 0 or side3 <= 0:
            raise BraveNewException(side1, side2, side3)
        else:
            s = Triangle.get_perimeter(self, side1, side2, side3) / 2  # s is the semiperimeter
            return round(math.sqrt(s * (s - side1) * (s - side2) * (s - side3)), 2)
