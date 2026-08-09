try:
    with open("tasks.txt", "r") as file:
        task_list = [task.strip() for task in file.readlines()]
except FileNotFoundError:
    task_list = []

def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in task_list:
            file.write(task + "\n")

choice = ""

while choice != "4":
    print("===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    choice = input("Enter your choice (1-4): ")

    if choice == "1": 
        task = input("Enter the task you want to add: ")
        if task.strip() == "":
            print("Task cannot be empty. Please try again.")
            continue
        else:
            task_list.append(task)
            save_tasks()
            print("Task added successfully!")
    elif choice == "2":
        print("Your Tasks:")
        for number, task in enumerate(task_list, start=1):
            print(f"{number}. {task}")

    elif choice == "3":
        if len(task_list) == 0:
            print("No tasks to remove.")
            continue
        else:
            print("Removing a task")

            for number, task in enumerate(task_list, start=1):
                print(f"{number}. {task}")

            try:
                task_number = int(input("Enter the task number you want to remove: "))
                if task_number < 1 or task_number > len(task_list):
                    print("Invalid task number. Please try again.")
                    continue
                else:
                    task_list.pop(task_number - 1)
                    save_tasks()
                    print("Task removed successfully!")
            except ValueError:
                print("Invalid input. Please enter a valid task number.")
                continue
    elif choice == "4":
        print("Exiting the program.")
    else:
        print("Invalid choice. Please try again.")
