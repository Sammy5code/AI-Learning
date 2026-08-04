import random
secret_number = random.randint(1, 100)
guess = None
no_of_guesses = 0
while guess != secret_number:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess > secret_number:
        print("Too high! Try again.")
        no_of_guesses += 1
    elif guess < secret_number:
        print("Too low! Try again.")
        no_of_guesses += 1
    else:
        print(f"Congratulations! You've guessed the number {secret_number} in {no_of_guesses + 1} attempts.")