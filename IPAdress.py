import random


def ip_maker(filename):
    ip_addresses = open(filename, "w")
    counter = 0
    while counter < 100:
        num1 = random.randint(0, 200)
        num2 = random.randint(0, 200)
        num3 = random.randint(0, 200)
        num4 = random.randint(0, 200)
        address = "{}.{}.{}.{}".format(num1, num2, num3, num4)
        ip_addresses.write("{}\n".format(address))
        counter += 1
    ip_addresses.close()


ip_maker("whitelist")
ip_maker("blacklist")
