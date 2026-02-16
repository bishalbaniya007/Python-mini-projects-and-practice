# 32. Write a program that takes a paragraph and creates a dictionary showing how many times each unique word appears.

paragrph = input("Enter the paragraph: ").lower()
wordsList = paragrph.split()


myDict = {}

for word in wordsList:
  if word in myDict:
    myDict[word] += 1
  else:
    myDict.update({word : 1})

print(myDict)