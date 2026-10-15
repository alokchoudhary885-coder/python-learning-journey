# Recursion in Python: Factorial Implementation
# Migrated and improved from Python 167/recursion.py

import math


def factorial(n):
    """
    Calculate the factorial of a non-negative integer using recursion.
    
    Base Case:
        When n == 0 or n == 1, return 1 (stops recursion).
        
    Recursive Case:
        When n > 1, return n * factorial(n - 1) (calls itself with smaller input).
    """
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


if __name__ == "__main__":
    number = 5

    # 1. Recursive Factorial Calculation
    result = factorial(number)
    print(f"Factorial of {number} using recursion: {result}")

    # 2. Formula Expansion Visualization
    formula = " * ".join(str(i) for i in range(number, 0, -1))
    print(f"Step-by-step expansion: {formula} = {result}")

    # 3. Comparison with Python's Built-in math.factorial()
    # Built-in math.factorial() is implemented in C and optimized for speed and large integers.
    built_in_result = math.factorial(number)
    print(f"Factorial of {number} using math.factorial(): {built_in_result}")

    # Verify both approaches give identical results
    assert result == built_in_result, "Results should match!"
    print("Verification: Both recursive and math.factorial() outputs match successfully.")
