from Shapes import *
# Set up the square Class
square_side = input("Enter the measurement for side one of a square: ")
square = Square(side1=square_side)
squarea = square.get_area(square_side)
squaremiter = square.get_perimeter(square_side)
# print the area and perimeter for the square
print("The area of your square is {} and the perimeter is {}.\n".format(squarea, squaremiter))
# Set up the circle class
circle_radius = input("Enter the measurement for the radius of a circle: ")
circle = Circle(side1=circle_radius)
circlera = circle.get_area(circle_radius)
circlimeter = circle.get_perimeter(circle_radius)
# print the area and perimeter for the circle
print("The area of your circle is {} and the perimeter is {}.\n".format(circlera, circlimeter))
# set up the rectangle class
rectangle_side = input("Enter the two sides for a rectangle.\nSide one: ")
rectangle_side2 = input("And side two: ")
rectangle = Rectangle(rectangle_side, rectangle_side2)
rectanglerea = rectangle.get_area(rectangle_side, rectangle_side2)
rectanglimeter = rectangle.get_perimeter(rectangle_side, rectangle_side2)
# print the area and perimeter for the rectangle
print("The area is {} and the perimeter is {}.\n".format(rectanglerea, rectanglimeter))
# set the triangle class
triangle_side = input("Enter side one of a triangle: ")
triangle_side2 = input("Now enter side two of a triangle: ")
triangle_side3 = input("You figured this out yet? Provide the third side: ")
triangle = Triangle(triangle_side, triangle_side2, triangle_side3)
# Set the round() function to True
trianglemeter = triangle.get_perimeter(triangle_side, triangle_side2, triangle_side3, True)
trianglera = triangle.get_area(triangle_side, triangle_side2, triangle_side3)
# print the area and perimeter for the triangle
print("Here's your triangle's area: {} and here's the perimeter: {}.".format(trianglera, trianglemeter))
