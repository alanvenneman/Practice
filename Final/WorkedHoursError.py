class WorkedHoursError(ArithmeticError):
    def __init__(self, hrs):
        super().__init__()
        self.hours = hrs
