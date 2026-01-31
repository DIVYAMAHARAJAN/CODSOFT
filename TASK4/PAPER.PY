import random

choices = ["rock", "paper", "scissors"]

print("--- ROCK PAPER SCISSORS GAME ---")

while True:
    user_choice = input("\nEnter rock, paper, or scissors (or 'exit' to quit): ").lower()

    if user_choice == "exit":
        print("Thanks for playing!")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)
    print("Computer chose:", computer_choice)

    if user_choice == computer_choice:
        print("Result: Draw")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result: You Win 🎉")
    else:
        print("Result: You Lose 😢")
