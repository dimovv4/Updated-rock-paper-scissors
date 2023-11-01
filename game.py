import random

options = ("rock", "paper", "scissors")
player_score = 0
computer_score = 0

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
        player_score += 1
    else:
        print("You lose!")
        computer_score += 1

    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    while True:
        play_again = input("Play again? (y/n): ").lower()
        if play_again in ["y", "n"]:
            break
        else:
            print("Invalid choice. Please enter 'y' or 'n'.")

    if play_again != "y":
        break

print("Thanks for playing!")

