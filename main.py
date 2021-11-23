import tkinter

import object_tracking as ot
from tkinter import *
from tkinter import filedialog

filepath = "null"


def setPathText():
    global currentPathText, filepath
    currentPathText.config(text="Current path: " + filepath)


def startObjectTracking():
    global filepath
    if filepath != "null":
        try:
            ot.object_tracking(filepath)
        except:
            currentPathText.config(text="Wrong file selected")
    else:
        currentPathText.config(text="Please select a file")


def openFile():
    global filepath
    filepath = filedialog.askopenfilename(initialdir="C:\\Users\\Robert\\PycharmProjects\\ObjectTracking",
                                          filetypes=(("videos", "*.mp4"),
                                                     ("all files", "*.*")))
    setPathText()


root = Tk()
root.minsize(1200, 400)

titleLabel = Label(root, text="OBJECT TRACKING", font='Times_New_Roman 25 bold')
titleLabel.pack()

chooseFileButton = Button(root, text="Choose file", font="Times_New_Roman 18 bold", command=openFile).place(x=130,
                                                                                                            y=250)
runObjectTracking = Button(root, text="Run Object Tracking", font="Times_New_Roman 18 bold",
                           command=startObjectTracking).place(x=470, y=250)

closeAppButton = Button(root, text="Close app", font="Times_New_Roman 18 bold", command=root.destroy).place(
    x=900, y=250)

currentPathText = Label(root, text="File path: " + filepath, font="Helvetica 18 bold")

currentPathText.place(x=100, y=125)

infoLabelText = Label(root, text=" Press ESC to close the player ").pack(side=tkinter.BOTTOM)

root.mainloop()
