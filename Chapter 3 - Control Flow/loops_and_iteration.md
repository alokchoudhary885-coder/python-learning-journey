# Loops and Iteration in Python

## 1. Definition
**Iterative Statements (Loops)** allow a block of code to be executed repeatedly either for a fixed number of times or until a specific condition becomes `False`.

Python provides two primary loop constructs:
1. **`for` loop:** Iterates directly over the elements of any sequence (such as lists, tuples, strings, or ranges).
2. **`while` loop:** Repeatedly executes statements as long as a test condition remains `True`.

---

## 2. Why We Use Loops
- Avoids code repetition (violating the DRY principle).
- Enables traversing large collections of data (e.g. processing 10,000 database records).
- Powers polling, simulations, game loops, and search algorithms.

---

## 3. Syntax & Forms

### A. The `for` Loop with `range()`
```python
for item in sequence:
    # Executed for each element in sequence
    statements
```
`range(start, stop, step)` generates a sequence of numbers from `start` up to (but not including) `stop`:
```python
range(5)          # 0, 1, 2, 3, 4
range(1, 6)       # 1, 2, 3, 4, 5
range(0, 10, 2)   # 0, 2, 4, 6, 8 (step 2)
range(5, 0, -1)   # 5, 4, 3, 2, 1 (reverse)
```

### B. The `while` Loop
```python
while condition:
    # Executed repeatedly while condition is True
    statements
    # Must update loop variable to avoid infinite loop!
```

---

## 4. Loop Control Statements

| Keyword | Purpose | Example |
| :--- | :--- | :--- |
| **`break`** | Immediately terminates the loop and exits. | Stops searching once item is found. |
| **`continue`** | Skips the rest of the current iteration and jumps to the next iteration. | Skips invalid records or negative values. |
| **`pass`** | A null statement (placeholder); does nothing. | Syntactic placeholder for empty loops. |

---

## 5. Python's Unique `for...else` and `while...else` Construct

In Python, loops can have an optional **`else` block**:
```python
for item in collection:
    if condition:
        # Match found!
        break
else:
    # Executed ONLY IF the loop finished NATURALLY without hitting a 'break'!
    print("Item not found")
```
- If the loop terminates via `break`, the `else` block is **skipped**.
- If the loop finishes all iterations without breaking, the `else` block **runs**.
- Eliminates the need for awkward boolean flags (e.g. `found = False`).

---

## 6. Practical Example: Prime Number Checker
```python
number = 29

if number <= 1:
    print(f"{number} is not prime.")
else:
    for divisor in range(2, int(number ** 0.5) + 1):
        if number % divisor == 0:
            print(f"{number} is not prime (divisible by {divisor}).")
            break
    else:
        print(f"{number} is a Prime Number!")
```

---

## 7. Comparison: `for` Loop vs `while` Loop

| Feature | `for` Loop | `while` Loop |
| :--- | :--- | :--- |
| **When to Use** | When the number of iterations or sequence length is known | When iterations depend on a dynamic condition |
| **Loop Counter** | Incremented automatically by Python | Must be updated manually inside loop body |
| **Risk of Infinite Loop** | Very low (sequences are finite) | High if condition variable is never updated |
| **Performance** | Optimized in C under the hood | Slightly more overhead per condition check |

---

## 8. Common Mistakes
1. **The Off-by-One Error:**
   `range(1, 5)` stops at `4`, not `5`!
2. **Infinite While Loops:**
   Forgetting to update the counter (`i += 1`) causes the program to hang indefinitely.
3. **Modifying a list while iterating over it:**
   ```python
   # ❌ Modifying a list during iteration skips elements!
   numbers = [1, 2, 3, 4]
   for n in numbers:
       if n % 2 == 0: numbers.remove(n)
   # ✅ Pythonic: Iterate over a slice copy or use list comprehension
   numbers = [n for n in numbers if n % 2 != 0]
   ```

---

## 9. Quick Revision Notes
- Use `enumerate(seq)` to get both index and value: `for i, val in enumerate(list):`.
- `range()` returns an efficient generator-like lazy object in Python 3, using minimal memory.
- `break` exits the nearest enclosing loop.
- `else` on a loop executes only if **no `break`** occurred.

---

## 10. Practice Questions & Answers

### Q1: What is the output of `range(5, 5)`?
**Answer:** An empty range (0 elements). The start equals the stop, so the loop never runs.

### Q2: What does the following code print?
```python
for i in range(3):
    if i == 1:
        continue
    print(i, end=" ")
else:
    print("Done")
```
**Answer:** `0 2 Done`. The `continue` statement skips printing `1`, but since no `break` occurred, the `else` block executes.

### Q3: How do you reverse iterate over a list without modifying it?
**Answer:** Using `reversed(my_list)` or `for item in my_list[::-1]:`.

### Q4: Write a `while` loop that computes the factorial of `5`.
```python
n = 5
fact = 1
while n > 0:
    fact *= n
    n -= 1
print("Factorial:", fact)  # 120
```

### Q5: When does a `while...else` statement execute its `else` block?
**Answer:** When the `while` test condition evaluates to `False` naturally without an internal `break` being triggered.
