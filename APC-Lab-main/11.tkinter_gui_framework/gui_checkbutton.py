from tkinter import *
master = Tk()
var1 = IntVar()
c1 = Checkbutton(master, text='male', variable=var1)
c1.pack()
var2 = IntVar()
c2 = Checkbutton(master, text='female', variable=var2)
c2.pack()
mainloop()