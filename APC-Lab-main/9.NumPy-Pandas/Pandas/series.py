# PROGRAM 4: CREATE AND DISPLAY A PANDAS SERIES

import pandas as pd

# Creating a Series
marks = pd.Series([85, 90, 78, 92, 88])

print("PANDAS SERIES:")
print(marks)

# Accessing elements
print("\nFIRST ELEMENT:")
print(marks[0])

print("\nFIRST THREE ELEMENTS:")
print(marks[:3])

# Basic operations
print("\nMEAN:")
print(marks.mean())

print("\nMAXIMUM:")
print(marks.max())

print("\nMINIMUM:")
print(marks.min())