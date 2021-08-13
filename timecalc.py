# Importing required libraries.
from tkinter import *

#Creating a new Tkinter instance
root = Tk()
root.iconbitmap('D:\Documents\ico\calc.ico')
# root.geometry('500x500')

#Title-ing the Tkinter object
root.title("Time Calculator")

head = Label(root,
    text = "Time Calculator")

time_input = Entry(root, 
    width = 30, 
    borderwidth = 3)

# Configs and griding the instances
head.grid(row = 0, column =0)

time_input.grid(row = 1, column = 0,columnspan = 1)

# Looping the Tkinter instance
root.resizable(False, False)
root.mainloop()
