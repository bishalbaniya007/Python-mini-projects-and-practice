# 1️⃣2️⃣ Palindrome Checker

# Check if a string is palindrome.

word = input("Enter any word: ").lower()
reverse = word[::-1]

if reverse == word:
  print("Palindrome")
else:
  print("Not palindrome")