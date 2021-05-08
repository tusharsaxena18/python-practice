# Importing required libraries.
from tkinter import *
from PIL import ImageTk , Image

#Creating a new Tkinter instance
root = Tk() 
root.iconbitmap('D:\Documents\ico\calc.ico')
# root.geometry('250x250')

#Title-ing the Tkinter object
root.title("Login")

def popup():
    return

user_label =Label(root, text = 'Username')
pass_label =Label(root, text = 'Password')
user_entry = Entry(root)
pass_entry = Entry(root)
login = Button(root, text = 'Login')

#griding the labels
user_entry.grid(row=0 , column =1)
pass_entry.grid(row=1 , column =1)
user_label.grid(row=0 , column =0)
pass_label.grid(row=1 , column =0)
login.grid(row = 2 , column = 1,sticky=E)

# Looping the Tkinter instance
root.mainloop()
