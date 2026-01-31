import tkinter as tk

def click(event):
    global expression
    text = event.widget.cget("text")

    if text == "=":
        try:
            result = str(eval(expression))
            screen.set(result)
            expression = result
        except:
            screen.set("Error")
            expression = ""
    elif text == "C":
        expression = ""
        screen.set("")
    else:
        expression += text
        screen.set(expression)

# Main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

expression = ""
screen = tk.StringVar()

# Display
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, relief=tk.SUNKEN)
entry.pack(fill=tk.X, padx=10, pady=10)

# Buttons
button_texts = [
    "7","8","9","/",
    "4","5","6","*",
    "1","2","3","-",
    "0",".","=","+",
    "C"
]

frame = tk.Frame(root)
frame.pack()

for i, text in enumerate(button_texts):
    btn = tk.Button(frame, text=text, font="Arial 15", width=5, height=2)
    btn.grid(row=i//4, column=i%4, padx=5, pady=5)
    btn.bind("<Button-1>", click)

root.mainloop()
