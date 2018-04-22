from tkinter import *


class Calculator:
    def __init__(self):
        root = Tk()
        root.title("Simple Calculator")

        frame2 = Frame(root)
        frame2.pack()

        self.entry_variable = IntVar()
        L1 = Label(frame2, text="Enter first operand: ")
        L1.pack(anchor=W)
        E1 = Entry(frame2, bd=3, textvariable=self.entry_variable)
        E1.pack(anchor=W)

        self.second_entry_variable = IntVar()
        L2 = Label(frame2, text="Enter second operand: ")
        L2.pack(anchor=W)
        E2 = Entry(frame2, bd=3, textvariable=self.second_entry_variable)
        E2.pack(anchor=W)

        frame1 = Frame(root)
        frame1.pack()
        label = Label(frame1, text="Choose a mathematical function by clicking the radio button.")
        label.pack()

        self.var = IntVar()
        R1 = Radiobutton(frame1, text="Addition", variable=self.var, value=1, command=self.add)
        R1.pack(anchor=W)

        R2 = Radiobutton(frame1, text="Subtraction", variable=self.var, value=2, command=self.subtract)
        R2.pack(anchor=W)

        R3 = Radiobutton(frame1, text="Multiplication", variable=self.var, value=3, command=self.multiply)
        R3.pack(anchor=W)

        R4 = Radiobutton(frame1, text="Division", variable=self.var, value=4, command=self.divide)
        R4.pack(anchor=W)

        self.label = Label(frame1)
        self.label.pack()

        root.mainloop()

    def add(self):
        try:
            calculation = int(self.entry_variable.get() + self.second_entry_variable.get())
            self.label.config(text="Calculation complete: {}".format(calculation))
        except TclError:
            self.label.config(text="Please enter an integer.")

    def subtract(self):
        try:
            calculation = int(self.entry_variable.get() - self.second_entry_variable.get())
            self.label.config(text="Calculation complete: {}".format(calculation))
        except TclError:
            self.label.config(text="Please enter an integer.")

    def multiply(self):
        try:
            calculation = int(self.entry_variable.get() * self.second_entry_variable.get())
            self.label.config(text="Calculation complete: {}".format(calculation))
        except TclError:
            self.label.config(text="Please enter an integer.")

    def divide(self):
        try:
            calculation = int(self.entry_variable.get() / self.second_entry_variable.get())
            self.label.config(text="Calculation complete: {}".format(calculation))
        except TclError:
            self.label.config(text="Please enter an integer.")
        except ZeroDivisionError:
            self.label.config(text="Second operand cannot be 0.")

Calculator()
