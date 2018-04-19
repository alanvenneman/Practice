def insertionSort(list1):
    for i in range(1, len(list1)):
        currentElement = list1[i]
        k = i - 1
        while k >= 0 and list1[k] > currentElement:
            list1[k + 1] = list1[k]
            k -= 1

        list1[k + 1] = currentElement

import random

p = 0
li = []
while p <= 10:
    li.append(random.randint(1, 500))
    p += 1
print("Before sort: ", li)

insertionSort(li)
print("After sort: ", li)
