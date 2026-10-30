from tkinter import *

root = Tk()

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

mylist = Listbox(root, yscrollcommand=scrollbar.set)

for line in range(100):
    mylist.insert(END, 'Line - ' + str(line))

mylist.pack()

scrollbar.config(command=mylist.yview)

mainloop()