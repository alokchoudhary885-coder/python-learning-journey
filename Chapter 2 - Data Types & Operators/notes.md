# Chapter 2 - Data Types & Operators in Python

## 1. Definition
Data types specify the kind of value a variable can store, such as numbers, text, or truth values. Operators are special symbols in Python used to perform computations, comparisons, and logical evaluations on values and variables.

## 2. Syntax
```python
# Data Types
age = 21            # int
price = 99.50       # float
name = "Alok"       # str
is_active = True    # bool

# Checking Type
type(variable_name)

# Type Conversion
converted_value = int("25")

# Operators
sum_result = a + b      # Arithmetic
is_equal = (a == b)     # Comparison
both_true = p and q     # Logical
```

## 3. Example
```python
# Variables with different data types
item_price = 120.5
quantity = 3
is_member = True

# Calculation using arithmetic operators
subtotal = item_price * quantity

# Type conversion
discount_percent = int("10")
discount = (subtotal * discount_percent) / 100
final_bill = subtotal - discount

# Logical comparison
eligible_for_gift = final_bill > 300 and is_member

print("Subtotal:", subtotal)
print("Discount:", discount)
print("Final Bill:", final_bill)
print("Eligible for Gift:", eligible_for_gift)
```

## 4. Output
```text
Subtotal: 361.5
Discount: 36.15
Final Bill: 325.35
Eligible for Gift: True
```

## 5. Explanation
- `item_price` is a `float`, `quantity` is an `int`, and `is_member` is a `bool`.
- `int("10")` explicitly converts the string `"10"` into the integer `10`.
- Operators `*`, `/`, `-` perform standard arithmetic calculations.
- `final_bill > 300 and is_member` uses a comparison operator (`>`) and a logical operator (`and`) to evaluate to `True`.

## 6. Important Points
- Python has 4 primary scalar data types: `int`, `float`, `str`, `bool`.
- `type()` returns the data type of any object.
- Division `/` always returns a `float` in Python 3 (e.g., `4 / 2` gives `2.0`).
- Floor division `//` discards the fractional part and returns the quotient.
- Modulus `%` returns the remainder of division.
- Exponentiation is written as `**` (e.g., `2 ** 3` is `8`).
- In Python, implicit conversion automatically converts a narrower type (like `int`) to a wider type (like `float`) during operations.

## 7. Common Mistakes
- Trying to concatenate a string and an integer directly (e.g., `"Age: " + 21` raises a `TypeError`; use `str(21)` or comma in `print`).
- Confusing assignment `=` with equality comparison `==`.
- Assuming integer division truncates to integer type (e.g., `5 // 2.0` produces `2.0`, not `2`).
- Converting invalid strings to numbers (e.g., `int("abc")` raises `ValueError`).

## 8. Practice Questions
1. Predict the output and type of `5 + 2.0` and `10 // 3`.
2. Convert a user input string `"45"` into an integer, add `5`, and print the result.
3. Write a program to calculate simple interest: `SI = (P * R * T) / 100`.
4. What is the difference between `/` and `//` in Python? Give examples.
5. Given `x = 10` and `y = 20`, swap their values without using a temporary variable.