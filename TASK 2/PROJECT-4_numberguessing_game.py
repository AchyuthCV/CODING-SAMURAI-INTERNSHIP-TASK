import tkinter as tk
import random

# Generate random number
number = random.randint(1, 100)
attempts = 0

def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        result_label.config(text="Enter a valid number!")
        return

    guess = int(guess)
    attempts += 1

    if guess < number:
        result_label.config(text="Too Low! Try again.")
    elif guess > number:
        result_label.config(text="Too High! Try again.")
    else:
        result_label.config(
            text=f"Correct! 🎉 You guessed it in {attempts} attempts."
        )

# 🔴 THIS LINE IS MANDATORY
window = tk.Tk()

window.title("Number Guessing Game")
window.geometry("350x250")

# Heading
heading = tk.Label(window, text="Guess the Number (1-100)", font=("Arial", 14))
heading.pack(pady=10)

# Entry box
entry = tk.Entry(window, font=("Arial", 12))
entry.pack(pady=5)

# Button
button = tk.Button(window, text="Check Guess", command=check_guess)
button.pack(pady=10)

# Result label
result_label = tk.Label(window, text="", font=("Arial", 12))
result_label.pack(pady=10)

# 🔴 THIS LINE IS ALSO MANDATORY
window.mainloop()
