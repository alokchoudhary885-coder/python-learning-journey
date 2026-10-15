# Chapter 1 - Python Fundamentals

## 1. Definition
Python fundamentals cover the core building blocks of the language: variables to store data, comments to explain code, statements to execute actions, and indentation to define code blocks.

## 2. Syntax
```python
# Variable assignment
variable_name = value

# Comments
# Single-line comment
"""Multi-line string / comment"""

# Indented block (standard 4 spaces)
if condition:
    statement_1
    statement_2
```

## 3. Example
```python
# Student details
student_name = "Alok"
student_age = 21

# Conditional statement with indentation
if student_age >= 18:
    print(student_name, "is eligible to vote.")
else:
    print(student_name, "is not eligible to vote.")
```

## 4. Output
```text
Alok is eligible to vote.
```

## 5. Explanation
- `student_name = "Alok"` assigns a string value to a variable named `student_name`.
- `#` begins a comment that Python ignores during execution.
- Python uses whitespace indentation (usually 4 spaces) instead of curly braces `{}` to define code blocks.
- The `if-else` statement controls code flow based on whether `student_age >= 18` evaluates to `True` or `False`.

## 6. Important Points
- Variable names cannot start with a number or contain spaces or special symbols (except `_`).
- In Python, variable types are dynamically inferred; you do not need to declare types explicitly.
- Inconsistent indentation causes an `IndentationError`.
- Statements perform actions, while expressions evaluate to a value.

## 7. Common Mistakes
- Mixing tabs and spaces for indentation.
- Forgetting the colon `:` at the end of `if`, `else`, `for`, or `def` lines.
- Using Python keywords (e.g., `def`, `class`, `if`) as variable names.
- Forgetting that variable names are case-sensitive (`Age` vs `age`).

## 8. Practice Questions
1. Create three variables for book title, author, and price, and print them.
2. What will happen if you use a reserved keyword like `pass = 10`?
3. Write a code snippet with an `if-else` condition using 4 spaces of indentation.
4. Explain the difference between an expression and a statement with examples.
5. Fix the indentation error in this code:
   ```python
   if True:
   print("Hello")
   ```
