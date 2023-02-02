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


root.mainloop()