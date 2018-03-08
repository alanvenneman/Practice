TUPLE = (1)

repeats = 0
number = 0
count = 0

while len(TUPLE) > count:
    if repeats < TUPLE.count(TUPLE[count]):
        if TUPLE.count(TUPLE[count]) > 1:
            repeats = TUPLE.count(TUPLE[count])
            number = str(TUPLE[count])
    count += 1
if repeats > 0:
    print("The number {} is repeated {} times.".format(number, repeats))
else:
    print("There are no repeats in this tuple.")

### SECOND SCENARIO ###
repeats = 0
count = 0

while len(TUPLE) >= count:
    if len(TUPLE) >= 1:
        if TUPLE.count(TUPLE[0]) > 1:
            repeats = TUPLE.count(TUPLE[0])
            print("The first value repeats {} times.".format(repeats))
            break
        else:
            print("The first number, {} does not repeat in this tuple.".format(TUPLE[0]))
            break
    else:
        print("This tuple is empty.")
    count += 1
