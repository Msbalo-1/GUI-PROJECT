from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.title("ms images")

img = ImageTk.PhotoImage(Image.open("cat1.jpg"))
img1 = ImageTk.PhotoImage(Image.open("bird.jpg"))
img2 = ImageTk.PhotoImage(Image.open("cat3.jpg"))
img3 = ImageTk.PhotoImage(Image.open("bick.jpg"))
img4 = ImageTk.PhotoImage(Image.open("bird.jpg"))
img5 = ImageTk.PhotoImage(Image.open("bird1.jpg"))
img6 = ImageTk.PhotoImage(Image.open("food.jpg"))
img7 = ImageTk.PhotoImage(Image.open("rood.jpg"))
img8 = ImageTk.PhotoImage(Image.open("money.jpg"))
img9 = ImageTk.PhotoImage(Image.open("cup.jpg"))

my_list = [img, img1,  img2, img3, img4, img5, img6, img7, img8, img9]

my_label = Label(root, image=img)
my_label.grid(row=0, column=0, columnspan=3)


def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=my_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == 10:
        button_forward = Button(root, text=">>", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=2)


def back(image_number):

    global my_label
    global button_forward
    global button_back
    my_label.grid_forget()
    my_label = Label(image=my_list[image_number - 1])
    button_forward = Button(root, text=">>", command=lambda: forward(image_number + 1))
    button_back = Button(root, text="<<", command=lambda: back(image_number - 1))

    if image_number == -10:
        button_back = Button(root, text="<<", state=DISABLED)

    my_label.grid(row=0, column=0, columnspan=3)
    button_forward.grid(row=1, column=2)
    button_back.grid(row=1, column=2)


button_back = Button(root, text="<<", command=lambda: back)
button = Button(root, text="exit", command=root.quit)
button_forward = Button(root, text=">>", command=lambda: forward(2))


button_back.grid(row=1, column=0,)
button.grid(row=1, column=1)
button_forward.grid(row=1, column=2)


root.mainloop()
