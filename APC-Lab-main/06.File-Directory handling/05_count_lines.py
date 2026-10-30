# Count the number of lines in a file

file = open("student.txt", "r")

lines = file.readlines()

count = len(lines)

print("Total number of lines:", count)

file.close()