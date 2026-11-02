# Conditional Statements in Python

## 1. Definition
**Conditional Statements** are control flow structures that allow a Python program to make decisions and execute specific blocks of code based on whether a condition evaluates to `True` or `False`.

In Python, the primary decision-making constructs are `if`, `elif`, `else`, and `match-case` (Python 3.10+).

---

## 2. Why We Use Conditional Statements
Programs rarely execute sequentially from top to bottom without variation. Real-world applications require dynamic responses:
- Verifying a user's password before granting access.
- Checking stock availability before placing an order.
- Calculating progressive tax slabs based on income brackets.

---

## 3. Syntax & Forms

### A. Simple `if` Statement
```python
if condition:
    # Executed only if condition is True
    statements
```

### B. `if-else` Statement
```python
if condition:
    # Executed if condition is True
    statement_1
else:
    # Executed if condition is False
    statement_2
```

### C. `if-elif-else` Ladder
```python
if condition_1:
    statement_1
elif condition_2:
    statement_2
else:
    fallback_statement
```

### D. Structural Pattern Matching (`match-case`)
Introduced in Python 3.10 as an elegant alternative to long `if-elif` chains:
```python
match variable:
    case value_1:
        action_1
    case value_2:
        action_2
    case _:
        default_action  # Wildcard matches everything
```

---

## 4. How It Works Internally: Short-Circuit Evaluation
Python conditions are evaluated from left to right using **short-circuit evaluation**:
- In an **`and`** chain: As soon as one operand is `False`, Python stops evaluating the remaining conditions and returns `False`.
- In an **`or`** chain: As soon as one operand is `True`, Python stops evaluating and returns `True`.

This is crucial for preventing errors:
```python
# Safe: If user is None, user.is_active is never checked (avoids AttributeError)
if user is not None and user.is_active:
    print("Welcome!")
```

---

## 5. Truthy and Falsy Values in Python
Every value in Python has an inherent boolean truth value:

| Falsy Values (evaluate to `False`) | Truthy Values (evaluate to `True`) |
| :--- | :--- |
| `0`, `0.0`, `0j` | Any non-zero number (`1`, `-5`, `3.14`) |
| `""` (empty string) | Non-empty string (`"hello"`, `" "`) |
| `[]` (empty list), `()` (empty tuple) | Non-empty collections (`[1, 2]`, `{'a': 1}`) |
| `{}` (empty dict), `set()` | Function objects, class instances |
| `None`, `False` | `True` |

---

## 6. Practical Example: E-Commerce Discount Engine
```python
cart_total = 2500
is_premium_member = True

if cart_total >= 5000:
    discount_pct = 25
elif cart_total >= 2000 or is_premium_member:
    discount_pct = 15
else:
    discount_pct = 5

final_amount = cart_total - (cart_total * discount_pct / 100)
print(f"Original: Rs. {cart_total} | Discount: {discount_pct}% | Pay: Rs. {final_amount}")
```

---

## 7. Important Differences: `if-elif` Ladder vs Multiple Independent `if` Statements
- In an **`if-elif` ladder**, only the **first matching block** runs. The rest are completely skipped.
- In **multiple independent `if` statements**, **every single condition** is evaluated independently, which can cause multiple blocks to run unexpectedly.

---

## 8. Common Mistakes
1. **Using assignment `=` instead of equality `==`:**
   ```python
   # ❌ SyntaxError: invalid syntax
   if age = 18:
       print("Adult")
   ```
2. **Missing colon `:` at the end of `if`/`elif`/`else` line.**
3. **Inconsistent Indentation:**
   Mixing tabs and spaces will trigger an `IndentationError`.
4. **Redundant comparisons with boolean literals:**
   ```python
   # ❌ Bad practice:
   if is_logged_in == True:
   # ✅ Pythonic:
   if is_logged_in:
   ```

---

## 9. Quick Revision Notes
- Python uses indentation (4 spaces) rather than curly braces `{}` to define code blocks.
- `elif` is short for "else if".
- Wildcard `case _:` in `match-case` acts as the default fallback.
- Python's `and` / `or` short-circuit evaluation prevents unnecessary function execution.

---

## 10. Practice Questions & Answers

### Q1: What does the following code print?
```python
x = 0
if x:
    print("Yes")
else:
    print("No")
```
**Answer:** `No`. The integer `0` is a falsy value in Python.

### Q2: What is the difference between `elif` and `else if` in Python?
**Answer:** Python does not have an `else if` keyword. Writing `else if` is a syntax error. Python uses the keyword `elif`.

### Q3: How can you write a one-line if-else in Python?
**Answer:** Using the ternary conditional expression:
```python
status = "Adult" if age >= 18 else "Minor"
```

### Q4: Write a program to check if a given year is a Leap Year.
```python
year = 2024
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a Leap Year")
else:
    print(f"{year} is not a Leap Year")
```

### Q5: How does `match-case` differ from traditional `switch` statements in C/Java?
**Answer:** Unlike C/Java `switch`, Python's `match-case` does not require explicit `break` statements (it does not fall through by default). It also supports advanced structural pattern matching (matching sequences, types, and dictionaries).
