# Program to find the length of a string without using len()

string = input("Enter a string: ")

count = 0
for ch in string:
    count += 1

print("Length of the string is:", count)
