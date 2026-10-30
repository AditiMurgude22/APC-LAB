attendance = {
    "Monday": {"Amit", "Rahul", "Suhana", "Priya"},
    "Tuesday": {"Rahul", "Suhana", "Priya"},
    "Wednesday": {"Amit", "Rahul", "Suhana"},
    "Thursday": {"Rahul", "Suhana", "Priya"},
    "Friday": {"Rahul", "Suhana"}
}

# Students attending all classes
all_days = set.intersection(*attendance.values())

print("Students who attended all classes:")
print(all_days)

# Count attendance of each student
attendance_count = {}

for students in attendance.values():
    for student in students:
        attendance_count[student] = attendance_count.get(student, 0) + 1

# Students attending only one class
only_one = set()

for student, count in attendance_count.items():
    if count == 1:
        only_one.add(student)

print("Students who attended only one class:")
print(only_one)

# Total unique students
unique_students = set.union(*attendance.values())

print("Total unique students:", len(unique_students))
print("Students:", unique_students)
