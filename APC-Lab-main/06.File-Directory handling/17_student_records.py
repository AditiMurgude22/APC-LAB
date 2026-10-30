# Student record management

file = open("students.txt", "w")

file.write("RollNo,Name,Marks\n")
file.write("101,Amit,85\n")
file.write("102,Priya,92\n")
file.write("103,Rahul,78\n")

file.close()

# Read the records
file = open("students.txt", "r")

lines = file.readlines()

file.close()

students = []

for line in lines[1:]:
    roll_no, name, marks = line.strip().split(",")

    student = {
        "roll_no": roll_no,
        "name": name,
        "marks": int(marks)
    }

    students.append(student)

# Display all records
print("All Student Records:")

for student in students:
    print(student)

# Find student with highest marks
highest = max(students, key=lambda x: x["marks"])

print("\nStudent with highest marks:")
print(highest["name"], "-", highest["marks"])

# Calculate average marks
total = sum(student["marks"] for student in students)

average = total / len(students)

print("\nAverage marks:", average)

# Display students scoring more than 80
print("\nStudents scoring more than 80:")

for student in students:
    if student["marks"] > 80:
        print(student["name"], "-", student["marks"])