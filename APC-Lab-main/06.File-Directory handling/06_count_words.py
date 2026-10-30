# Count the total number of words in a file

file = open("student.txt", "r")

content = file.read()

words = content.split()

count = len(words)

print("Total number of words:", count)

file.close()