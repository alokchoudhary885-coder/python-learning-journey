# Chapter 4 - Functions, Variable Scope & Recursion

## 1. Definition
A **function** is a reusable block of code that performs a specific action and optionally returns a result. A **local variable** is defined inside a function and can only be accessed within that function. A **global variable** is defined outside all functions and is accessible throughout the module. **Recursion** is a technique where a function calls itself to solve smaller sub-problems until reaching a base condition.

## 2. Syntax
```python
# Global variable
global_var = 100

def my_function():
    # Local variable
    local_var = 20
    
    # Modifying a global variable
    global global_var
    global_var += 50
    return local_var

# Recursive function
def recursive_func(n):
    if n <= 1:              # Base case
        return 1
    return n * recursive_func(n - 1)  # Recursive case
```

## 3. Example
```python
import math

# Global variable
counter = 10

def process_data(value):
    # Local variable
    factor = 2
    global counter
    counter += 1
    return value * factor

# Recursive factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print("Result:", process_data(5))
print("Updated Global counter:", counter)
print("Factorial of 5:", factorial(5))
print("Built-in math.factorial(5):", math.factorial(5))
```

## 4. Output
```text
Result: 10
Updated Global counter: 11
Factorial of 5: 120
Built-in math.factorial(5): 120
```

## 5. Explanation
### Local vs Global Scope
- **Local Scope:** Variables created inside a function (like `factor`) are stored in the function's local namespace. When the function finishes execution, these variables are destroyed from memory.
- **Global Scope:** Variables declared outside functions (like `counter`) live at module level and are accessible anywhere in the script for reading.
- **The `global` Keyword:** In Python, assigning a value inside a function automatically creates a local variable by default. To modify a module-level variable inside a function, you must declare it with `global variable_name`.

### Understanding the Recursive Factorial Implementation
1. **Base Case (`n == 0` or `n == 1`)**:
   - The condition that stops recursion. It prevents infinite calls and stack overflow.
   - Returns `1` immediately.
2. **Recursive Case (`n * factorial(n - 1)`)**:
   - Reduces the problem by calling `factorial` with `n - 1`.
3. **Function Call Stack (Winding & Unwinding)**:
   - Call frames are pushed: `5 * fact(4) -> 4 * fact(3) -> 3 * fact(2) -> 2 * fact(1)`.
   - Base case returns `1`, and frames unwind: `1 -> 2 -> 6 -> 24 -> 120`.
4. **Recursive vs `math.factorial()`**:
   - Our recursive function demonstrates call stack mechanics and recursion theory.
   - `math.factorial()` is written in C and avoids call stack overhead, making it faster and free from Python recursion limits.

## 6. Important Points
- **LEGB Rule:** Python searches for variable names in order: **L**ocal -> **E**nclosing -> **G**lobal -> **B**uilt-in.
- Accessing a local variable outside its function raises a `NameError`.
- Reading a global variable inside a function does NOT require the `global` keyword; modifying it DOES.
- Best practice: Prefer returning values and passing parameters over modifying global state directly.
- Every recursive function must have at least one reachable base case to prevent a `RecursionError`.

## 7. Common Mistakes
- **`UnboundLocalError`:** Occurs when you read and assign a global variable inside a function without declaring `global` first:
  ```python
  count = 0
  def increment():
      count += 1  # Raises UnboundLocalError! Fix: add 'global count'
  ```
- **Accessing Local Variable Outside:** Trying to print a variable declared inside a function from global scope raises `NameError`.
- **Variable Shadowing Confusion:** Creating a local variable with the same name as a global variable overrides access to the global variable inside that function without warning.
- **Missing Base Case:** A recursive function without a base case runs until hitting Python's recursion limit (default 1000).

## 8. Practice Questions
1. What will be the output of this code?
   ```python
   x = 5
   def change():
       x = 10
   change()
   print(x)
   ```
2. Write a function with a local variable `pi = 3.14` to calculate the area of a circle.
3. How can you modify a global variable `score = 0` inside a function `update_score(points)`? Write the code.
4. What is the difference between reading a global variable and modifying a global variable inside a function?
5. What error occurs if you try to print a local variable outside its function? Explain why.
