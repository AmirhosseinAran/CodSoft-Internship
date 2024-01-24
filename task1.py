import os

def display_menu():
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            if tasks:
                print("Tasks:")
                for index, task in enumerate(tasks, start=1):
                    print(f"{index}. {task.strip()}")
            else:
                print("No tasks found.")
    else:
        print("No tasks found.")

def add_task():
    task = input("Enter the task: ")
    with open("tasks.txt", "a") as file:
        file.write(task + "\n")
    print("Task added successfully!")

def mark_completed():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to mark as completed: ")) - 1
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_index < len(tasks):
            completed_task = tasks.pop(task_index)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task marked as completed: {completed_task.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_index = int(input("Enter the task number to delete: ")) - 1
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
        if 0 <= task_index < len(tasks):
            deleted_task = tasks.pop(task_index)
            with open("tasks.txt", "w") as file:
                file.writelines(tasks)
            print(f"Task deleted: {deleted_task.strip()}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        if choice == "1":
            view_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            mark_completed()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            print("Exiting the To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
