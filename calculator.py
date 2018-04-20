from tkinter import *


class Calculator():
    def __init__(self):
        window = Tk()
        window.title("Simple Calculator")

        Label(window, text="Left Operand").grid(row=1, column=1, sticky=W)
        Label(window, text="Right Operand").grid(row=1, column=2, sticky=W)
        Label(window, text="Calculation").grid(row=4, column=1, sticky=W)

        frame1 = Frame(window)
        frame1.pack()
        Label(frame1, text="Operation")

        self.left_operand = DoubleVar()
        Entry(frame1, textvariable=self.left_operand, justify=RIGHT).grid(row=1, column=2)
        self.right_operand = DoubleVar()
        Entry(frame1, textvariable=self.right_operand, justify=RIGHT).grid(row=2, column=2)
        self.v1 = DoubleVar()
        addition = Radiobutton(frame1, text="+", variable=self.v1, value=1, command=self.calculate(self.right_operand, self.left_operand)).grid(row=3, column=2)
        subtraction = Radiobutton(frame1, text="-", variable=self.v1, value=2, command=self.calculate(self.right_operand, self.left_operand)).grid(row=3, column=3)
        multiplication = Radiobutton(frame1, text="*", variable=self.v1, value=3, command=self.calculate(self.right_operand, self.left_operand)).grid(row=3, column=4)
        division = Radiobutton(frame1, text="/", variable=self.v1, value=4, command=self.calculate(self.right_operand, self.left_operand)).grid(row=3, column=5)


        self.calculation = StringVar()
        lbl_calculation = Label(window, textvariable=self.calculation).grid(row=4, column=2, sticky=E)

        window.mainloop()

    def calculate(self, right_operand, left_operand):
        if self.v1.get() == 1:
            return right_operand + left_operand
        elif self.v1.get() == 2:
            return left_operand - right_operand
        elif self.v1.get() == 3:
            return left_operand * right_operand
        else:
            return left_operand / right_operand

Calculator()
