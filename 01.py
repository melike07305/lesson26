import datetime
def add_task():
    task = input("What task do you want to add to your To-Do List? \n")
    current_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("ToDoList.txt", 'a') as file:
        file.write(f"{current_date} - {task}\n")
    print("Task added.")
def view_tasks():
    with open("ToDoList.txt", "r") as file:
        lines = file.readlines()
    if not lines:
        print("No tasks in the To-Do List.")
    else:
        print("To-Do List tasks:")
        for line in lines:
            print(line)
print("To-Do List Application")
while True:
    choice = input("\nAdd new task (1) \nView tasks (2) \nExit (3) \nYour choice: ")
    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        print("Thank you for using the To-Do List application!")
        break
