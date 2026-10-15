import re

text = input("Enter text: ")

pattern = r'^[a-zA-Z]+$'

if re.match(pattern, text):
    print("Valid input")
else:
    print("Invalid input")