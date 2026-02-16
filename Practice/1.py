# Variables & Data Types

#1 Create a program that swaps the values of two variables without using a third variable.

a = input("Enter first value: ")
b = input("Enter second value: ")

# Swap without third variable
a, b = b, a  # Python's tuple unpacking

print("First value: ", a)
print("Second value: ", b)


#2 Write a program that takes a number as input and prints whether it's an integer or a float.

num = input("Enter any number: ")

# Better method using type checking after conversion

num = float(num)  # Convert to number first

if num == int(num):
    print("It's an integer")
else:
    print("It's a float")



#3 Create variables of different data types and use the type() function to verify each one.

# String
str_var = input("Enter your string: ")
print(f"Type of str_var: {type(str_var)}")

# Integer
num1 = int(input("Enter any integer: "))
print(f"Type of num1: {type(num1)}")

# Float
num2 = float(input("Enter any floating point number: "))
print(f"Type of num2: {type(num2)}")

# List
my_list = [1, 2, 3, 4, 5]
print(f"Type of my_list: {type(my_list)}")

# Tuple
my_tuple = (10, 20, 30)
print(f"Type of my_tuple: {type(my_tuple)}")

# Dictionary
my_dict = {"name": "John", "age": 25}
print(f"Type of my_dict: {type(my_dict)}")

# Set
my_set = {1, 2, 3, 4}
print(f"Type of my_set: {type(my_set)}")

# Boolean
my_bool = True
print(f"Type of my_bool: {type(my_bool)}")


