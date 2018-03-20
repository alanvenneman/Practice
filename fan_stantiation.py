from Fan import Fan

blue_fan = Fan()
ask_color = input("Please select a color for your fan\n"
                  "1 - blue\n2 - red\n3 - black\n")
if ask_color == 1:
    Fan.set_color(blue_fan, 'blue')
elif ask_color == 2:
    Fan.set_color(blue_fan, 'red')
elif ask_color == 3:
    Fan.set_color(blue_fan, 'black')
else:
    print("Fail.")

ask_speed = input("Please select the speed of the fan\n"
                       "1 - Slow\n2 - Medium\n3 - Fast\n")

if ask_speed == 1:
    Fan.set_speed(blue_fan, 'slow')
elif ask_speed == 2:
    Fan.set_speed(blue_fan, 'medium')
elif ask_speed == 3:
    Fan.set_speed(blue_fan, 'fast')
else:
    print("You suck at life.")

ask_on_or_off = input("Is the fan on or off?\n"
                      "1 - True\n2 - False\n")

if ask_on_or_off == 1:
    Fan.set_on(blue_fan, True)
elif ask_on_or_off == 2:
    Fan.set_on(blue_fan, False)
else:
    print("(-__-)")

ask_radius = input("What is the radius of the fan?\n"
                        "1 - 1 foot\n2 - 1.25 foot\n3 - 1.5 foot\n")

if ask_radius == 1:
    Fan.set_radius(blue_fan, 1.0)
elif ask_radius == 2:
    Fan.set_radius(blue_fan, 1.25)
elif ask_radius == 3:
    Fan.set_radius(blue_fan, 1.5)
else:
    print("No. Just no.")

print("Your {} fan has a {} foot radius, it's set to {}, and it's turned {}.".format(Fan.get_color(blue_fan),
                                                                                     Fan.get_radius(blue_fan),
                                                                                     Fan.get_speed(blue_fan),
                                                                                     Fan.get_on(blue_fan)))
