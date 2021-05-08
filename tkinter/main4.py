# Importing Tkinter 
from tkinter import *

#Creating a new Tkinter instance
root = Tk()

#Title-ing the Tkinter object
root.title("Calculator")

#Creating a input Tkinter instance
box = Entry(root , width =  30, borderwidth = 5)
box.pack()
#creating a function
def function():
    my_label=Label(root , text = "Hello " + box.get())
    my_label.pack()
    
#Creating new Tkinter buttons
button_1 = Button(root , text = "Enter" , command=function).pack()

# Looping the Tkinter instance
root.mainloop()