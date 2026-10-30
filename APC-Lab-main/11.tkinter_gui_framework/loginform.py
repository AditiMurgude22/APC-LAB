import tkinter as tk

def login():
    username = user_entry.get()
    password = pass_entry.get()

    if username == "admin" and password == "1234":
        result.config(text="Login Successful")
    else:
        result.config(text="Invalid Login")

root = tk.Tk()
root.title("Login Form")
root.geometry("300x250")

tk.Label(root, text="Username").pack()
user_entry = tk.Entry(root)
user_entry.pack()

tk.Label(root, text="Password").pack()
pass_entry = tk.Entry(root, show="*")
pass_entry.pack()

tk.Button(root, text="Login", command=login).pack(pady=10)

result = tk.Label(root, text="")
result.pack()

root.mainloop()