tasks = []
while True:
    print("\n---To-Do List Menu---")
    print("1. ADD TASK")
    print("2. VIEW TASKS")
    print("3. EXIT")
    choice = input("Enter your choice: ")
    if choice == "1":
        task = input("Enter your task: ")
        tasks.append(task)
        print("Task added successfully")
    elif choice == "2":
        if len(tasks) == 0:
            print("No tasks Available")
        else:
            print("\nYour tasks:")
            for i in range(len(tasks)):
                print(f"{i+1}. {tasks[i]}")
    elif choice == "3":
        print("Exiting Program. Bye, see you again!")
        break
    else:
        print("Invalid Choice. Try again")
