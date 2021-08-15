# Importing required libraries.
from tkinter import *
from math import *

#Creating a new Tkinter object
root = Tk() 
root.iconbitmap('D:\Documents\ico\calc.ico')
root.geometry('250x250')

#Title-ing the Tkinter object
root.title("Timer")

#Creating new Tkinter instances
button_1 = Button(root ,
    text = "Hours Decimal to n/ Hours seconds ").pack()

# Looping the Tkinter object
root.mainloop()