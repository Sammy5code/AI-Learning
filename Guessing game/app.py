import random
secret_number = random.randint(1, 100)
guess = None
no_of_guesses = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    no_of_guesses += 1

    if guess > secret_number:
        print("Too high! Try again.")
    elif guess < secret_number:
        print("Too low! Try again.")
    else:
        if no_of_guesses <= 5:
            print(f"Excellent! You've guessed the number {secret_number} in {no_of_guesses} attempts.")
        elif no_of_guesses <= 10:
            print(f"Good Job! You've guessed the number {secret_number} in {no_of_guesses} attempts.")
        else:
            print(f"Keep Practicing! You've guessed the number {secret_number} in {no_of_guesses} attempts.")
    
    if guess == secret_number:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again == "yes":
            secret_number = random.randint(1, 100)
            guess = None
            no_of_guesses = 0
        else:
            print("Thank you for playing! Goodbye.")
            break