import math

x = float(input("Enter x (in radians): "))
n = int(input("Enter number of terms: "))

sum = 0

for i in range(n):
    term = ((-1) ** i) * (x ** (2 * i)) / math.factorial(2 * i)
    sum += term

print("cos(x) =", sum)
