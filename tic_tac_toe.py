import tkinter as tk
from tkinter import messagebox

# Global variables
current_player = "X"
winner = False


def check_winner():
    global winner

    winning_combinations = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for combo in winning_combinations:
        if (
            buttons[combo[0]]["text"] ==
            buttons[combo[1]]["text"] ==
            buttons[combo[2]]["text"] != ""
        ):
            winner = True

            for i in combo:
                buttons[i].config(bg="lightgreen")

            messagebox.showinfo(
                "Tic-Tac-Toe",
                f"Player {buttons[combo[0]]['text']} Wins!"
            )

            return

    # Check for Draw
    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a Draw!")
        return


def toggle_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

    label.config(text=f"Player {current_player}'s Turn")


def button_click(index):
    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()

        if not winner:
            toggle_player()


# Create main window
root = tk.Tk()
root.title("Tic-Tac-Toe")

# Create Buttons
buttons = []

for i in range(9):
    button = tk.Button(
        root,
        text="",
        font=("Arial", 25),
        width=6,
        height=2,
        command=lambda i=i: button_click(i)
    )

    button.grid(row=i // 3, column=i % 3)
    buttons.append(button)

# Player Turn Label
label = tk.Label(
    root,
    text=f"Player {current_player}'s Turn",
    font=("Arial", 14)
)

label.grid(row=3, column=0, columnspan=3, pady=10)

root.mainloop()