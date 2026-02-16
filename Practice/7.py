# Conditional Statements

# 22. Write a program that checks if a year is a leap year.

year = int(input("Enter any year: "))
print("Leap year" if year % 4 == 0 else "Not a leap year")

# 23. Create a simple calculator that takes two numbers and an operator (+, -, *, /) and performs the operation.

num1 = float(input("Enter any number: "))
opr = input("Enter the operation to perform (+ - * /): ")
num2 = float(input("Enter any number: "))

if opr == '+':
  print(f"{num1} + {num2} = {num1 + num2}")
elif opr == '-':
  print(f"{num1} - {num2} = {num1 - num2}")
elif opr == '*':
  print(f"{num1} * {num2} = {num1 * num2}")
elif opr == '/':
  if num2 != 0:
    print(f"{num1} / {num2} = {num1 / num2}")
  else:
    print("Division by 0")
else:
  print("Invalid operation!!!")

# 24. Write a program that determines if a number is positive, negative, or zero.

num = float(input("Enter any number: "))
if num > 0:
  print("Positive number")
elif num < 0:
  print("Negative number")
else:
  print("Zero")

# 25. Create a grading system that converts numerical scores to letter grades.

marks  = float(input("Enter the marks of the student: "))
marks = float(input("Enter the marks of the student: "))

if marks > 100 or marks < 0:
    print("Invalid marks! Enter between 0-100")
elif marks > 90:
    print("Grade: A")
elif marks > 80:
    print("Grade: B")
elif marks > 70:
    print("Grade: C")
elif marks > 60:
    print("Grade: D")
else:
    print("Grade: F")