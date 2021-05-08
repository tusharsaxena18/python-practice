# Importing Tkinter 
from tkinter import *

#Creating a new Tkinter instance
root = Tk()

#Title-ing the Tkinter object
root.title("Calculator")

#Adding images to the program
root.iconbitmap('D:/Documents/ico/calc.ico')

#Creating a input Tkinter instance
box = Entry(root , width = 35 , borderwidth = 5)
box.grid(row = 0 , column = 0 , columnspan =3 ,padx = 10 , pady = 10)

# Declaring the functions for the number buttons
def button_number(number):
    previous = box.get()
    box.delete(0,END)
    box.insert(0,str(previous) + str(number))

# Creating  a function for clear button   
def button_clear():
    box.delete(0,END)
    
# Creating a function for the clear button    
def button_add():
    num = box.get()
    global first_num
    global math
    math = "Addition"
    first_num = int(num)
    box.delete(0,END)

# Creating a function for the multiply button
def button_multiply():
    num = box.get()
    global first_num
    global math
    math = "Multiply"
    first_num = int(num)
    box.delete(0,END)

# Creating a function for the subtract button
def button_subtract():
    num = box.get()
    global first_num
    global math
    math = "Subtract"
    first_num = int(num)
    box.delete(0,END)

# Creating a function for the Divide button
def button_divide():
    num = box.get()
    global first_num
    global math
    math = "Divide"
    first_num = int(num)
    box.delete(0,END)
    
# Creating a function for the Modulus button    
def button_mod():
    num = box.get()
    global first_num
    global math
    math = "mod"
    first_num = int(num)
    box.delete(0,END)

# Creating the function for the equal button
def button_equal():
    second_num = box.get()
    box.delete(0,END)

    if math == "Addition":
         box.insert(0,first_num + int(second_num))
    
    elif math == "Subtract":
        box.insert(0,first_num - int(second_num))
    
    elif math == "Multiply":
        box.insert(0,first_num * int(second_num))

    elif math == "Divide":
        box.insert(0,first_num / int(second_num))

    elif math == "mod":
        box.insert(0,first_num % int(second_num))
        
#Creating new Tkinter buttons
button_1 = Button(root , text = "1" , padx = 40 ,pady =20 , command=lambda: button_number(1))
button_2 = Button(root , text = "2" , padx = 40 ,pady =20 , command=lambda: button_number(2))
button_3 = Button(root , text = "3" , padx = 40 ,pady =20 , command=lambda: button_number(3))
button_4 = Button(root , text = "4" , padx = 40 ,pady =20 , command=lambda: button_number(4))
button_5 = Button(root , text = "5" , padx = 40 ,pady =20 , command=lambda: button_number(5))   
button_6 = Button(root , text = "6" , padx = 40 ,pady =20 , command=lambda: button_number(6))
button_7 = Button(root , text = "7" , padx = 40 ,pady =20 , command=lambda: button_number(7))
button_8 = Button(root , text = "8" , padx = 40 ,pady =20 , command=lambda: button_number(8))
button_9 = Button(root , text = "9" , padx = 40 ,pady =20 , command=lambda: button_number(9))
button_0 = Button(root , text = "0" , padx = 40 ,pady =20 , command=lambda: button_number(0))
button_e = Button(root , text = "=" , padx = 40 ,pady =20 , command=button_equal)
button_a = Button(root , text = "+" , padx = 39 ,pady =20 , command= button_add)
button_s = Button(root , text = "-" , padx = 40 ,pady =20 , command=button_subtract)
button_m = Button(root , text = "x" , padx = 40 ,pady =20 , command=button_multiply)
button_d = Button(root , text = "/" , padx = 40 ,pady =20 , command=button_divide)
button_c = Button(root , text = "Clear" , padx = 30 ,pady =20 , command=button_clear)
button_exit = Button(root , text = "Exit" , padx = 33 ,pady =20 , command=root.quit)
button_mod = Button(root , text = "%" , padx = 40 ,pady =20 , command=button_mod)


# Placing the buttons on the gui
button_1.grid(row =3 , column = 0) #third row
button_2.grid(row =3 , column = 1) #third row
button_3.grid(row =3 , column = 2) #third row

button_4.grid(row =2 , column = 0) #second row
button_5.grid(row =2 , column = 1) #second row
button_6.grid(row =2 , column = 2) #second row

button_7.grid(row =1 , column = 0) #first row
button_8.grid(row =1 , column = 1) #first row
button_9.grid(row =1 , column = 2) #first row

button_0.grid(row = 4 , column = 1) #operations row

button_a.grid(row =4 , column = 0)
button_m.grid(row = 5 , column = 0) #operations row
button_d.grid(row = 5 , column = 2) #operations row
button_s.grid(row = 4 , column = 2) #operations row
button_mod.grid(row = 6 , column = 2) #operations row
button_c.grid(row = 6 , column = 1) #operations row
button_e.grid(row = 5 , column = 1) #operations row
button_exit.grid(row = 6 , column = 0) #operations row

# Looping the Tkinter instance
root.mainloop()
