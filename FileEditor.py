"""
This is a line for line transcription of an example from Introduction to Programming Using Paython by Y. Liang

I want to practice using the tkinter library and later on add some error handling.
"""

from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import asksaveasfilename


class FileEditor:
    def __init__(self):
        window = Tk()
        window.title("Simple Text Editor")
        menubar = Menu(window)
        window.config(menu = menubar)  # displays the menu bar

        # Create pull-down menu and add it to the menu bar
        operationMenu = Menu(menubar, tearoff = 0)
        menubar.add_cascade(label = "File", menu = operationMenu)
        operationMenu.add_command(label = "Open",
                                  command = self.openFile)
        operationMenu.add_command(label = "Save",
                                  command = self.saveFile)

        # Add a tool bar frame
        frameO = Frame(window)  # Create and add a frame to window
        frameO.grid(row = 1, column = 1, sticky = W)

        # Create images
        openImage = PhotoImage(file = "image/open.gif")
        saveImage = PhotoImage(file = "image/save.gif")

        Button(frameO, image = openImage, command = self.openFile).grid(row = 1, column = 1, sticky = W)
        Button(frameO, image = saveImage, command = self.saveFile).grid(row = 1, column = 2)

        frame1 = Frame(window)  # Hold editor pane
        frame1.grid(row = 2, column = 1)

        scrollbar = Scrollbar(frame1)
        scrollbar.pack(side = RIGHT, fill = Y)
        self.text = Text(frame1, width = 40, height = 20, wrap = WORD, yscrollcommand = scrollbar.set)
        self.text.pack()
        scrollbar.config(command = self.text.yview)
        window.mainloop()

    def openFile(self):
        try:
            filenameforReading = askopenfilename()
            infile = open(filenameforReading, "r")
            self.text.insert(END, infile.read())  # Read all from file
            infile.close()
        except FileNotFoundError as f:
            print("Missing file:",  f)
        # finally:
        #     infile.close()

    def saveFile(self):
        try:
            filenameforWriting = asksaveasfilename()
            outfile = open(filenameforWriting, "w")
            outfile.write(self.text.get(1.0, END))
            outfile.close()
        except FileNotFoundError as f:
            print("Missing file:", f)
        # finally:
        #     outfile.close()

FileEditor()
