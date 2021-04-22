def average(num1, num2):
    return (num1+num2)/2

def multi(n,y):
    return (n*y)

def div (n,y):
    return (n/y)

def sub (n,y):
    return (n-y)

def add (n,y):
    return (n+y)

n=int(input('Enter the first number: '))
y=int(input('Enter the second number: '))

print('Do you want to Add,Sub,Multiply,Divide')
z=input()

if z in ['add','Add','ADD']:
    print(add(n,y))

elif z in ['sub','subtract','Sub','Subtract']:
    print(sub(n,y))

elif z in ['div','divide','Div','Divide']:
    print(div(n,y))

elif z in ['multiply','Multiply','multi','Multi','mul']:
    print(multi(n,y))

import tkinter as tk
root=tk.Tk()
root.mainloop()