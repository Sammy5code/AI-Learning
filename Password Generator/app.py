import random
uppercase_letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowercase_letters = "abcdefghijklmnopqrstuvwxyz"
digits = "0123456789"
symbols = "!@#$%^&*()_+-=[]{}|;:,.<>?/"
password = ""
try:
    password_length = int(input("Enter the desired password length: "))
except ValueError:
    print("Invalid input. Please enter a valid number.")
    exit()
if password_length < 4:
    print("Password must be at least 4 characters")
    exit()
else: 
    all_characters = uppercase_letters + lowercase_letters + digits + symbols
    password = password + random.choice(uppercase_letters)
    password = password + random.choice(lowercase_letters)
    password = password + random.choice(digits)
    password = password + random.choice(symbols)
    for i in range(password_length - 4):
        password = password + random.choice(all_characters)
    password = list(password)
    random.shuffle(password)
    password = "".join(password)
    print(f"Your generated password is: {password}")