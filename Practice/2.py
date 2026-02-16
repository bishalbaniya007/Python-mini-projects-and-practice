# Strings

# 4. Write a program that takes a sentence and prints it in reverse.
# Steps:
    # 1. Take input
    # 2. Convert it to list using .split() method
    # 3. Reverse the list using .reverse() method
    # 4. Join the elements using .join() method

sentence  = input("Enter any sentence: ")

wordsList = sentence.split()

wordsList.reverse()

result = " ".join(wordsList)

print(result)

# 5. Create a program that counts how many vowels are in a user-input string.

word = input("Enter any word: ")
count = 0

for ch in word:
  if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
    count += 1

print("Vowels count: ", count)

# 6. Take a string and check if it's a palindrome (reads the same forwards and backwards).

word = input("Enter any word: ")
wordRev = word[::-1]

if word == wordRev:
  print("Palindrome")
else:
  print("Not palidrome")

# 7. Write a program that takes a full name and prints the initials.

name = input("Enter your full name: ")
words = name.split()
initials = ""

for word in words:
    initials += word[0].upper() + "."

print(initials[:-1])  # Remove last dot


