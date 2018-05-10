from tkinter import *


class Gui():
    def __init__(self):
        window = Tk()
        window.title("Fucking Final!")
        frame1 = Frame(window)
        frame1.pack()

        self.label = Label(frame1, text="Enter your name ")
        self.user = StringVar()
        entryName = Entry(frame1, textvariable=self.user)
        btnOK = Button(frame1, text="Submit", fg="blue", command=self.processNamebutton)

        frame2 = Frame(window)
        frame2.pack()
        self.welcomeLabel = Label(frame2, text="Welcome !")
        self.label.grid(row=1, column=1)
        entryName.grid(row=1, column=2)
        btnOK.grid(row=1, column=3)
        self.welcomeLabel.grid(row=1, column=1)

        window.mainloop()

    def processNamebutton(self):
        self.welcomeLabel["text"] = "Welcome " + self.user.get() + "!"
        print("Submit button is pressed ", self.user.get())


Gui()
