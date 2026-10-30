project1 = {"Amit", "Rahul", "Suhana", "Priya"}
project2 = {"Rahul", "Priya", "Neha", "Karan"}

# Intersection
print("Employees working on both projects:")
print(project1.intersection(project2))

# Difference
print("Employees only in Project 1:")
print(project1.difference(project2))

print("Employees only in Project 2:")
print(project2.difference(project1))

# Union
print("Total unique employees:")
print(project1.union(project2))
