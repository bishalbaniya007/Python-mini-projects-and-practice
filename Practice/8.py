# Loops

# 26. Print all even numbers from 1 to 100.

num = 1
while num <= 100:
  if num % 2 == 0:
    print(num)
  num += 1

# 27. Create a program that prints the multiplication table for any number.

num = int(input("Enter any number: "))
i = 1

while i <= 10:
  print(num * i)
  i+= 1

# 28. Write a program to find all prime numbers between 1 and 50.

for i in range(2, 51):  # Start from 2 (1 is not prime)
    is_prime = True
    
    for j in range(2, int(i ** 0.5) + 1):  # Only check up to sqrt(i)
        if i % j == 0:
            is_prime = False
            break  # No need to check further
    
    if is_prime:
        print(i)

# 29. Create a pattern printer that prints a pyramid of stars based on user input for height.

height = int(input("Enter the height of the pyramid: "))

for i in range(1, height+1):     # controlling height
  for j in range(height,i,-1):       # printing spaces
    print(" ", end="")
  
  for k in range(1, i*2):   # printing stars
    print("*", end="")

  print()

# 30. Write a program that takes a number and prints its factorial.

num = int(input("Enter any number: "))
fact = 1

for i in range (1, num+1):
  fact *= i

print("Factorial: ", fact)