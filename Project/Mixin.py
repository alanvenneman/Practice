class Mixin(object):
    pass


    def binarySearch(self, list1, key):
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

    def listGeneration(self, listlength, upperbound):
        import random

        p = 0
        li = []
        while p <= listlength:
            li.append(random.randint(1, upperbound))
            p += 1
        return li
