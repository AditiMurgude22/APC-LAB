def character_frequency(text, ignore_case):
    if ignore_case:
        text = text.lower()

    frequency = {}

    for char in text:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1

    # Sort by frequency in descending order
    sorted_frequency = sorted(
        frequency.items(),
        key=lambda x: x[1],
        reverse=True
    )

    return sorted_frequency


text = input("Enter a string: ")

choice = input("Ignore case? (yes/no): ")

if choice.lower() == "yes":
    result = character_frequency(text, True)
else:
    result = character_frequency(text, False)

print("Character frequencies:")

for char, count in result:
    if char == " ":
        print("'space':", count)
    else:
        print(char, ":", count)
