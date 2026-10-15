import re

phone = input("Enter phone number: ")

pattern = r'^[0-9]{10}$'

if re.match(pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")