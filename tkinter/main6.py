# Importing required libraries.
from tkinter import *
from PIL import ImageTk , Image

#Creating a new Tkinter instance
root = Tk() 
root.iconbitmap('D:\Documents\ico\calc.ico')

#Title-ing the Tkinter object
root.title("main6")

#Creating a images Tkinter instance
#Creating a images Tkinter instance
my_img = ImageTk.PhotoImage(Image.open("hehe.png"))
my_label = Label(image=my_img)
my_label.pack()

#Creating new Tkinter buttons
button_1 = Button(root , text = "exit" , command=root.quit).pack()

# Looping the Tkinter instance
root.mainloop()