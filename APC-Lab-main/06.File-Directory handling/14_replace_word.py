# Replace a word in a file

file = open("student.txt", "r")

content = file.read()

file.close()

old_word = input("Enter word to replace: ")
new_word = input("Enter new word: ")

modified_content = content.replace(old_word, new_word)

file = open("student.txt", "w")

file.write(modified_content)

file.close()

print("Word replaced successfully.")