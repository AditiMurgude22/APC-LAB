import matplotlib.pyplot as plt
marks=[20,30,40,50,60,70,80]
plt.hist(marks, bins=5)
plt.title("marks distribution")
plt.xlabel("marks")
plt.ylabel("frequency")
plt.show()