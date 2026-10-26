# NumPy Fundamentals & Array Creation Routines

## 1. Definition
**NumPy** (Numerical Python) is the foundational open-source library for scientific computing and data science in Python. It introduces the high-performance **`ndarray`** (N-dimensional array) object and comprehensive mathematical functions optimized in C/Fortran.

## 2. Why We Use NumPy (Importance & Uses)
1. **Speed & Performance:** Up to 10x-50x faster than standard Python loops due to C-level vectorization.
2. **Contiguous Memory:** Arrays store homogeneous elements contiguously in memory, enabling hardware-level CPU cache optimization.
3. **Core of Modern AI & ML:** Libraries like Pandas, SciPy, Scikit-learn, PyTorch, and TensorFlow build directly on top of NumPy arrays.
4. **Convenient Mathematical Syntax:** Perform operations across millions of numbers with clean expressions (`arr * 2`) instead of multi-line loops.

## 3. Syntax of Core Creation Functions
```python
import numpy as np

# From Python sequence
arr = np.array([1, 2, 3])

# Zeros and Ones
zeros = np.zeros(shape, dtype=float)
ones = np.ones(shape, dtype=float)

# Range and Spacing
r = np.arange(start, stop, step)
lin = np.linspace(start, stop, num)
log = np.logspace(start, stop, num, base=10.0)
```

## 4. Simple Explanation: `arange()` vs `linspace()` vs `logspace()`
- **`np.arange(start, stop, step)`:** You specify the **step size** between numbers. May exclude the endpoint (like Python's `range`).
- **`np.linspace(start, stop, num)`:** You specify the **total count of points (`num`)** you want. The endpoint is **included** by default, and NumPy calculates the step size automatically.
- **`np.logspace(start, stop, num, base)`:** Spaced logarithmically (powers of `base`). `np.logspace(1, 3, 3)` produces $[10^1, 10^2, 10^3] = [10, 100, 1000]$.

## 5. Practical Example
```python
import numpy as np

# Generating sensor sample timestamps over 1 second with 10 intervals
timestamps = np.linspace(0.0, 1.0, 11)
print("Sensor timestamps:", timestamps)

# Binary mask array initialized to zeros
flags = np.zeros(5, dtype=int)
flags[2] = 1
print("Mask array       :", flags)
```

## 6. Expected Output
```text
Sensor timestamps: [0.  0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 1. ]
Mask array       : [0 0 1 0 0]
```

## 7. Important Differences: Python List vs NumPy Array
| Feature | Python List | NumPy `ndarray` |
|---|---|---|
| **Data Types** | Heterogeneous (can mix types) | Homogeneous (single type for all elements) |
| **Memory Storage** | Array of pointers to Python objects | Contiguous block of raw C memory bytes |
| **Arithmetic Operations** | Concatenation (`[1] + [2] = [1, 2]`) | Element-wise vector addition (`[1] + [2] = [3]`) |
| **Execution Speed** | Slower (interpreted Python loop overhead) | Extremely fast (C/Fortran compiled speed) |

## 8. Common Mistakes
1. **Confusing List Addition with Vector Addition:** Writing `[1, 2] * 2` repeats the list `[1, 2, 1, 2]`, while `np.array([1, 2]) * 2` calculates `[2, 4]`.
2. **`linspace` Count Parameter:** Confusing step size with count. The third parameter of `linspace(start, stop, num)` is the number of samples, NOT the step interval.
3. **Floating Point Roundoff in `arange`:** Using floating-point steps in `arange` can cause inconsistent inclusion of the endpoint due to IEEE 754 precision; use `linspace` instead when working with floats.

## 9. Short Revision Notes
- Always alias as `import numpy as np`.
- `np.zeros(n)` creates an array of zeros.
- `np.ones(n)` creates an array of ones.
- `np.arange()` = step-based range (supports floats).
- `np.linspace()` = count-based linear interpolation (ideal for plotting curves).
- `np.logspace()` = logarithmic geometric series.

## 10. Practice Questions with Answers

### Q1. How do you create an array of 8 zeros with integer data type?
**Answer:**
```python
import numpy as np
arr = np.zeros(8, dtype=int)
```

### Q2. How do you generate 10 evenly spaced values between 0 and 1 inclusive?
**Answer:**
```python
import numpy as np
vals = np.linspace(0, 1, 10)
```

### Q3. What is the difference between `np.arange(0, 10, 2)` and `np.linspace(0, 10, 5)`?
**Answer:** `np.arange(0, 10, 2)` produces `[0, 2, 4, 6, 8]` (step size 2, stop 10 excluded). `np.linspace(0, 10, 5)` produces `[0.0, 2.5, 5.0, 7.5, 10.0]` (5 total points, 10 included).

### Q4. What does `np.logspace(0, 3, 4, base=10)` return?
**Answer:** `[1., 10., 100., 1000.]` (representing $10^0, 10^1, 10^2, 10^3$).

### Q5. Why is a NumPy array faster than a Python list for numerical computations?
**Answer:** Because NumPy arrays are stored in contiguous blocks of memory and operations are executed in pre-compiled C loops without the overhead of Python dynamic type checking.
