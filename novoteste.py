from tkinter import * 
from tkinter.ttk import *



master = Tk() 
l1 = Label(master, text = 'teste') 
l2 = Label(master, text = "Width") 
l1.grid(row = 0, column = 0, sticky = W, pady = 2) 
l2.grid(row = 1, column = 0, sticky = W, pady = 2) 
e1 = Entry(master) 
e2 = Entry(master) 
e1.grid(row = 0, column = 1, pady = 2) 
e2.grid(row = 1, column = 1, pady = 2) 
c1 = Checkbutton(master, text = "Preserve") 
c1.grid(row = 2, column = 0, sticky = W, columnspan = 2) 
#img = PhotoImage(file = r"C:\Users\Admin\Pictures\capture1.png") 
#img1 = img.subsample(2, 2) 
#Label(master, image = img1).grid(row = 0, column = 2, 
#       columnspan = 2, rowspan = 2, padx = 5, pady = 5) 
b1 = Button(master, text = "Zoom in") 
b2 = Button(master, text = "Zoom out") 
b1.grid(row = 2, column = 2, sticky = E) 
b2.grid(row = 2, column = 3, sticky = E) 
mainloop() 

