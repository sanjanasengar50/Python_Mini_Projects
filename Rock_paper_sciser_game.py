"""
WORKING OF PROJECT:
1- INPUT from user(Rock, paper, scisser)
2- Commputer choice (Computer will randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = Drow
Rock - Paper = Paper win
Rock - Scissor = Rock win

B- Paper
Paper - Paper = Draw
Paper - Scissor = Scissor win
Paper - Rock = Paper win

C- Scissor
Scissor - Scissor = Draw
Scissor - Rock = Rock win
Scissor - Paper = Scissor win
"""

import random
item_list = ["Rock", "Paper", "Scissor"]

while True:
    user_choice = input("Enter your move = Rock, Paper, Scissor (or 'q' to quit): ")
    if user_choice == "q":
        print("Game ended")
        break
    computer_choice = random.choice(item_list)

    print(f"User choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if(user_choice == computer_choice):
        print("It's a Draw")

    elif user_choice == "Rock":
        if computer_choice == "Paper":
            print("Paper covers Rock = Computer win")
        else:
            print("Rock smashes scissor = You win")

    elif user_choice == "Paper":
        if computer_choice == "Scissor":
            print("Scissor cuts Paper = Computer win")
        else:
            print("Paper covers Rock = You win")

    elif user_choice == "Scissor":
        if computer_choice == "Rock":
            print("Rock smashes scissor = You win")
        else:
            print("Scissor cuts Paper = You win")









