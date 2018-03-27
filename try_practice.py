flag = 'Y'
while flag == 'Y':
    homework = open("division.txt", "w")
    homework.write("Here's my homework.")
    x = input(float("Enter a number that will be divided: \n"))
    y = input(float("Enter a number that will divide: \n"))
    z = x / y
    homework.write(z)
    homework.close()
