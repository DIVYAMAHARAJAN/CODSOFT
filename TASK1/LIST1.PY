import tkinter as tk

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        selected = listbox.curselection()
        listbox.delete(selected)
    except:
        pass

# Main window
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x350")

# Entry box
entry = tk.Entry(root, width=25)
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

# Listbox
listbox = tk.Listbox(root, width=30, height=10)
listbox.pack(pady=10)

root.mainloop()
