class Fan:
    def __init__(self):
        self.speed = 0
        self.on = bool
        self.radius = 0.0
        self.color = ''

    def set_speed(self, speed):
        self.speed = speed

    def get_speed(self):
        return self.speed

    def set_on(self, false):
        self.on = false

    def get_on(self):
        if self.on is False:
            return "off"
        else:
            return "on"

    def set_radius(self, radius):
        self.radius = radius

    def get_radius(self):
        return self.radius

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
