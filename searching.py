def binarySearch(list1, key):
    low = 0
    high = len(list1) - 1

    while high >= low:
        mid = (low + high) // 2
        if key < list1[mid]:
            high = mid - 1
        elif key == list1[mid]:
            return mid
        else:
            low = mid + 1

    return -low - 1

def listGeneration(listlength, upperbound):
    import random

    p = 0
    li = []
    while p <= listlength:
        li.append(random.randint(1, upperbound))
        p += 1
    return li

upperbound = eval(input("Enter an integer that will be the upper bound for the random list of numbers\nThe higher the"
                        "number, the more difficult it will be to guess correctly: "))
number = eval(input("Search for a number between 1 and {}: ".format(upperbound)))
li = listGeneration(10, upperbound)
print("Before search: ", li)
print("After search:", binarySearch(li, number))
