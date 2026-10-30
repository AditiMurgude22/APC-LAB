# Read a file and create another file with uppercase text

file = open("student.txt", "r")

content = file.read()

file.close()

uppercase_content = content.upper()

new_file = open("uppercase.txt", "w")

new_file.write(uppercase_content)

new_file.close()

print("Uppercase file created successfully.")