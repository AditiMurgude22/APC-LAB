# Remove single-line comments from a Python file

input_file = open("program.py", "r")
output_file = open("program_without_comments.py", "w")

for line in input_file:
    if not line.strip().startswith("#"):
        output_file.write(line)

input_file.close()
output_file.close()

print("Comments removed successfully.")