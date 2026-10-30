# Program to count uppercase and lowercase letters

string = input("Enter a string: ")

upper = lower = 0

for ch in string:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
