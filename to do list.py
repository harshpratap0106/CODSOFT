

# TO DO LIST
def display_menu():
    print("Menu:")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark As Complete")
    print("4. Exist")

#define fxn. for add task
def add_task(tasks):
    task=input("Enter The Task Details:")
    tasks.append(task)
    print("Task Added Successfully.")

#define function for viewing the task
def view_the_task(tasks):
    print("\nTasks:")
    if not tasks:
        print("No tasks to display.")
    else:
        for i, task in enumerate(task,start=1):
            print(f"{i}.{task}")

#define fxn. for task complete
def mark_as_complete(tasks):
    if not tasks:
       print("No Task To Mark As Complete.")
       return
       view_tasks(tasks)
       index=int(input("Enter Task Index TO Mark As Complete:"))-1
       
    if 0<=index < len(tasks):
        removed_task=tasks.pop(index)
        print(f"Task '{removed_task}' marked as completed and removed.")
    else:
        print("invalid task index.")

#define a fxn. for save tasks
def save_task(tasks):
    with open("task,txt","w") as f:
        for task in tasks:
            f.write(task+'\n')


def load_task():
    try:
        with open("tasks.txt",'r') as f:
            return f.read(),splitness()
    except FileNotFoundError:
        return[]
    
def main():
    tasks=load_task()
    while True:
        display_menu()
        choice=input("Enter Your Choice:")
        if choice =='1':
            add_task(tasks)
        elif choice=='2':
           view_the_task(tasks)
        elif choice=='3':
           mark_as_complete(tasks)
        elif choice=='4':
            print("Existing.")
            save_tasks(tasks)
            break
        else:
            print("Invalid Choice.Please Select A Valid Option.")
if __name__=="__main__":
    main()





