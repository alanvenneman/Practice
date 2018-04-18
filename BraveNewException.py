class BraveNewException(ArithmeticError):
    def __init__(self, *args):
        super().__init__()
        self.side = args

    # def zero_radius(self):
    #     if self.radius <= 0:
    #         print("You must have a radius greater than zero.")
