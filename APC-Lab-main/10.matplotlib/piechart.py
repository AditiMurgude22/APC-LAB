import matplotlib.pyplot as plt
subjects=["maths","science","english","hindi","social"]
marks=[85,87,91,85,99]
plt.pie(marks,labels=subjects, autopct="%1.1f%%")
plt.title("subject marks")
plt.show()