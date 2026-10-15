import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Student": ["Aarav", "Aditi", "Kabir", "Meera", "Ishaan"],
    "Python": [78, 92, 85, 88, 73],
    "Statistics": [82, 89, 80, 94, 76],
    "Visualization": [85, 95, 88, 91, 79]
}
df = pd.DataFrame(data)
subjects = ["Python", "Statistics", "Visualization"]
df["Average"] = df[subjects].mean(axis=1).round(1)

print(df[["Student", "Average"]])
df.plot(x="Student", y="Average", kind="bar", legend=False)
plt.ylabel("Average score (%)")
plt.title("Average Score by Student")
plt.tight_layout()
plt.show()