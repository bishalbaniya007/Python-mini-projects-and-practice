# Dictionaries

# 15. Create a simple phone book using a dictionary where names are keys and phone numbers are values. 
# Add a feature to search for a number by name.

phone = {
  "bishal" : "982914",
  "mom" : "982410",
  "dad" : "981616", 
  "ruby" : "981243"
}

name = input("Enter the name of person you want to search for: ")

if name in phone:
  print(phone.get(name))
else:
  print("Name not availabe")

# 16. Write a program that counts the frequency of each word in a sentence using a dictionary.

myDict = {}

sentence = input("Enter any sentence: ").lower()
words = sentence.split()

for word in words:
  if word not in myDict:
    myDict.update({word : 1})
  else:
    myDict[word] += 1
print(myDict)


# 17. Merge two dictionaries together.
myDict1 = {
  "a": 12,
  "b" : 12
}

myDict2 = {
  "c": 12,
  "a": 1
}

myDict1.update(myDict2)

print(myDict1)
# 18. Create a dictionary of students and their grades, then find the student with the highest grade.

students = {
  "bishal" : 3.81, 
  "ruby" : 3.34,
  "sudip" : 3.67,
  "bibek" : 3.71
}

gpa = list(students.values())
maxGpa = max(gpa)

for student in students:
  if (students[student]) == maxGpa:
    print(f"{student} has the highest gpa which is {maxGpa}")