# PROGRAM 3: MATRIX OPERATIONS USING NUMPY

import numpy as np

A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("MATRIX A:")
print(A)

print("\nMATRIX B:")
print(B)

# Matrix Addition
print("\nMATRIX ADDITION:")
print(A + B)

# Matrix Subtraction
print("\nMATRIX SUBTRACTION:")
print(A - B)

# Matrix Multiplication
print("\nMATRIX MULTIPLICATION:")
print(np.dot(A, B))

# Transpose
print("\nTRANSPOSE OF MATRIX A:")
print(A.T)

# Determinant
print("\nDETERMINANT OF MATRIX A:")
print(np.linalg.det(A))

# Inverse
print("\nINVERSE OF MATRIX A:")
print(np.linalg.inv(A))