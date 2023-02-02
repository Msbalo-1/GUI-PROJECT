# import tkinter and every thing in it with *
from tkinter import *


 # pack
root = Tk()
# creating a label widget
myLabel = Label(root, text="Hello word!")
# making it show on the screen
myLabel.pack()
# calling the loop
root.mainloop()



# # grid
# root = Tk()
# # creating a label widget
# myLabel1 = Label(root, text="Hello word!")
# myLabel2 = Label(root, text="my name is ms")
# # making it show on the screen
# myLabel1.grid(row=0, column=0)
# myLabel2.grid(row=1, column=5)
# # calling the loop
# root.mainloop()

# button
root = Tk()
entry = Entry(root, width=50, borderwidth=5)
entry.pack()
entry.insert(0, "enter your name")


def myClick():
    hello = "Hello " + entry.get()
    myLabel = Label(root, text=hello)
    myLabel.pack()


button = Button(root, text="click me", command=myClick, fg="red", bg="yellow", )
button.pack()

root.mainloop()