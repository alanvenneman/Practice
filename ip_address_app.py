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

ip_entry = input("Please enter the IP address you wish to browse.\n /"
                 "Use this format: ###.###.###.###\n")
read_whitelist = open("whitelist", "r")
read_blacklist = open("blacklist", "r")
black = 0
white = 0


b_counter = 0
while b_counter <= 100:
    check_b = read_blacklist.readline()
    if ip_entry == check_b.strip("\n"):
        black = 1
        break
    b_counter += 1
read_blacklist.close()

counter = 0
while counter <= 100:
    check_w = read_whitelist.readline()
    if ip_entry == check_w.strip("\n"):
        white = 1
        break
    counter += 1
read_whitelist.close()

if black == 1:
    print("Harmful IP address - access denied.")
elif white == 1:
    print("Whitelisted address. Happy Browsing")
else:
    new_list = open("check_ip", "w")
    new_list.write(ip_entry)
    print("You are temporarily given access to this site.\nYour browsing will be monitored.")
    new_list.close()
