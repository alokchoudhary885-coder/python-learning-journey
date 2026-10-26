# 2D Arrays, Dimensions & Shapes in NumPy

## 1. Definition
A **2D array** in NumPy is a grid of values indexed by two coordinates: a row index and a column index. It is commonly referred to as a **matrix**. The structure of an array is defined by its **`.shape`** (a tuple describing the size of each dimension) and its **`.ndim`** (number of dimensions).

## 2. Why We Use 2D Arrays & Shapes
- **Tabular Data Representation:** Rows represent samples/records, while columns represent features (standard format in Data Science and Machine Learning).
- **Matrix Mathematics:** Enables linear algebra operations like dot products, matrix inversions, and eigenvectors.
- **Image Processing:** Grayscale images are represented directly as 2D NumPy arrays of pixel intensities.

## 3. Syntax Reference
```python
import numpy as np

# Creating 2D array from nested lists
matrix = np.array([[1, 2, 3], [4, 5, 6]])

# Built-in 2D creation
zeros_matrix = np.zeros((rows, cols))
identity = np.eye(n)

# Shape and dimensions
print(matrix.shape)   # (rows, cols)
print(matrix.ndim)    # 2

# Reshaping
reshaped = arr.reshape(new_rows, new_cols)

# Slicing: [row_slice, col_slice]
sub = matrix[0:2, 1:3]
```

## 4. Simple Explanation: Understanding `axis=0` vs `axis=1`
In a 2D array:
- **`axis=0` (Vertical / Columns):** Collapses rows to compute column-wise statistics. For example, `arr.sum(axis=0)` gives the sum of each column.
- **`axis=1` (Horizontal / Rows):** Collapses columns to compute row-wise statistics. For example, `arr.sum(axis=1)` gives the sum of each row.

```text
       axis=1 (across columns -> row operation)
         ───────>
axis=0 ┌───┬───┬───┐
  │    │ 1 │ 2 │ 3 │
  │    ├───┼───┼───┤
  v    │ 4 │ 5 │ 6 │
(down) └───┴───┴───┘
```

## 5. Practical Example
```python
import numpy as np

# Student exam scores: 3 students across 4 subjects
scores = np.array([
    [78, 85, 92, 88],  # Student 1
    [65, 72, 80, 75],  # Student 2
    [90, 95, 89, 94]   # Student 3
])

print("Shape (Students, Subjects):", scores.shape)
print("Average per student (axis=1):", scores.mean(axis=1))
print("Subject highest score (axis=0):", scores.max(axis=0))
```

## 6. Expected Output
```text
Shape (Students, Subjects): (3, 4)
Average per student (axis=1): [85.75 73.   92.  ]
Subject highest score (axis=0): [90 95 92 94]
```

## 7. Important Differences: `*` vs `@` Operator
| Operation | Syntax | Meaning | Requirement |
|---|---|---|---|
| **Element-wise Multiplication** | `A * B` | Multiplies matching indices $(A_{ij} \times B_{ij})$ | Same shape or broadcastable |
| **Matrix Multiplication (Dot Product)** | `A @ B` or `np.dot(A, B)` | Linear algebra dot product (row $\times$ col) | $A$'s columns must equal $B$'s rows |

## 8. Common Mistakes
1. **Reshape Dimension Mismatch:** Attempting `np.arange(10).reshape(3, 3)` raises `ValueError: cannot reshape array of size 10 into shape (3,3)` because $3 \times 3 = 9 \ne 10$.
2. **Missing Tuple in `zeros`/`ones`:** Writing `np.zeros(3, 4)` raises `TypeError` because NumPy expects `shape` as a tuple: `np.zeros((3, 4))`.
3. **Confusing Python 2D indexing:** In native Python lists, you write `list[0][1]`. In NumPy, the preferred, faster syntax is `arr[0, 1]`.

## 9. Short Revision Notes
- `.shape` returns `(rows, cols)` for 2D arrays.
- `.ndim` is 2 for matrices, 1 for vectors.
- `.size` is total count of elements ($rows \times cols$).
- Slicing syntax: `array[row_start:row_stop, col_start:col_stop]`.
- Matrix dot product is written using `@` operator in modern Python.

## 10. Practice Questions with Answers

### Q1. How do you create a $4 \times 5$ matrix filled entirely with ones?
**Answer:**
```python
import numpy as np
matrix = np.ones((4, 5))
```

### Q2. Given `arr = np.arange(16)`, how do you reshape it into a $4 \times 4$ matrix?
**Answer:**
```python
matrix_4x4 = arr.reshape(4, 4)
```

### Q3. How do you extract only the third column from a 2D array `matrix`?
**Answer:**
```python
col_3 = matrix[:, 2]
```

### Q4. Given `data = np.array([[10, 20], [30, 40]])`, what is `data.sum(axis=0)`?
**Answer:** `np.array([40, 60])` (sum of first column $10+30=40$, second column $20+40=60$).

### Q5. What is the difference between `A * B` and `A @ B` for two square matrices?
**Answer:** `A * B` performs element-wise multiplication, multiplying corresponding elements. `A @ B` computes the matrix product (linear algebra row-by-column dot product).
