import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y1 = [10, 20, 30, 40, 50]
y2 = [5, 15, 25, 35, 45]

plt.plot(x, y1, label="Line 1")
plt.plot(x, y2, label="Line 2")

plt.title("Multiple Line Plot")
plt.xlabel("X-axis")
plt.ylabel("Values")
plt.legend()
plt.show()