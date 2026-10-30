# Program to check whether a string is a palindrome

string = input("Enter a string: ")

reverse = ""

for ch in string:
    reverse = ch + reverse

if string == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
