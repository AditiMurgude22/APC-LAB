import matplotlib.pyplot as plt

subjects = ["Python", "Java", "AI", "Cloud"]
marks = [80, 70, 90, 60]

plt.pie(marks, labels=subjects, autopct="%1.1f%%")
plt.title("Marks Distribution")
plt.show()