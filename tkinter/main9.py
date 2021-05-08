from tkinter import *

root=Tk()
root.title('Adding frames')
root.iconbitmap('D:/Documents/ico/calc.ico')

# r = IntVar()
# r.set("0")

MODES = [
            ("Pesto" , "Pesto"),
            ("Cheese " , "Cheese"),
            ("Extra Cheese" , "Extra Cheese"),
            ("Onion" , "Onion")    
    
    
]

pizza = StringVar()
pizza.set("Pepperoni")

for text , mode in MODES:
    Radiobutton(root , text=text , variable = pizza , value=mode).pack(anchor = W)


def clicked(value):
    my_label = Label(root , text = value)
    my_label.pack()

    
# Radiobutton(root , text = "Option 1 " , variable = r , value = 1).pack()
# Radiobutton(root , text = "Option 2 " , variable = r , value = 2).pack()

# my_label = Label(root , text = " ")
# my_label.pack()

button = Button(root , text = "Get value" , command = lambda: clicked(pizza.get())).pack()

root.mainloop()