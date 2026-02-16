# 31. Create a to-do list program where users can add tasks, view tasks, and remove tasks using a list.

print("!!! To-Do-List !!!")
print()

tasks = []    # empty list

print("1. Add Task")
print("2. View Task")
print("3. Remove Task")


toContinue = True
while toContinue:

  userChoice = int(input("What would you like to do? Choose a number: "))

  if userChoice == 1:
    newTask = input("Enter the task you would like to add: ")
    tasks.append(newTask)

  elif userChoice == 2:
    print(tasks)

  elif userChoice == 3:
    task = input("Enter the task you would like to remove: ")
    tasks.remove(task)

  else:
    print("Invalid choice!!!Chose between 1-3: ")

  userInput = input("Would you like to continue? (y/n) ").lower()
  if userInput != 'y':
    toContinue = False
  
