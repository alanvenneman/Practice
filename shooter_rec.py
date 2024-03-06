import random

ROOM = random.randint(1, 500)
# Comment in the next line and choose 65 to test.
ROOM = 65
room_sizes = []
again = 'Y'
while again.upper() == 'Y':
    # print("Not found yet.")
    sqft = int(input("Enter square footage of room: \n"))
    room_sizes.append(sqft)
    again = input("Enter another room size? Y/N")
# maximum = max(room_sizes)


def found(target_list):
    next_room = target_list.pop()
    if next_room == ROOM:
        print("You found him.")
    else:
        if len(target_list) > 0:
            return found(target_list)
        else:
            print("No shooter.")


found(room_sizes)
