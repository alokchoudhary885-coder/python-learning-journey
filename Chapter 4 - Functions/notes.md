# Chapter 4 - Functions & Recursion

## 1. Definition
A function is a reusable block of code designed to perform a specific task. Recursion is a programming technique where a function calls itself directly or indirectly to solve a problem by breaking it into smaller sub-problems.

## 2. Syntax
```python
# Function definition
def function_name(parameter1, parameter2):
    # Code block
    return result

# Calling a function
value = function_name(arg1, arg2)

# Recursive function structure
def recursive_function(n):
    if base_condition:      # Base case
        return stop_value
    return n * recursive_function(n - 1)  # Recursive case
```

## 3. Example
```python
import math

# Basic function
def multiply(a, b):
    return a * b

# Recursive function for factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Product:", multiply(4, 5))
print("Factorial of 5:", factorial(5))
print("Built-in math.factorial(5):", math.factorial(5))
```

## 4. Output
```text
Product: 20
Factorial of 5: 120
Built-in math.factorial(5): 120
```

## 5. Explanation
### Understanding the Recursive Factorial Implementation
1. **Base Case (`n == 0` or `n == 1`)**:
   - The condition that stops the recursion. Without it, the function calls itself indefinitely until Python reaches its recursion limit.
   - For `n = 0` or `n = 1`, it immediately returns `1`.

2. **Recursive Case (`n * factorial(n - 1)`)**:
   - The function calls itself with a smaller input (`n - 1`), reducing the original problem.

3. **Function Call Stack (Winding Phase)**:
   - `factorial(5)` calls `5 * factorial(4)`
   - `factorial(4)` calls `4 * factorial(3)`
   - `factorial(3)` calls `3 * factorial(2)`
   - `factorial(2)` calls `2 * factorial(1)`
   - `factorial(1)` hits the base case and returns `1`.

4. **Return Values (Unwinding Phase)**:
   - `factorial(1)` returns `1`
   - `factorial(2)` returns `2 * 1 = 2`
   - `factorial(3)` returns `3 * 2 = 6`
   - `factorial(4)` returns `4 * 6 = 24`
   - `factorial(5)` returns `5 * 24 = 120`

5. **Recursive Implementation vs `math.factorial()`**:
   - Our recursive implementation teaches how function call stacks and call frames work in memory.
   - `math.factorial()` is implemented internally in C. It uses an iterative or divide-and-conquer algorithm that avoids Python call-stack overhead and handles huge numbers much faster without hitting Python's recursion limit.

## 6. Important Points
- Functions improve code reusability and modularity.
- `return` sends a value back to the caller and terminates the function execution immediately.
- `*args` collects positional arguments into a tuple; `**kwargs` collects keyword arguments into a dictionary.
- Every recursive function MUST have at least one reachable base case.
- Python has a default recursion limit (typically 1000 frames) to prevent stack overflows.

## 7. Common Mistakes
- Omitting the base case, causing `RecursionError: maximum recursion depth exceeded`.
- Forgetting to write `return` in front of the recursive call.
- Accidentally importing `result` from `unittest` (a common IDE auto-complete mistake).
- Writing dead code after a `return` statement.
- Assigning a call result to a variable sharing the function name inside itself (e.g. `f = f(10)` inside `f`), causing `UnboundLocalError`.

## 8. Practice Questions
1. Write a function that takes two numbers and returns the larger one.
2. Write a recursive function to calculate the sum of numbers from 1 to $n$.
3. Write a function that accepts `**kwargs` and prints all keys and values in alphabetical order.
4. What error occurs when a recursive function has no base case?
5. Write a recursive function `fibonacci(n)` that returns the $n$-th Fibonacci number.
