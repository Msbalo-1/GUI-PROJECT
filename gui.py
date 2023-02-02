from tkinter import *
#
# # root = Tk()
# #
# # myLabel = Label(root, text="ms is a good boy")
# # myLabel.grid()
# #
# #
# # root.mainloop()
#
#
# # root = Tk()
# #
# # myLabel1 = Label(root, text="ms is a good boy")
# # myLabel2 = Label(root, text="ms is  a programmer")
# # myLabel1.grid(row=0, column=0)
# # myLabel2.grid(row=1, column=5)
# # root.mainloop()
#
#
# root = Tk()
# entry = Entry(root, width=50, borderwidth=5)
# entry.pack()
# # entry.insert(0, "enter your name")
#
#
# def myClick():
#     hello = "Hello " + entry.get()
#     myLabel = Label(root, text=hello)
#     myLabel.pack()
#
#
# myButton = Button(root, command=myClick, text="click me", fg="red", bg="yellow")
# myButton.pack()
#
# root.mainloop()
#
#
# #  # pack
# # root = Tk()
# # # creating a label widget
# # myLabel = Label(root, text="Hello word!")
# # # making it show on the screen
# # myLabel.pack()
# # # calling the loop
# # root.mainloop()
#
#
#
# # grid
# # root = Tk()
# # # creating a label widget
# # myLabel1 = Label(root, text="Hello word!")
# # myLabel2 = Label(root, text="my name is ms")
# # # making it show on the screen
# # myLabel1.grid(row=0, column=0)
# # myLabel2.grid(row=1, column=5)
# # # calling the loop
# # root.mainloop()
#
# # # button
# # root = Tk()
# # entry = Entry(root, width=50, borderwidth=5)
# # entry.pack()
# # entry.insert(0, "enter your name")
# #
# #
# # def myClick():
# #     hello = "Hello " + entry.get()
# #     myLabel = Label(root, text=hello)
# #     myLabel.pack()
# #
# #
# # button = Button(root, text="click me", command=myClick, fg="red", bg="yellow", )
# # button.pack()




# import tkinter and every thing in it with *
from tkinter import *


root = Tk()
root.title("ms calculator")

entry = Entry(root, width=35, borderwidth=5)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)


def button_click(number):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current) + str(number))


def button_clear():
    entry.delete(0, END)


def button_add():
    first_number = entry.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    entry.delete(0, END)


def button_subtract():
    first_number = entry.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    entry.delete(0, END)


def button_multiply():
    first_number = entry.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    entry.delete(0, END)


def button_divide():
    first_number = entry.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    entry.delete(0, END)


def button_equal():
    second_number = entry.get()
    entry.delete(0, END)
    if math == "addition":
        entry.insert(0, f_num +  int(second_number))

    if math == "subtraction":
        entry.insert(0, f_num - int(second_number))

    if math == "multiplication":
        entry.insert(0, f_num * int(second_number))

    if math == "division":
        entry.insert(0, f_num / int(second_number))

button_1 = Button(root, text="1", command=lambda :  button_click(1), padx=40, pady=20)
button_2 = Button(root, text="2", command=lambda :  button_click(2), padx=40, pady=20)
button_3 = Button(root, text="3", command=lambda :  button_click(3), padx=40, pady=20)
button_4 = Button(root, text="4", command=lambda :  button_click(4), padx=40, pady=20)
button_5 = Button(root, text="5", command=lambda :  button_click(5), padx=40, pady=20)
button_6 = Button(root, text="6", command=lambda :  button_click(6), padx=40, pady=20)
button_7 = Button(root, text="7", command=lambda :  button_click(7), padx=40, pady=20)
button_8 = Button(root, text="8", command=lambda :  button_click(8), padx=40, pady=20)
button_9 = Button(root, text="9", command=lambda :  button_click(9), padx=40, pady=20)
button_0 = Button(root, text="0", command=lambda :  button_click(0), padx=40, pady=20)
button_add= Button(root, text="+", command= button_add,  padx=39, pady=20)
button_equal = Button(root, text="=", command= button_equal, padx=91, pady=20)
button_clear = Button(root, text="clear", command= button_clear, padx=79, pady=20)
button_subtract= Button(root, text="-", command= button_subtract,  padx=41, pady=20)
button_multiply= Button(root, text="*", command= button_multiply,  padx=41, pady=20)
button_divide= Button(root, text="/", command= button_divide,  padx=41, pady=20)


button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)

button_0.grid(row=4, column=0,)
button_add.grid(row=5, column=0, )
button_clear.grid(row=5, column=1, columnspan=2)
button_equal.grid(row=4, column=1, columnspan=2)
button_multiply.grid(row=6, column=0)
button_divide.grid(row=6, column=1)
button_subtract.grid(row=6, column=2)


button = Button(root, text="my click", bg="red", fg="green")
# button.grid()


root.mainloop()
