task = []


def showMenu():
    print("\n To-Do List Menu")
    print("1. View task")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")


while True:
    showMenu()
    Choice = input("Enter choiche (1-4): ")

    if Choice == "1":
        if not task:
            print(" No Task")
        else:
            print("\n Your Task: ")
            for i, task in enumerate(task, 1):
                print(f"{i}.{task}")
    elif Choice == "2":
        task = input("Enter a new task ")
        task.append(task)
        print(f"Task '{task}' added.")
    elif Choice == "3":
        if not task:
            print("No task to remove")
        else:
            for i, task in enumerate(task, 1):
                print(f"{i}.{task}")
            try:
                task_num = int(input("Enter task number to remove: "))
                removed = task.pop(task_num - 1)
                print(f"Task {removed} removed.")
            except (ValueError, ImportError):
                print("Invalid task number")
    elif Choice == "4":
        print("Exiting....")
    else:
        print("Invalid Choice")
