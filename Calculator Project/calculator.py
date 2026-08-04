choice = ""
while choice != 5:
    print("Calculator App")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    if choice == 1:
        print(num1 + num2)

    elif choice == 2:
        print("You chose Subtraction")
    elif choice == 3:
        print("You chose Multiplication")
    elif choice == 4:
        print("You chose Division")
    elif choice == 5:
        print("Thank you for Using Calculator")
    #else:
        #print("Invalid Operators")

    num1 = float(input("Enter First Number: "))
    num2 = float(input("Enter Second Number: "))
    choice = float(input("Choose Operators: "))