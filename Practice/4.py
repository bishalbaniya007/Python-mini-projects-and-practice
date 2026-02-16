# Tuples

# 12. Create a tuple of coordinates (x, y) and write a program to unpack and print them separately.

# Create a single coordinate tuple
coordinates = (12, 4)

# Unpack into separate variables
x, y = coordinates

print(f"X coordinate: {x}")
print(f"Y coordinate: {y}")

# 13. Write a program that counts how many times a specific element appears in a tuple.
numbers = (1, 3, 5 ,7, 3, 9, 3)
print(f"Number 3 appears {numbers.count(3)} times")

# 14. Try to modify a tuple element and handle the error that occurs.

# Create a tuple
my_tuple = (1, 2, 3, 4, 5)

print("Original tuple:", my_tuple)

# Try to modify an element (this will cause an error)
try:
    my_tuple[0] = 100  # Attempting to change first element
    print("Modification successful")
except TypeError as e:
    print(f"Error occurred: {e}")
    print("Tuples are immutable and cannot be modified!")