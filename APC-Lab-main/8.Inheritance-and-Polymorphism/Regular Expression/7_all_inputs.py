import re

email = input("Enter email: ")
phone = input("Enter phone number: ")
password = input("Enter password: ")
text = input("Enter characters: ")

email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_pattern = r'^[0-9]{10}$'
password_pattern = r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@#$%^&*!]).{8,}$'
text_pattern = r'^[a-zA-Z]+$'

if re.match(email_pattern, email):
    print("Valid email")
else:
    print("Invalid email")

if re.match(phone_pattern, phone):
    print("Valid phone number")
else:
    print("Invalid phone number")

if re.match(password_pattern, password):
    print("Valid password")
else:
    print("Invalid password")

if re.match(text_pattern, text):
    print("Valid text")
else:
    print("Invalid text")