from tkinter import *


class gui:
    window = Tk()

    btnOK = Button(window, text="Submit", fg="blue", command=self.processNamebutton("Alan"))
    user = StringVar()
    entry = Entry(window, textvariable=f"Welcome {user}")

    btnOK.pack()
    entry.pack()

    window.mainloop()


    def processNamebutton(self):
        print("Welcome ", self.user.get())
