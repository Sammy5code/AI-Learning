import random
player_score = 0
computer_score = 0
while True:
    choices = ["rock", "paper", "scissors"]
    player_choice = input("Enter rock, paper, or scissors: ").lower()
    if player_choice not in choices:
        print("Invalid choice. Please try again.")
        continue
    computer = random.choice(choices)
    print(f"Computer chose: {computer}")
    if player_choice == computer:
        print("It's a tie!")
    elif (player_choice == "rock" and computer == "scissors") or \
         (player_choice == "paper" and computer == "rock") or \
            (player_choice == "scissors" and computer == "paper"):
            player_score += 1
            print("You win!")
    else:
        computer_score += 1
        print("You lose!")

    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break


