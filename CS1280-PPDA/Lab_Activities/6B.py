import numpy as np

# Creating matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:\n", A)
print("Matrix B:\n", B)

# Matrix addition
C = A + B
print("\nMatrix Addition (A + B):\n", C)

# Matrix subtraction
D = A - B
print("\nMatrix Subtraction (A - B):\n", D)

# Matrix multiplication (element-wise)
E = A * B
print("\nElement-wise Multiplication (A * B):\n", E)

# Matrix dot product
F = np.dot(A, B)
print("\nMatrix Dot Product (A @ B):\n", F)

# Matrix transpose
G = A.T
print("\nTranspose of A:\n", G)

# Determinant of a matrix
det_A = np.linalg.det(A)
print("\nDeterminant of A:", det_A)

# Inverse of a matrix
if det_A != 0:
    inv_A = np.linalg.inv(A)
    print("\nInverse of A:\n", inv_A)
else:
    print("\nMatrix A is singular and cannot be inverted.")

