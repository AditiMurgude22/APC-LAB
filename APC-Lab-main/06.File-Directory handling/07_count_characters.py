# Count total characters including spaces

file = open("student.txt", "r")

content = file.read()

count = len(content)

print("Total number of characters:", count)

file.close()