

print("....WELCOME TO THE TO DO LIST....")
tasks = []

def add_tasks():
    create_task = int(input("How many tasks do you want to add?: "))
    
    for k in range(create_task):
        task_name = input(f"Enter task {i + 1}: ")
        tasks.append({"name": task_name, "status": "Due"})
        print(f"Task '{task_name}' added to list.")

    display_tasks()

def update_task():
    task_to_update = input("Enter the task name which you want to update: ")
    for task in tasks:
        if task["name"] == task_to_update:
            new_task_name = input("Enter the new task name: ")
            task["name"] = new_task_name
            print(f"Task '{task_to_update}' updated to '{new_task_name}'.")
            return
    print("Task not found.")

def display_tasks():
    print("\nYour current tasks are:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['name']} - {task['status']}")

def task_complete_or_not():
    task_to_complete = input("Enter the task name you want to mark as completed: ")
    for task in tasks:
        if task["name"] == task_to_complete:
            task["status"] = "Completed"
            print(f"Task '{task_to_complete}' marked as completed.")
            return
    print("Task not found.")

def task_list():
    add_tasks()

    while True:
        print("\nOptions:")
        print("1. Update a task")
        print("2. Display tasks")
        print("3. Mark a task as completed")
        print("0. Exit")
        operation = int(input("Enter your choice: "))
    
        if operation == 1:
            update_task()
        elif operation == 2:
            display_tasks()
        elif operation == 3:
            task_complete_or_not()
        elif operation == 0:
            print("Thank you for using the TO DO LIST!.")
            break
        else:
            print("Invalid input.")

task_list()



