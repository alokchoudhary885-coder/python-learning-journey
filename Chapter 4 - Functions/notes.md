# Chapter 4 - Advanced Functions, Arguments & Functional Tools

## 1. Definition
Python functions are versatile first-class objects. Beyond basic declarations, Python supports flexible argument types (**positional, keyword, default, `*args`, `**kwargs`**), **function aliasing** (assigning function references to new names), and **nested functions** (inner functions inside outer scopes). A **ternary operator** evaluates conditions inline. **Lambda functions** are concise, single-expression anonymous functions, often used with higher-order functions like **`filter()`** to extract matching elements from an iterable.

## 2. Syntax
```python
# 1. Types of Arguments
def func(pos, default_val=10, *args, **kwargs):
    pass

# 2. Function Aliasing
new_alias = original_function

# 3. Nested Functions
def outer():
    def inner():
        return "Inside helper"
    return inner()

# 4. Ternary Operator
result = value_if_true if condition else value_if_false

# 5. Lambda Function
lambda arguments: single_expression

# 6. filter()
filtered_list = list(filter(lambda x: condition, iterable))
```

## 3. Example
```python
# 1. Types of arguments
def calculate_bill(base_price, tax_rate=0.05, *discounts, **customer):
    total = base_price + (base_price * tax_rate) - sum(discounts)
    return total

# 2. Function Aliasing
compute = calculate_bill

# 3. Nested Function
def format_receipt(name, amount):
    def add_currency():
        return f"Rs. {amount:.2f}"
    return f"Customer: {name} | Total: {add_currency()}"

# 4. Ternary Operator & Lambda
check_status = lambda score: "Pass" if score >= 40 else "Fail"

# 5. filter()
marks_list = [28, 55, 38, 72, 90, 42]
passed_marks = list(filter(lambda m: m >= 40, marks_list))

print("Bill with Alias   :", compute(1000, 0.05, 50, 20))
print("Formatted Receipt :", format_receipt("Alok", 980))
print("Status of 45      :", check_status(45))
print("Passed Marks List :", passed_marks)
```

## 4. Output
```text
Bill with Alias   : 980.0
Formatted Receipt : Customer: Alok | Total: Rs. 980.00
Status of 45      : Pass
Passed Marks List : [55, 72, 90, 42]
```

## 5. Explanation
- **Types of Arguments:** Positional arguments map in sequence; keyword arguments map by parameter name; default arguments provide fallbacks; `*args` packs extra positional arguments into a `tuple`; `**kwargs` packs extra keyword arguments into a `dict`.
- **Function Aliasing:** Functions in Python are objects. Writing `compute = calculate_bill` copies the function reference without executing it. Both names point to the same memory address (`compute is calculate_bill` is `True`).
- **Nested Functions:** `add_currency()` exists inside `format_receipt()` and cannot be accessed from global scope, creating encapsulation.
- **Ternary Operator:** `value_if_true if condition else value_if_false` evaluates compactly in a single expression line.
- **Lambda & `filter()`:** `lambda m: m >= 40` evaluates each item in `marks_list`. `filter()` passes items that evaluate to `True` into an iterator, which is cast into a Python `list`.

## 6. Important Points
- Default arguments must always be placed **after** non-default arguments (`def f(a, b=5):` is valid; `def f(a=5, b):` causes `SyntaxError`).
- When aliasing a function, never include parentheses `()` (e.g., `alias = func`, not `alias = func()`).
- Lambda functions can only contain a single expression—no statements, loops, or multiple assignments.
- `filter(func, iterable)` returns a lazy iterator; use `list(filter(...))` to view and store the results.
- Nested functions can read variables from their enclosing outer function scope (LEGB rule).

## 7. Common Mistakes
- **SyntaxError in Default Arguments:** Placing non-default argument after a default argument:
  ```python
  def greet(message="Hi", name):  # SyntaxError: non-default argument follows default argument
  ```
- **Calling Instead of Aliasing:** Writing `alias = func()` stores the return value of `func()`, not the function object itself.
- **Iterating Filter Once:** Trying to iterate over a raw `filter` object twice; it exhausts after one pass unless converted to `list`.
- **Using Return in Lambda:** Writing `lambda x: return x * 2` causes a `SyntaxError` (`lambda` automatically returns the expression result).

## 8. Practice Questions
1. Write a function `greet_user(name, title="Mr.")` that uses default and keyword arguments.
2. Create an alias `quadruple` for a function `multiply_by_four(n)` and verify both have the same `id()`.
3. Write a nested function where the inner function squares a number and the outer function adds two squared numbers.
4. Use a ternary operator inside a lambda function to return `"Adult"` if age >= 18 else `"Minor"`.
5. Given `numbers = [15, 22, 33, 40, 55, 60]`, use `filter()` with a lambda to extract all numbers divisible by 5.
