choice = ""
while choice != "5":
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    choice = input("Select an Option (1-5): ")

    if choice in ["1", "2", "3", "4"]:
        num1 = float(input("Enter First Number: "))
        num2 = float(input("Enter Second Number: "))

        if choice == "1":
            result = num1 + num2
            print(f"{num1} + {num2} = {result}")
        elif choice == "2":
            result = num1 - num2
            print(f"{num1} - {num2} = {result}")
        elif choice == "3":
            result = num1 * num2
            print(f"{num1} * {num2} = {result}")
        elif choice == "4":
            if num2 != 0:
                result = num1 / num2
                print(f"{num1} / {num2} = {result}")
            else:
                print("Error: Division by zero is not allowed.")
    elif choice == "5":
        print("Exiting the calculator. Goodbye!")
    else:  
        print("Invalid choice. Please select a valid option (1-5).")

