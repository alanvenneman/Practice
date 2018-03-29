def volume_box(side1, side2, side3):
    if side1 == 1 or side2 == 1 or side3 == 1:
        return 1
    else:
        print("Side 1: {}, Side 2: {} Side 3: {} ".format(side1, side2, side3))
        vol = side1 * side2 * side3
        print("Volumne: ", vol)
        return vol + volume_box(side1 - 1, side2 - 1, side3 - 1)

try:
    x = int(input("Enter the measurement: \n"))
    y = int(input("Enter the second measurement: \n"))
    z = int(input("Enter the third measurement: \n"))
    print("the total volume of all boxes", volume_box(x, y , z))
except ValueError as v:
    print("Please use an integer. Exception: ", v)
