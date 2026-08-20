import json
def load_expenses():
     try:
          with open ("expenses.json", "r") as file:
               expenses = json.load(file)
               return expenses 
     except FileNotFoundError:
          return []

def save_expenses():
     with open ("expenses.json", "w") as file:
          json.dump(expenses, file)
          

def add_expense():
    category = input("Enter the category of this expense: ").strip()
    try:
         amount = float(input("Enter the amount: "))
    except ValueError:
         print("Invalid input. Try again")
         return
    if amount <= 0:
         print("Amount must be greater than Zero")
         return
    description = input("Enter the description: ").strip()
    expense = {"category": category, "amount": amount, "description": description}
    expenses.append(expense)
    save_expenses()
    print("Expense added successfully")

def view_expenses():
        if not expenses:
              print("No expenses found")
        else:
            print("Expenses:")
            for index, expense in enumerate(expenses, start=1):
                  print(f"{index}. Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")


def search_expenses():
      search_name = input("Enter the category of expense to search: ").strip()
      found_expense = [expense for expense in expenses if expense['category'].lower() == search_name.lower()]
      if not found_expense:
            print("No expenses found with that name.")
      else:
            print("Found Expense:")
            for index, expense in enumerate(found_expense, start=1):
                  print(f"{index}. Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

def remove_expense():
    if not expenses:
        print("No expenses found")
    else:
        print("Expenses:")
        for index, expense in enumerate(expenses, start=1):
            print(f"{index}. Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

        try:
            expense_number = int(input("Enter the expense number you want to remove: "))
        except ValueError:
            print("Invalid input. Please try again")
            return

        if expense_number < 1 or expense_number > len(expenses):
            print("Invalid Input. Please try again")
        else:
            expense_index = expense_number - 1
            removed_expense = expenses[expense_index]
            expenses.pop(expense_index)
            save_expenses()
            print(f"{removed_expense['category']} was removed successfully!")

def calculate_total():
    total = 0
    for expense in expenses:
        total += expense["amount"]
    print(f"Total expenses: {total}")


def category_total():
     category_totals = {}
     for expense in expenses:
          if expense["category"] in category_totals:
               category_totals[expense["category"]] += expense["amount"]
          else:
               category_totals[expense["category"]] = expense["amount"]
     for index, (category, total) in enumerate(category_totals.items(), start=1):
          print(f"{index}. {category}: {total}")

def edit_expenses():
     if not expenses:
          print("No expenses found")
     else:
          print("Expenses: ")
          for index, expense in enumerate(expenses, start=1):
               print(f"{index}. Category: {expense['category']}, Amount: {expense['amount']}, Description: {expense['description']}")

          try:
               edit_number = int(input("Enter the expense number you want to edit: "))
          except ValueError:
               print("Invalid input. Try Again")
               return
          if edit_number < 1 or edit_number > len(expenses):
               print("Invalid input. Try again")
          else:
               edit_index = edit_number - 1
               edit_expense = expenses[edit_index]
               new_category = input("Enter the new category: ")
               try:
                    new_amount = float(input("Enter the new amount: "))
               except ValueError:
                    print("Invalid input. Try again")
                    return
               if new_amount < 1:
                    print("Invalid input. Try again")
                    return
               new_description = input("Enter the new description: ")
               edit_expense["category"] = new_category
               edit_expense["amount"] = new_amount
               edit_expense["description"] = new_description

               save_expenses()
               print("Expenses have been edited successfully")

               
               

expenses = load_expenses()
choice = ""
while choice != "8":
    print("===== EXPENSE BOOK =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Search Expense")
    print("4. Remove Expense")
    print("5. View total")
    print("6. View Catergory Totals")
    print("7. Edit expenses")
    print("8. Exit")

    choice = input("Enter your choice (1 -7): ")

    # if choice == "1":
    #     add_expense()
    # elif choice == "2":
    #     view_expenses()
    # elif choice == "3":
    #     search_expenses()
    # elif choice == "4":
    #     remove_expense()
    # elif choice == "5":
    #     calculate_total()
    # elif choice == "6":
    #     print("Exiting the program.")
    # else:
    #     print("Invalid choice. try again")

    match choice:
         case "1":
              add_expense()
         case "2" :
              view_expenses()
         case "3":
              search_expenses()
         case "4":
              remove_expense()
         case "5":
              calculate_total()
         case "6":
              category_total()
         case "7":
              edit_expenses()
         case "8":
              print("Exiting the program.")
         case _:
              print("Invalid choice. try again")
             
