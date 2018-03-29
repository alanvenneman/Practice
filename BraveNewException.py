class BraveNewException(RuntimeError):
    def __init__(self, radius):
        super().__init__()
        self.radius = radius

    # def zero_radius(self):
    #     if self.radius <= 0:
    #         print("You must have a radius greater than zero.")
