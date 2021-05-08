# Importing Tkinter 
from tkinter import *

#Creating a new Tkinter instance
root = Tk()

#Creating a new Tkinter label
myLabel = Label(root,text = "Heya")
myLabel2 = Label(root,text = "My name is Tushar Saxena")
myLabel3 = Label(root,text = " ")

#Placing the label on the grid
myLabel.grid(row=0,column=0)
myLabel2.grid(row=1,column=5)
myLabel3.grid(row=1,column=1)

# Looping the Tkinter instance
root.mainloop()