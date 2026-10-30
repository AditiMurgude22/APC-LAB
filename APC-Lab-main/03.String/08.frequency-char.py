# Program to count the frequency of a character

string = input("Enter a string: ")
character = input("Enter a character: ")

count = 0

for ch in string:
    if ch == character:
        count += 1

print("Frequency of", character, "is", count)
