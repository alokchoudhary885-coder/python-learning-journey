# Why Lambda Is Not Used Everywhere in Python

## 1. Definition
A **lambda function** is a small, anonymous function defined with the `lambda` keyword that evaluates and returns a single expression. While useful for short, inline operations, it is intentionally limited and is not meant to replace standard `def` functions.

## 2. Why We Use Lambda (And When It Is Useful)
Lambda functions excel in specific, limited contexts:
- **Short throwaway functions:** For one-time use without cluttering the global namespace with helper function names.
- **Sorting keys:** In `sorted(iterable, key=lambda x: ...)` or `list.sort(key=lambda x: ...)`.
- **Inline functional utilities:** Inside `map()`, `filter()`, or GUI event callbacks.

## 3. Syntax Comparison
```python
# Lambda Syntax (Single expression, implicit return)
lambda arg1, arg2: arg1 + arg2

# Normal 'def' Syntax (Multiple statements, explicit return, docstrings)
def add(arg1, arg2):
    """Add two numbers and return the result."""
    return arg1 + arg2
```

## 4. Simple Explanation: Why `def` Is Preferred for Real-World Code
1. **Readability & The Zen of Python:** "Readability counts." Complex one-liners violate Python's core philosophy.
2. **Naming & Identity:** A `def` function has a descriptive name (`func.__name__ = "calculate_tax"`), whereas all lambdas have `__name__ = "<lambda>"`.
3. **Debugging & Tracebacks:** When an exception occurs inside a lambda, Python's traceback only indicates `<lambda>`, making it difficult to find the buggy line when multiple lambdas exist.
4. **Statements & Multi-step Logic:** Lambdas cannot contain loops (`for`, `while`), assignments (`=`), assertions (`assert`), exception handling (`try-except`), or multiple statements.
5. **Documentation & Type Hints:** Lambdas cannot have docstrings (`"""..."""`) or type hints, severely degrading maintainability in team projects.

## 5. Practical Examples: Lambda vs `def`
```python
# GOOD USE of Lambda: Sorting dictionaries by key
students = [{"name": "Alok", "age": 21}, {"name": "Priya", "age": 19}]
students_sorted = sorted(students, key=lambda s: s["age"])

# BAD USE of Lambda: Over-complicated nested ternary logic
bad = lambda x, y: x * 2 if x > y else (y * 3 if y > 10 else 0)

# CLEAN REPLACEMENT with def:
def evaluate_values(x, y):
    """Evaluates x and y cleanly with clear branches."""
    if x > y:
        return x * 2
    if y > 10:
        return y * 3
    return 0
```

## 6. Expected Output
```text
Sorted students: [{'name': 'Priya', 'age': 19}, {'name': 'Alok', 'age': 21}]
Evaluated result: 20
```

## 7. Important Differences: `lambda` vs `def`
| Feature | Lambda Function | Normal `def` Function |
|---|---|---|
| **Naming** | Anonymous (`__name__ == '<lambda>'`) | Named (`__name__ == 'function_name'`) |
| **Expression limit** | Exactly one expression | Multiple statements and lines |
| **Return keyword** | Implicit (no `return` keyword) | Explicit (uses `return`) |
| **Docstrings** | Not supported | Fully supported |
| **PEP 8 Guideline** | Discourages assigning to variables (`f = lambda ...`) | Recommended for all reusable logic |
| **Debugging** | Harder to trace in stack traces | Clear stack traces with line & name |

## 8. Common Mistakes
1. **Binding lambda to a variable name:** Writing `square = lambda x: x ** 2`. PEP 8 explicitly advises using `def square(x): return x ** 2`.
2. **Writing `return` inside lambda:** Writing `lambda x: return x * 2` raises `SyntaxError`.
3. **Attempting multiple statements:** Trying to write `lambda x: print(x); x * 2` or `if-else` blocks without ternary syntax.

## 9. Short Revision Notes
- Lambda is for simple, short, anonymous inline operations.
- `def` is for all reusable, multi-step, documented, or business-critical logic.
- Do not sacrifice readability just to make your code fit on a single line.
- Use list comprehensions or `def` functions whenever a lambda starts getting hard to read.

## 10. Practice Questions with Answers

### Q1. What does PEP 8 say about assigning a lambda function to a variable name?
**Answer:** PEP 8 explicitly discourages it. It recommends always using a `def` statement instead of an assignment statement that binds a lambda to an identifier.

### Q2. Why does debugging code with many lambda functions become difficult?
**Answer:** In stack traces and profilers, lambda functions all share the generic name `<lambda>`, making it hard to identify which specific lambda raised an exception.

### Q3. Can a lambda function contain an `if-else` statement?
**Answer:** Not a traditional multi-line `if-else` statement, but it can contain a single-line ternary conditional expression (`val1 if condition else val2`).

### Q4. Can you add a docstring to a lambda function?
**Answer:** No, lambda functions do not support docstrings.

### Q5. Convert this unreadable lambda into a clean `def` function:
`f = lambda a, b: a / b if b != 0 else None`
**Answer:**
```python
def safe_divide(numerator, denominator):
    """Safely divides numerator by denominator, returning None on division by zero."""
    if denominator == 0:
        return None
    return numerator / denominator
```
