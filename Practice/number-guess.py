# 33. Create a number guessing game where the computer picks a random number and the user has to guess it (you'll need to import the random module).

print("!!! NUMBER GUESSING GAME !!!\n")

import random

print("Welcome to number guessing game !!!\n")
print("Levels: ")
print("1. Easy")
print("2. Medium")
print("3. Hard")

while True:
  try:
    level = int(input("\nChoose the difficulty level (1-3): "))
  except ValueError:
    print("Invalid input!! Please enter a number.")
    continue

  if level == 1:
    maximum = 10
    num = random.randint(1, maximum)
    break
  elif level == 2:
    maximum = 50
    num = random.randint(1, maximum)
    break
  elif level == 3:
    maximum = 100
    num = random.randint(1, maximum)
    break
  else:
    print("Choose between 1-3.")

guess = 0
attempts = 0

while guess != num:
  try:
    guess = int(input(f"\nGuess a number between 1 to {maximum}: "))
  except ValueError:
    print("Invalid input! Please enter a number.")
    continue

  if guess > num:
    print("Too high! Go lower.")
  elif guess < num:
    print("Too low! Go higher.")
  else:
    print("You're goddamn right!")
  
  attempts += 1

print(f"\nIt took you {attempts} to guess the number.")