from tkinter import *
from PIL import ImageTk , Image

root=Tk()
root.title('Adding frames')
root.iconbitmap('D:/Documents/ico/calc.ico')


frame = LabelFrame(root, text="This is a frame", padx = 50, pady = 50)
frame.pack(padx = 50, pady= 50)
 
     
button_frame= Button(frame , text = "Dock click this guy...").pack()

root.mainloop()