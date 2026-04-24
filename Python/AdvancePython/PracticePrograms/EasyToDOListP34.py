# Program: To-Do List with File Storage

class Todo:
    def __init__(self, filename):
        self.filename = filename

    def add_task(self):
        task = input("Enter task: ")

        with open(self.filename, "a") as file:
            file.write(task + "\n")

        print("Task added!")

    def view_tasks(self):
        try:
            with open(self.filename, "r") as file:
                print("\nYour Tasks:")
                for i, line in enumerate(file, 1):
                    print(i, "-", line.strip())
        except FileNotFoundError:
            print("No tasks found!")

    def clear_tasks(self):
        open(self.filename, "w").close()
        print("All tasks cleared!")


todo = Todo("tasks.txt")

while True:
    print("\n=== To-Do List ===")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Clear Tasks")
    print("4. Exit")

    choice = input("Choice: ")

    if choice == "1":
        todo.add_task()
    elif choice == "2":
        todo.view_tasks()
    elif choice == "3":
        todo.clear_tasks()
    else:
        break