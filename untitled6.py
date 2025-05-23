
tasks = []

def show_menu():
    print("To-Do Notes Builder")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Mark Task as Completed")
    print("5. Exit")

def add_task():
    task = input("Enter a new task: ")
    tasks.append([task, False])
    print("Task added.\n")

def view_tasks():
    if not tasks:
        print("No tasks available.\n")
    else:
        for i, (task, done) in enumerate(tasks, start=1):
            status = "Done" if done else "Not Done"
            print(f"{i}. {task} - {status}")
        print()

def delete_task():
    view_tasks()
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        print("Task deleted.\n")
    except:
        print("Invalid input.\n")

def mark_completed():
    view_tasks()
    try:
        num = int(input("Enter task number to mark as completed: "))
        tasks[num - 1][1] = True
        print("Task marked as completed.\n")
    except:
        print("Invalid input.\n")

while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        mark_completed()
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Please enter a number between 1 and 5.\n")
