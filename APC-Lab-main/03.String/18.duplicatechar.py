# Program to remove duplicate characters while maintaining order

string = input("Enter a string: ")

result = ""

for ch in string:
    if ch not in result:
        result += ch

print("String after removing duplicates:", result)
