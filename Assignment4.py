
# a.
import numpy as np

# Create 4x4 identity matrix
identity_matrix = np.eye(4)

print("4x4 Identity Matrix:")
print(identity_matrix)

import numpy as np

#b. Generate two 3x3 matrices with random integers (1 to 9)
A = np.random.randint(1, 10, (3, 3))
B = np.random.randint(1, 10, (3, 3))

print("Matrix A:")
print(A)

print("Matrix B:")
print(B)

# Addition
addition = A + B
print("Addition of matrices:")
print(addition)

# Multiplication
multiplication = np.dot(A, B)
print("Multiplication of matrices:")
print(multiplication)



# 2 Matrix multipliaction
import numpy as np

print("Enter elements for 5x3 matrix:")
A = []
for i in range(5):
    row = list(map(int, input().split()))
    A.append(row)

print("Enter elements for 3x2 matrix:")
B = []
for i in range(3):
    row = list(map(int, input().split()))
    B.append(row)

A = np.array(A)
B = np.array(B)

# Multiply matrices
result = np.dot(A, B)

print("Product Matrix (5x3 * 3x2):")
print(result)