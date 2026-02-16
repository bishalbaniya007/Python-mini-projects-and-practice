# 1️⃣1️⃣ Prime Number Checker

# Check if a number is prime.

num = int (input("Enter any number >1 :"))
count = 0

for i in range(2, num):
  if num % i == 0:
    count += 1

if count == 0:
  print("Pirme")
else:
  print("Not prime")