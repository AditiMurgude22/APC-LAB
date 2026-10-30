# Program to replace all occurrences of a character

string = input("Enter a string: ")
old = input("Enter the character to replace: ")
new = input("Enter the new character: ")

result = ""

for ch in string:
    if ch == old:
        result += new
    else:
        result += ch

print("Updated string:", result)
