import tkinter as tk

root = tk.Tk()
root.title("My First Window")
root.geometry("400x300")

label = tk.Label(root, text="Hello, Python!")
label.pack()

root.mainloop()