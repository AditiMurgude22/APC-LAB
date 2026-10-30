import matplotlib.pyplot as plt

subjects = ["Python", "Java", "AI", "Cloud"]
marks = [80, 70, 90, 85]

plt.barh(subjects, marks)
plt.title("Subject Marks")
plt.xlabel("Marks")
plt.ylabel("Subjects")
plt.show()