from Shapes import *

square_side = input("Enter the measurement for side one of a square: ")
square = Square(side1=square_side)
squarea = square.get_area(square_side)
squaremiter = square.get_perimeter(square_side)

print("The damn area is {} and the damn perimeter is {}.\n".format(squarea, squaremiter))

circle_radius = input("Enter the measurement for the radius of a circle: ")
circle = Circle(side1=circle_radius)
circlera = circle.get_area(circle_radius)
circlimeter = circle.get_perimeter(circle_radius)

print("The muthafuckin' area is {} and the muthafuckin' perimeter is {}.\n".format(circlera, circlimeter))

rectangle_side = input("Enter the two bitchin' sides for a rectangle!\n Side one: ")
rectangle_side2 = input("And side two: ")
rectangle = Rectangle(rectangle_side, rectangle_side2)
rectanglerea = rectangle.get_area(rectangle_side, rectangle_side2)
rectanglimeter = rectangle.get_perimeter(rectangle_side, rectangle_side2)

print("The bitchin area is {} and the bitchin' perimeter is {}.\n".format(rectanglerea, rectanglimeter))

triangle_side = input("Gimme yo damn triangle side one! ")
triangle_side2 = input("Now gimme yo damn triangle side two! ")
triangle_side3 = input("You figured this out yet? Gimme side three! ")
triangle = Triangle(triangle_side, triangle_side2, triangle_side3)
trianglemeter = triangle.get_perimeter(triangle_side, triangle_side2, triangle_side3, True)
trianglera = triangle.get_area(triangle_side, triangle_side2, triangle_side3)

print("Was that so hard? Here's yo area: {} and here's yo perimeter: {}. Now get the fuck outta here!".format(trianglera, trianglemeter))
