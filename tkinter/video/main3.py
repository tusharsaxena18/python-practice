# Importing Tkinter 
from tkinter import *

#Creating a new Tkinter instance
root = Tk()

# Creating a function for the Button
def hehe():
    my_label = Label(root,text = "U clicked it!! yay.....")
    my_label.pack()

#Creating a button and packing it
my_button = Button(root,text="Submit" , command=hehe, fg="white", bg="black",)

#packing the button
my_button.pack()

# Looping the Tkinter instance
root.mainloop()