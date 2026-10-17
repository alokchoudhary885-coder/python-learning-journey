# Chapter 4: Standard Library Demo — math Module
# ==================================================
# The 'math' module provides access to mathematical functions defined by the C standard.
# It is a built-in standard module (no 'pip install' needed).

import math

print("--- 1. Mathematical Constants ---")
print("Value of pi (pi):", math.pi)
print("Value of Euler's number (e):", math.e)

print("\n--- 2. Common Arithmetic & Power Functions ---")
number = 16
print(f"Square root of {number} (math.sqrt):", math.sqrt(number))
print("2 raised to power 5 (math.pow)    :", math.pow(2, 5))

print("\n--- 3. Rounding Functions ---")
decimal_val = 4.3
print(f"Original value:", decimal_val)
print("Ceiling value (math.ceil) :", math.ceil(decimal_val))   # 5 (smallest integer >= 4.3)
print("Floor value (math.floor)   :", math.floor(decimal_val))  # 4 (largest integer <= 4.3)

print("\n--- 4. Factorial and Absolute Values ---")
print("Factorial of 6 (math.factorial):", math.factorial(6))
print("Absolute value of -45.7 (math.fabs):", math.fabs(-45.7))

print("\n--- 5. Greatest Common Divisor (GCD) ---")
a, b = 48, 64
print(f"GCD of {a} and {b} (math.gcd):", math.gcd(a, b))

print("\n--- 6. Trigonometric Functions ---")
# Trigonometric functions take angles in radians
angle_degrees = 90
angle_radians = math.radians(angle_degrees)
print(f"sin({angle_degrees} degrees):", math.sin(angle_radians))
