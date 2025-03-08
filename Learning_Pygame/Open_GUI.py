# https://www.youtube.com/watch?v=q8WDvrjPt0M&t=159s

from tkinter import *
from tkinter import filedialog

def openFile():
    filepath = filedialog.askopenfilename()
    file = open(filepath, 'r')
    print(file.read())
    file.close()

Window = Tk()
button = Button(text="Open", command=openFile)
button.pack()
Window.mainloop()