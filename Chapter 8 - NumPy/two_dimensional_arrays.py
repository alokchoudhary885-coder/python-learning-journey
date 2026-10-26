# Chapter 8: 2D Arrays (Matrices) and Shapes in NumPy
# Demonstrates 2D array creation, shape inspection, slicing, axis operations, and reshaping.

import numpy as np

# 1. Creating 2D Arrays (Matrices)
# From nested Python lists:
matrix_a = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

# Using built-in creation functions with tuple shapes:
zeros_2d = np.zeros((3, 4), dtype=int)
ones_2d = np.ones((2, 3))
identity_matrix = np.eye(3)  # 3x3 Identity matrix

print("--- 1. Creating 2D Arrays ---")
print("Matrix A (2x3):\n", matrix_a)
print("Zeros 2D (3x4):\n", zeros_2d)
print("Identity Matrix (3x3):\n", identity_matrix)

# 2. Inspecting Array Attributes
print("\n--- 2. Key Attributes ---")
print("matrix_a.shape :", matrix_a.shape)   # (2, 3) -> 2 rows, 3 columns
print("matrix_a.ndim  :", matrix_a.ndim)    # 2 (dimensions)
print("matrix_a.size  :", matrix_a.size)    # 6 (total elements)
print("matrix_a.dtype :", matrix_a.dtype)   # int32 or int64

# 3. Reshaping Arrays (.reshape)
# Total elements must remain identical: 12 elements -> (3, 4) or (2, 6) or (4, 3)
linear_12 = np.arange(1, 13)
reshaped_3x4 = linear_12.reshape(3, 4)
reshaped_2x6 = linear_12.reshape(2, 6)

print("\n--- 3. Reshaping Arrays ---")
print("Original 1D (12 elements)    :", linear_12)
print("Reshaped to 3x4:\n", reshaped_3x4)
print("Reshaped to 2x6:\n", reshaped_2x6)

# 4. 2D Indexing and Slicing [row, col]
print("\n--- 4. 2D Slicing and Indexing ---")
data = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("Sample Data Matrix (3x4):\n", data)
print("Element at row 1, col 2 (data[1, 2]):", data[1, 2])
print("Entire first row (data[0, :])       :", data[0, :])
print("Entire second column (data[:, 1])    :", data[:, 1])
print("Sub-matrix (top 2 rows, left 2 cols):\n", data[0:2, 0:2])

# 5. Axis Operations (axis=0 for columns, axis=1 for rows)
print("\n--- 5. Axis Operations ---")
print("Total sum of all elements :", data.sum())
print("Column-wise sums (axis=0) :", data.sum(axis=0))
print("Row-wise sums (axis=1)    :", data.sum(axis=1))
print("Row-wise means (axis=1)   :", data.mean(axis=1))

# 6. Matrix Multiplication (Dot Product)
m1 = np.array([[1, 2], [3, 4]])
m2 = np.array([[5, 6], [7, 8]])

# Element-wise multiplication vs Matrix dot product:
element_wise = m1 * m2
matrix_product = m1 @ m2  # Or np.dot(m1, m2)

print("\n--- 6. Matrix Operations ---")
print("Element-wise multiplication (m1 * m2):\n", element_wise)
print("Matrix Dot Product (m1 @ m2):\n", matrix_product)
