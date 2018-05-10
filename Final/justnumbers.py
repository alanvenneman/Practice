def just_numbers(number):
    list = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    if len(list) == number:
        return list[number] #, just_numbers(number - 1)
    else:
        list.pop()
        return list[0]
        range(list, 11)


just_numbers(10)
