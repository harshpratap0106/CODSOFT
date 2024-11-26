#CREATED BY - HARSH PRATAP SINGH 
#TASK 1 - TO DO LIST

#TO DO LIST
print("----WELCOME TO THE TO DO LIST----")
tasks = []

def add_tasks():
    create_task = int(input("How many tasks do you want to add? "))
    
    for i in range(create_task):
        task_name = input(f"Enter task {i + 1}: ")
        tasks.append(task_name)
        print(f"Task '{task_name}' added successfully.")

    print("\nYour current tasks are:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def update_task():
    task_to_update = input("Enter the task name you want to update: ")
    if task_to_update in tasks:
        new_task_name = input("Enter the new task name: ")
        index = tasks.index(task_to_update)
        tasks[index] = new_task_name
        print(f"Task '{task_to_update}' updated to '{new_task_name}'.")
    else:
        print("Task not found.")

def display_tasks():
    print("\nYour current tasks are:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task}")

def task_list():
    add_tasks()

    while True:
        print("\nOptions:")
        print("1. Update a task")
        print("2. Display tasks")
        print("0. Exit")
        operation = int(input("Enter your choice: "))
    
        if operation == 1:
            update_task()
        elif operation == 2:
            display_tasks()
        elif operation == 0:
            print("THANK YOU for using the TO DO LIST.")
            break
        else:
            print("Invalid input. Please try again.")

task_list()
