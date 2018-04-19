from tkinter import *


class Calculator():
    def __init__(self):
        window = Tk()
        window.title("Calculator")
        frame1 = Frame(window)
        frame1.pack()

    plusButton = Button(frame1, text="+", )