# Chapter 8: NumPy Fundamentals & Core Benefits
# Demonstrates NumPy array creation, type homogeneity, and performance comparison with Python lists.

import time
import numpy as np

# 1. Creating Basic NumPy Arrays
python_list = [10, 20, 30, 40, 50]
numpy_array = np.array(python_list)

print("--- 1. Python List vs NumPy Array ---")
print("Python List :", python_list, "| Type:", type(python_list))
print("NumPy Array :", numpy_array, "| Type:", type(numpy_array))

# 2. Array Homogeneity and Data Types
# All elements in a NumPy array must share the same data type
float_array = np.array([1, 2, 3.5, 4])
int32_array = np.array([1, 2, 3, 4], dtype=np.int32)

print("\n--- 2. Data Types (dtype) ---")
print("Float array dtype:", float_array.dtype, "| Values:", float_array)
print("Int32 array dtype:", int32_array.dtype, "| Values:", int32_array)

# 3. Vectorization (Element-wise Operations without Loops)
# In Python lists: [x * 2 for x in python_list]
# In NumPy: numpy_array * 2 (executed in optimized C code)
doubled = numpy_array * 2
added = numpy_array + 100

print("\n--- 3. Vectorized Math ---")
print("Original   :", numpy_array)
print("Multiplied :", doubled)
print("Added 100  :", added)

# 4. Performance Benchmark: Python List vs NumPy Array
size = 1_000_000
list_a = list(range(size))
list_b = list(range(size))

start = time.perf_counter()
list_result = [a + b for a, b in zip(list_a, list_b)]
py_time = time.perf_counter() - start

arr_a = np.arange(size)
arr_b = np.arange(size)

start = time.perf_counter()
arr_result = arr_a + arr_b
np_time = time.perf_counter() - start

print("\n--- 4. Speed Benchmark (1 Million Elements Addition) ---")
print(f"Python list time : {py_time:.4f} seconds")
print(f"NumPy array time : {np_time:.4f} seconds")
print(f"NumPy is ~{py_time / np_time:.1f}x faster!")
