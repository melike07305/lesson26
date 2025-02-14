def add_student(name, course, price):
    with open("student_data.txt", "a") as file:
        file.write(f"{name},{course},{price}\n")

def show_students():
    with open("student_data.txt", "r") as file:
        lines = file.readlines()
    for line in lines:
        name, course, price = line.strip().split(",")
        print(f"Name: {name}, Course: {course}, Price: {price}")

def remove_student(name):
    with open("student_data.txt", "r") as file:
        lines = file.readlines()
    with open("student_data.txt", "w") as file:
        removed = False
        for line in lines:
            data = line.strip().split(",")
            if data[0] != name:
                file.write(line)
            else:
                removed = True
    if removed:
        print(f"{name} was successfully removed.")
    else:
        print(f"{name} not found.")

print("Welcome to the student Management System!")
while True:
    choice = input("\nAdd Student (1) \nShow Students (2) \nRemove Student (3) \nExit (4) \nYour choice: ")
    if choice == "1":
        name = input("Students Name: ")
        course = input("Cource: ")
        price = input("Price: ")
        add_student(name, course, price)
    elif choice == "2":
        show_students()
    elif choice == "3":
        name = input("Name of the student to remove: ")
        remove_student(name)
    elif choice == "4":
        print("Thank you for using our program!")
        break
