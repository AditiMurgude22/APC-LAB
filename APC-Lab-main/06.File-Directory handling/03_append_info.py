# Append additional information to an existing file

file = open("student.txt", "a")

file.write("College: ABC College\n")
file.write("Division: A\n")

file.close()

print("Additional information appended successfully.")
