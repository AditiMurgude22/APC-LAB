# Program to reverse a string without using built-in reverse functions

string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

print("Reversed string:", reverse)
