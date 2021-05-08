# Importing the required libraries
from tkinter import *
from PIL import Image , ImageTk

#Creating a Tkinter instance
root = Tk()

#Title-ing the Tkinter object
root.title("Image Viewer")
root.iconbitmap('D:/Documents/ico/photo.ico')

# Creating a Tkinter image list
img1 = ImageTk.PhotoImage(Image.open('D:/Coding/tkinter/images/hehe.png'))
img2 = ImageTk.PhotoImage(Image.open('images/hehe.png'))
img3 = ImageTk.PhotoImage(Image.open('images/hehe.png'))
img4 = ImageTk.PhotoImage(Image.open('images/hehe.png'))
img5 = ImageTk.PhotoImage(Image.open('images/hehe.png'))
img_list = [img1 ,img2 ,img3 ,img4 ,img5 ]
# 
# Placing the image
img_label = Label(image=img1)
img_label.grid(row = 0, column =0 ,columnspan =3)

# Creating a function for the buttons
def forward(image_number):
	global img_label
	global forw
	global back

	img_label.grid_forget()
	img_label = Label(image=img_list[image_number - 1])
	img_label.grid(row = 0, column =0 ,columnspan =3)
def back():
	global img_label
	global forw
	global back

# Creating buttons for the gui
button_back = Button(root, text="<<", command = back).grid(row =1, column=0)
button_exit = Button(root, text="Exit Program",command = root.quit).grid(row =1 , column=1)
button_forw = Button(root, text=">>", command = lambda: forward(2)).grid(row =1, column=2)

#Disabling the resizing of the window 
root.resizable(False, False)	

# Looping the Tkinter instance
root.mainloop()