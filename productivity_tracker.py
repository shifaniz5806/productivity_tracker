#Productivity Tracker

tasks = []
def add_to_task():
    task = input("Enter task: ")
    tasks.append(task)
    task_status[task] = "incomplete"

task_status = {}

def view_productivity():
    complete = 0
    incomplete = 0
    for t in task_status:
        if task_status[t] == "complete":
            complete += 1
        else:
            incomplete += 1
    print("Completed tasks: ", complete)
    print("incomplete tasks: ", incomplete)


while True:
    print("Welcome to Productivity tracker")
    print("\n 1. Add a task \n 2. View all tasks \n 3. Complete a task \n 4. View productivity \n 5. Exit")
    choice = input("Enter your choice: ")


    if choice == "1":
        add_to_task()
        print("Added to tasks!")
    elif choice == "2":
        print("\nYour Tasks:")
        for number, task in enumerate(tasks, start=1):
            print(number, task, "-", task_status[task])
    elif choice == "3":
        task = input("Enter name of the task you have completed: ")
        task_status[task] = "complete"
    elif choice == "4":
        view_productivity()
    elif choice == "5":
        break
    else:
        print("invalid choice. Please try again")