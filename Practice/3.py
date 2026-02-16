# Lists

# 8. Create a list of numbers and find the sum and average without using built-in functions like sum().
numbers = [12, 44, 55, 89, 9]
sum = 0
avg = 0

for num in numbers: 
  sum += num

avg = sum / len(numbers)

print("Sum = ", sum)
print("Average = ", avg)

# 9. Write a program that removes all duplicate elements from a list.
numbers = [1, 2, 2, 3, 5, 3]
newList = []    # empty list

for num in numbers:
  if num not in newList:
    newList.append(num)

print(newList)

# 10. Take two lists and merge them into one, then sort it in descending order.
list1 = [1, 2, 2, 3, 5, 3]
list2 = [12, 44, 55, 89, 9]

list3 = list1 + list2

list3.sort()
print(list3)

# 11. Create a program that finds the second largest number in a list.
numbers = [1, 3, 5, 7, 7, 7, 7]
largest = float('-inf')  # Start with very small number
secondLargest = float('-inf')

for num in numbers:
  if num > largest:
    secondLargest = largest
    largest = num

  if num != largest and num > secondLargest:
    secondLargest = num
print("Second largest: ", secondLargest)
