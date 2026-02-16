# Sets

# 19. Take two lists and find the common elements using sets.

list1 = [1, 3, 5, 7, 9]
list2 = [2, 3, 5, 7, 11]

set1 = set(list1)
set2 = set(list2)

set3 = set1.intersection(set2)

print(set3)

# 20. Write a program that removes all duplicates from a list using sets.

list1 = [1, 3, 5, 3, 5, 7, 9]
print(set(list1))


# 21. Create two sets and perform union, intersection, and difference operations.
set1 = {1, 3, 5, 7, 9}
set2 = {2, 3, 5, 7, 11}

#union
print(set1.union(set2))

#intersection
print(set1.intersection(set2))

#difference
print(set1.difference(set2))