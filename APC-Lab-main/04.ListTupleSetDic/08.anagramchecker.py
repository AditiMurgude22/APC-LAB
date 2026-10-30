import string

def normalize(text):
    result = ""

    for char in text.lower():
        if char.isalnum():
            result += char

    return result

def are_anagrams(str1, str2):
    str1 = normalize(str1)
    str2 = normalize(str2)

    return sorted(str1) == sorted(str2)


s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

if are_anagrams(s1, s2):
    print("The strings are anagrams")
else:
    print("The strings are not anagrams")
