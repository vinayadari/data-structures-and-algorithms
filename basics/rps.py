import random
import sys

CHOICES = ["Rock", "Paper", "Scissors"]

while True:
    try:
        player_input = int(input(
            "Enter...\n  1 for Rock\n  2 for Paper\n  3 for Scissors\n  0 to Exit\n\nYour choice: "
        ))
    except ValueError:
        print("\nInvalid input! Please enter a number.\n")
        continue

    if player_input == 0:
        print("Thanks for playing!")
        sys.exit()

    if player_input < 1 or player_input > 3:
        print("\nInvalid choice. Please enter a number between 1 and 3.\n")
        continue

    player_choice = CHOICES[player_input - 1]
    comp_choice = random.choice(CHOICES)

    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {comp_choice}\n")

    if comp_choice == player_choice:
        print("It's a Draw!")
    elif (player_choice == "Rock" and comp_choice == "Scissors") or \
         (player_choice == "Paper" and comp_choice == "Rock") or \
         (player_choice == "Scissors" and comp_choice == "Paper"):
        print("Congrats, you win!")
    else:
        print("Sorry, you lost.")

    print("-" * 25)
