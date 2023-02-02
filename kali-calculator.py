from tkinter import *

root = Tk()
root.title("kali-calculator")


entry = Entry(root, width=65, borderwidth=1, bg="black", fg="white", )
entry.grid(row=0, column=0, padx=10, pady=10, columnspan=6)


def click(num):
    current = entry.get()
    entry.delete(0, END)
    entry.insert(0, str(current ) + str(num))


def clear():
    entry.delete(0, END)


def add():
    global number
    global function
    number = int(entry.get())
    function = "plus"
    entry.delete(0, END)


def minus():
    global number
    global function
    number = int(entry.get())
    function = "minus"
    entry.delete(0, END)


def times():
    global number
    global function
    number = int(entry.get())
    function = "times"
    entry.delete(0, END)


def divide():
    global number
    global function
    number = int(entry.get())
    function = "divide"
    entry.delete(0, END)


def percent():
    global number
    global function
    number = int(entry.get())
    function = "percent"
    entry.delete(0, END)


def equal():
    second_number = entry.get()
    entry.delete(0, END)
    if function == "plus":
        entry.insert(0, number + int(second_number))
    elif function == "minus":
        entry.insert(0, number - int(second_number))
    elif function == "times":
        entry.insert(0, number * int(second_number))
    elif function == "divide":
        entry.insert(0, number / int(second_number))
    elif function == "percent":
        entry.insert(0, number % int(second_number))











b_1 = Button(root, text="1",  padx=40, pady=5, command=lambda: click(1), bg="black", fg="white")
b_2 = Button(root, text="2",  padx=40, pady=5, command=lambda: click(2), bg="black", fg="white")
b_3 = Button(root, text="3",  padx=40, pady=5, command=lambda: click(3), bg="black", fg="white" )
b_4 = Button(root, text="4",  padx=40, pady=5, command=lambda : click(4), bg="black", fg="white" )
b_5 = Button(root, text="5",  padx=40, pady=5, command=lambda : click(5), bg="black", fg="white" )
b_6 = Button(root, text="6",  padx=40, pady=5, command=lambda : click(6), bg="black", fg="white" )
b_7 = Button(root, text="7",  padx=40, pady=5, command=lambda : click(7), bg="black", fg="white" )
b_8 = Button(root, text="8",  padx=40, pady=5, command=lambda : click(8), bg="black", fg="white" )
b_9 = Button(root, text="9",  padx=40, pady=5, command=lambda : click(9), bg="black", fg="white" )
b_0 = Button(root, text="0",  padx=40, pady=5, command=lambda: click(0), bg="black", fg="white" )
b_add = Button(root, text="+",  padx=38, pady=5, command=add, bg="black", fg="white")
b_minus = Button(root, text="-",  padx=40, pady=5, command= minus, bg="black", fg="white")
b_divide = Button(root, text="/",  padx=40, pady=5, command= divide, bg="black", fg="white")
b_times = Button(root, text="*",  padx=39, pady=5, command= times , bg="black", fg="white")
b_equal = Button(root, text="=",  padx=71, pady=40, command=equal, bg="black", fg="white")
b_clear = Button(root, text="C",  padx=25, pady=5, command= clear, bg="black", fg="white")
b_cancel = Button(root, text="exit",  padx=30, pady=5, command= root.quit, bg="black", fg="white" )
b_dot = Button(root, text=".",  padx=41, pady=5, command=lambda: click(".") , bg="black", fg="white")
b_percent = Button(root, text="%",  padx=38, pady=5, command= percent, bg="black", fg="white")

b_1.grid(row=3, column=0)
b_2.grid(row=3, column=1)
b_3.grid(row=3, column=2)

b_4.grid(row=2, column=0)
b_5.grid(row=2, column=1)
b_6.grid(row=2, column=2)

b_7.grid(row=1, column=0)
b_8.grid(row=1, column=1)
b_9.grid(row=1, column=2)

b_0.grid(row=4, column=0)
b_add.grid(row=4, column=3)
b_minus.grid(row=3, column=3)


b_divide.grid(row=1, column=3)
b_times.grid(row=2, column=3)
b_equal.grid(row=2, column=4, columnspan=2, rowspan=3)
b_dot.grid(row=4, column=1)
b_percent.grid(row=4, column=2)
b_cancel.grid(row=1, column=4)
b_clear.grid(row=1, column=5, )



# b_1.grid(row=, column=)
# b_1.grid(row=, column=)
# b_1.grid(row=, column=)





root.mainloop()
