students = []
grades = []

def add_student(name, grade):
    students.append(name)
    grades.append(grade)

def update_grade(name, grade):
    if name in students:
        index = students.index(name)
        grades[index] = grade
    else:
        print("Student not found")

def remove_student(name):
    if name in students:
        index = students.index(name)
        students.pop(index)
        grades.pop(index)
    else:
        print("Student not found")

def average_grade():
    if grades:
        print("Average Grade:", sum(grades) / len(grades))
    else:
        print("No grades available")

def extreme_grades():
    if grades:
        print("Highest Grade:", max(grades))
        print("Lowest Grade:", min(grades))
    else:
        print("No grades available")


add_student("Suhana", 90)
add_student("Aisha", 85)
add_student("Rahul", 78)

update_grade("Rahul", 82)
remove_student("Aisha")

print("Students:", students)
print("Grades:", grades)

average_grade()
extreme_grades()
