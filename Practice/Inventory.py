# 1️⃣3️⃣ Inventory System (Mini Project)

# Create a dictionary for a shop:

# inventory = {
#     "apple": 10,
#     "banana": 5,
#     "orange": 8
# }


# Ask user:

# What item they want

# Quantity

# Update inventory if available.
# If not, print “Out of stock”.

inventory = {
  "apple" : 20,
  "banana" : 20,
  "mango" : 20,
  "orange": 20
}

toContinue = True

while toContinue:


  fruit = input("What fruit do you want? : ").lower()

  if fruit not in inventory:
    print(f"{fruit} isnot availabe.")

  else:
    quantity = int(input(f"How many {fruit} do you want? : "))

    if inventory[fruit] == 0:
      print("Sorry! Out of Stock")

    elif quantity <= inventory[fruit]:
      print(f"You purchased {quantity} {fruit}/s.")
      inventory[fruit] -= quantity

    else:
      print(f"{quantity} {fruit}/s arenot available. Only {inventory[fruit]} are available.")
  
  userResponse = input("Do you still wish to continue shopping? (y/n): ").lower()
  if userResponse != 'y':
    toContinue = False


  

print(inventory)
  



