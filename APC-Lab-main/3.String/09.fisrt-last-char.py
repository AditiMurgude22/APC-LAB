# Program to print the first and last character of a string

string = input("Enter a string: ")

if string:
    print("First character:", string[0])
    print("Last character:", string[-1])
else:
    print("The string is empty.")
