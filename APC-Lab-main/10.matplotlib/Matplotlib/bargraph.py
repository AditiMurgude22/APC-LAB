import matplotlib.pyplot as plt

subjects = ["Python", "Java", "AI", "Cloud"]
marks = [80, 70, 90, 85]

plt.bar(subjects, marks)
plt.title("Student Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")
plt.show()