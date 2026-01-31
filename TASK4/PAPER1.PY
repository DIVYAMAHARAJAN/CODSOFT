import tkinter as tk
import random

def play(user_choice):
    computer_choice = random.choice(["Rock", "Paper", "Scissors"])
    result = ""

    if user_choice == computer_choice:
        result = "Draw"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win 🎉"
    else:
        result = "You Lose 😢"

    result_label.config(
        text=f"You: {user_choice}\nComputer: {computer_choice}\nResult: {result}"
    )

# Window
root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("300x300")

tk.Label(root, text="Choose one", font=("Arial", 14)).pack(pady=10)

tk.Button(root, text="Rock", width=10, command=lambda: play("Rock")).pack(pady=5)
tk.Button(root, text="Paper", width=10, command=lambda: play("Paper")).pack(pady=5)
tk.Button(root, text="Scissors", width=10, command=lambda: play("Scissors")).pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=20)

root.mainloop()
