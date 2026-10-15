# Program to display each character with its ASCII value

string = input("Enter a string: ")

for ch in string:
    print(ch, ":", ord(ch))
