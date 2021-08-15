from tkinter import *

#Creating a  new instance 
root = Tk()

#Icon for the app
root.iconbitmap('D:\Documents\ico\counter.ico')

# setting up title for the program
root.title("Counter")

#Creating functions for all the instances
def blue_counter_update():
    f_num= int(blue_label_number.cget("text"))
    print (f_num)
    
def red_label_color():
    red_label.config(bg="red")

def blue_label_color():
    blue_label.config(bg="blue")

#creating a label for the counter 
red_label_head = Label(root , text = "RED TEAM",fg = "red")
blue_label_head = Label(root , text = "BLUE TEAM",fg="blue")
red_label = Label(root , text = "Counter 👇🏼")
red_label_number = Label(root , text = "0")
blue_label_number = Label(root , text = "0")
blue_label = Label(root , text = "Counter 👇🏼 ")
counter_header = Label(root , text = "COUNTER")

#Creating a button for the counter
counter_header.grid(row = 0 , column =0 , columnspan =3)
red_button = Button(root , text = "Increase Counter")
blue_button = Button(root , text = "Increase Counter",command =blue_counter_update)

# griding all the instances
red_label_head.grid(row = 1 , column = 1)
red_label.grid(row = 2 , column = 1)
red_label_number.grid(row = 4 , column = 1)
red_button.grid(row = 5 , column = 1)

blue_label_head.grid(row = 1 , column = 2)
blue_label.grid(row = 2 , column = 2)
red_label_number.grid(row = 4 , column = 2)
blue_button.grid(row = 5 , column = 2)

#Setting the size of the tkinter instance
root.geometry("200x110")

#Making the instance de-sizeable
root.resizable(False, False)

#Looping the Tkinter instance
root.mainloop()