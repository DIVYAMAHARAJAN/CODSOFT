import tkinter as tk

contacts = {}

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name:
        contacts[name] = f"Phone: {phone}, Email: {email}"
        listbox.insert(tk.END, name)
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)

def show_contact(event):
    selected = listbox.curselection()
    if selected:
        name = listbox.get(selected)
        details.set(contacts[name])

# Window
root = tk.Tk()
root.title("Contact Book")
root.geometry("350x400")

tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Phone").pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=5)

listbox = tk.Listbox(root)
listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", show_contact)

details = tk.StringVar()
tk.Label(root, textvariable=details).pack()

root.mainloop()
