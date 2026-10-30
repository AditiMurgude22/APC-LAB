# Count alphabets, digits, spaces and special characters

file = open("student.txt", "r")

content = file.read()

alphabets = 0
digits = 0
spaces = 0
special_characters = 0

for ch in content:
    if ch.isalpha():
        alphabets += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1
    elif ch != "\n":
        special_characters += 1

print("Total alphabets:", alphabets)
print("Total digits:", digits)
print("Total spaces:", spaces)
print("Total special characters:", special_characters)

file.close()