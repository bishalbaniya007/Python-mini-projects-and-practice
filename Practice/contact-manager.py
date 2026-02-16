# 34. Build a simple contact manager using dictionaries and loops that allows adding, viewing, and searching contacts.

print("!!! CONTACT MANAGAER !!!\n")

contacts ={}    # empty contact dictionary

while True:
  print("\n--- MENU ---")
  print("1. Add contact")
  print("2. View Contact")
  print("3. Search Contact")
  print("4. Exit")

  try:
    choice  = int(input(("\nChoose the task you wish to perform (1-4): ")))
  except ValueError:
    print("Invalid input! Please enter aa number.")
    continue

  if choice == 1:
    name = input("\nEnter the name of the contact: ").lower()
    contact = input("Enter the contact no: ")

    contacts.update({name: contact})
    print(f"{name} added successfully to the contacts.")

  elif choice == 2:
    if len(contacts) == 0:
      print("\nYou havenot saved any contact.")
    else:
      print("\n Your saved contacts:")
      print(contacts)

  elif choice == 3:
    name = input("\nEnter the contact name: ").lower()
    if name not in contacts:
      print(f"{name} isnot saved in your contacts.")
    else:
      print(f"{name}: {contacts[name]}")

  elif choice == 4:
    print("GoodBye!!!")
    break

  else:
    print("Invalid choice!! Choose a number between 1-4: ")

