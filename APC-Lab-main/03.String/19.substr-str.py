# Program to check whether a substring exists in a string

string = input("Enter the main string: ")
substring = input("Enter the substring: ")

if substring in string:
    print("Substring found.")
else:
    print("Substring not found.")
