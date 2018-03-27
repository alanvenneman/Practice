class BraveNewException(ArithmeticError):
    def __init__(self,radius):
        self.radius = radius
        super().__init__()
    #
    #
    # def zero_radius(self):
    #     if self.radius <= 0:
    #         print("You must have a radius greater than zero.")

