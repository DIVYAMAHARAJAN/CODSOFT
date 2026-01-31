import tkinter as tk
import random
import string

def generate():
    length = int(entry.get())
    chars = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(chars) for _ in range(length))
    result.set(password)

# Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("300x200")

tk.Label(root, text="Password Length").pack(pady=5)
entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Generate Password", command=generate).pack(pady=10)

result = tk.StringVar()
tk.Entry(root, textvariable=result, width=30).pack(pady=5)

root.mainloop()
