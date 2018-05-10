def just_numbers(number):
    number_list = []
    for n in range(0, number + 1):
        number_list.append(number)
        print(number_list)
        number -= 1

print(just_numbers(10))
