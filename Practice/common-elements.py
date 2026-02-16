# Combined Challenges

# 35. Write a program that finds common elements between three different lists.

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 5, 7, 11]
list3 = [3, 6, 9, 12, 15]

list4 = list(set(list1).intersection(set(list2)))

list5 = list(set(list4).intersection(list3))

print(list5)

# or 

common = []

for item in list1:
    if item in list2 and item in list3:
        common.append(item)

print(common)