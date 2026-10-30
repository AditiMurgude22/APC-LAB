from collections import Counter

text = input("Enter a paragraph: ")

# Convert to lowercase and split into words
words = text.lower().split()

# Total number of words
print("Total number of words:", len(words))

# Word frequency
frequency = Counter(words)

print("Word frequencies:")
for word, count in frequency.items():
    print(word, ":", count)

# Top 3 frequent words
print("Top 3 most frequent words:")
for word, count in frequency.most_common(3):
    print(word, ":", count)

# Count vowels
vowels = "aeiou"
vowel_count = 0

for char in text.lower():
    if char in vowels:
        vowel_count += 1

print("Number of vowels:", vowel_count)
