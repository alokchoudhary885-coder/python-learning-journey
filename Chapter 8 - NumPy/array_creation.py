# Chapter 8: NumPy Array Creation Routines
# Demonstrates zeros, ones, arange, linspace, and logspace.

import numpy as np

# 1. np.zeros() - Arrays filled with zeros
zeros_1d = np.zeros(5)
zeros_int = np.zeros(4, dtype=int)

print("--- 1. np.zeros() ---")
print("zeros float (default):", zeros_1d)
print("zeros int            :", zeros_int)

# 2. np.ones() - Arrays filled with ones
ones_1d = np.ones(6)
ones_int = np.ones(5, dtype=int)

print("\n--- 2. np.ones() ---")
print("ones float :", ones_1d)
print("ones int   :", ones_int)

# 3. np.arange(start, stop, step)
# Unlike Python's range(), arange supports floating-point steps!
int_range = np.arange(1, 10, 2)
float_range = np.arange(0.0, 1.0, 0.2)

print("\n--- 3. np.arange() ---")
print("Integer step [1 to 10 by 2] :", int_range)
print("Float step [0.0 to 1.0 by 0.2]:", float_range)

# 4. np.linspace(start, stop, num)
# Returns evenly spaced numbers over a specified closed interval [start, stop]
linear_samples = np.linspace(0, 10, 5)
percentage_steps = np.linspace(0, 100, 11)

print("\n--- 4. np.linspace() (Linearly Spaced) ---")
print("5 points from 0 to 10   :", linear_samples)
print("11 points from 0 to 100 :", percentage_steps)

# 5. np.logspace(start, stop, num, base)
# Returns numbers spaced evenly on a logarithmic scale
# Formula: base ** val where val ranges from start to stop
log_base10 = np.logspace(1, 4, num=4)          # 10^1, 10^2, 10^3, 10^4
log_base2 = np.logspace(1, 5, num=5, base=2.0) # 2^1, 2^2, 2^3, 2^4, 2^5

print("\n--- 5. np.logspace() (Logarithmically Spaced) ---")
print("Base 10 [10^1 to 10^4] :", log_base10)
print("Base 2  [2^1 to 2^5]   :", log_base2)
