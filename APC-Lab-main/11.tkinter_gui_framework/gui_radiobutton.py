from tkinter import *
root = Tk()
v = IntVar()
r1 = Radiobutton(root, text='Male', variable=v, value=1)
r1.pack()
r2 = Radiobutton(root, text='Female', variable=v, value=2)
r2.pack()
mainloop()