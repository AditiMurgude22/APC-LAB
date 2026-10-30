# Count the frequency of each word

file = open("student.txt", "r")

content = file.read()

words = content.lower().split()

word_count = {}

for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print("Word frequency:")

for word, count in word_count.items():
    print(word, ":", count)

file.close()