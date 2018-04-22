# from tkinter import *
#
#
# class Calculator():
#     def __init__(self):
#         window = Tk()
#         window.title("Simple Calculator")
#
#         frame1 = Frame(window)
#         frame1.pack()
#         instructions = Label(frame1, text="Enter two numbers: ") #.grid(row=1, column=1)
#         instructions.pack()
#
#         frame2 = Frame(window)
#         # frame1.pack()
#         Label(frame2, text="Left Operand").grid(row=1, column=1)
#         self.left_operand = DoubleVar()
#         Entry(frame2, textvariable=self.left_operand).grid(row=1, column=2)
#         Label(frame2, text="Right Operand").grid(row=1, column=3)
#         self.right_operand = DoubleVar()
#         Entry(frame2, textvariable=self.right_operand).grid(row=1, column=4)
#         Button(frame2, text="Select Operation", command=self.processButton).grid(row=2, column=1)
#         self.v1 = DoubleVar()
#         Radiobutton(frame2, text="+", variable=self.v1, value=1, command=self.calculate(self.right_operand, self.left_operand)).grid(row=2, column=2)
#         Radiobutton(frame2, text="-", variable=self.v1, value=2, command=self.calculate(self.right_operand, self.left_operand)).grid(row=2, column=3)
#         Radiobutton(frame2, text="*", variable=self.v1, value=3, command=self.calculate(self.right_operand, self.left_operand)).grid(row=2, column=4)
#         Radiobutton(frame2, text="/", variable=self.v1, value=4, command=self.calculate(self.right_operand, self.left_operand)).grid(row=2, column=5)
#
#
#         frame3 = Frame(window)
#         Label(frame3, text="Calculation").grid(row=1, column=1)
#         self.calculation = StringVar()
#         lbl_calculation = Label(frame3, textvariable=self.calculation).grid(row=1, column=2)
#
#         window.mainloop()
#
#     def calculate(self, right_operand, left_operand):
#         if self.v1.get() == 1:
#             # return right_operand + left_operand
#             print("addition")
#         elif self.v1.get() == 2:
#             # return left_operand - right_operand
#             print("subtraction")
#         elif self.v1.get() == 3:
#             # return left_operand * right_operand
#             print("multiplication")
#         elif self.v1.get() == 4:
#             print("division")
#             # return left_operand / right_operand
#
#     def processButton(self):
#         self.v1[]
#
# Calculator()


# from tkinter import *
# # import time
#
# class App:
#     def __init__(self, master):
#         w = Label(master, text="1. Anxiety, nervousness, worry or fear")
#         w.pack()
#
#         v = IntVar()
#         Radiobutton(master, text="0 for not at all", variable=v, value=1).pack(side=TOP, anchor="w")
#         Radiobutton(master, text="1 for somewhat", variable=v, value=2).pack(side=TOP, anchor="w")
#         Radiobutton(master, text="2 for moderatly", variable=v, value=3).pack(side=TOP, anchor="w")
#         Radiobutton(master, text="3 for a lot", variable=v, value=4).pack(side=TOP, anchor="w")
#
#         self.button = Button(master, text="BACK", fg="red", command=self.button6)
#         self.button.pack(side=BOTTOM)
#         self.button = Button(master, text="NEXT", fg="red", command=self.button5)
#         self.button.pack(side=BOTTOM)
#
#     def button6(self):
#         print ("Sam is awesome!GAJONGA")
#
#     def button5(self):
#         print ("PYTHON FOR THE WIN! GIAN SAYS PYTHON = FILTHY")

# master = k()
# app = App(master)
# master.mainloop()


# from tkinter import *
#
# root = Tk()
# frame = Frame(root)
# frame.pack()
#
# bottomframe = Frame(root)
# bottomframe.pack( side = BOTTOM )
#
# redbutton = Button(frame, text="Red", fg="red")
# redbutton.pack( side = LEFT)
#
# greenbutton = Button(frame, text="Brown", fg="brown")
# greenbutton.pack( side = LEFT )
#
# bluebutton = Button(frame, text="Blue", fg="blue")
# bluebutton.pack( side = LEFT )
#
# blackbutton = Button(bottomframe, text="Black", fg="black")
# blackbutton.pack( side = BOTTOM)
#
# root.mainloop()


# from tkinter import *
#
# top = Tk()
# L1 = Label(top, text="User Name")
# L1.pack( side = LEFT)
# E1 = Entry(top, bd =5)
# E1.pack(side = RIGHT)
#
# top.mainloop()

from tkinter import *


root = Tk()
root.title("MyApp")

myvar = StringVar()

def mywarWritten(*args):
    print ("mywarWritten",myvar.get())

myvar.trace("w", mywarWritten)

label = Label(root, textvariable=myvar)
label.pack()

text_entry = Entry(root, textvariable=myvar)
text_entry.pack()

root.mainloop()
