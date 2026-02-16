print("!!! To-Do List !!!")
print()

tasks = []

while True:
    print("\n--- MENU ---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")
    print()
    
    try:
        userChoice = int(input("What would you like to do? Choose a number: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue
    
    if userChoice == 1:
        newTask = input("Enter the task you would like to add: ")
        tasks.append(newTask)
        print(f"✓ Task '{newTask}' added successfully!")
    
    elif userChoice == 2:
        if len(tasks) == 0:
            print("No tasks in your to-do list!")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
    
    elif userChoice == 3:
        if len(tasks) == 0:
            print("No tasks to remove!")
        else:
            print("\n--- Your Tasks ---")
            for i, task in enumerate(tasks, 1):
                print(f"{i}. {task}")
            
            task = input("\nEnter the task you would like to remove: ")
            if task in tasks:
                tasks.remove(task)
                print(f"✓ Task '{task}' removed successfully!")
            else:
                print("Task not found in the list!")
    
    elif userChoice == 4:
        print("Goodbye! 👋")
        break
    
    else:
        print("Invalid choice! Please choose between 1-4.")