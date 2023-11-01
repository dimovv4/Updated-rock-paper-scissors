import random

options = ("rock", "paper", "scissors")

while True:
    while True:
        player = input("Enter a choice (rock, paper, scissors): ").lower()
        if player in options:
            break
        else:
            print("Invalid choice. Please choose from rock, paper, or scissors.")

    computer = random.choice(options)

    print(f"Player: {player}")
    print(f"Computer: {computer}")

    if player == computer:
        print("It's a tie!")
    elif (player == "rock" and computer == "scissors") or (player == "paper" and computer == "rock") or (player == "scissors" and computer == "paper"):
        print("You win!")

    else:
        print("You lose!")


    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

    if play_again != "y":
        break

print("Thanks for playing!")
