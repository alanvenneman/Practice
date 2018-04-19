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

    return low

import random

p = 0
li = []
while p <= 10:
    li.append(random.randint(1, 15))
    p += 1
print("Before search: ", li)

results = binarySearch(li, 3)
print(results)
