# Program: Task Reminder System

tasks = []

def add_task():
    """Adds a task to the list"""
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added!")

def view_tasks():
    """Displays all tasks"""
    if not tasks:
        print("No tasks available.")
        return

    for i, task in enumerate(tasks, start=1):
        print(i, "-", task)

def complete_task():
    """Marks task as completed"""
    view_tasks()
    index = int(input("Enter task number to complete: "))

    if 1 <= index <= len(tasks):
        removed = tasks.pop(index - 1)
        print("Completed:", removed)
    else:
        print("Invalid task number!")


while True:
    print("\n=== Task Reminder ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Complete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        break
    else:
        print("Invalid choice!")