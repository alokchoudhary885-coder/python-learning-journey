# Python Tuples: The Complete Guide

## 1. Definition
A **Tuple** in Python is an **ordered**, **immutable** (unchangeable), and **heterogeneous** collection of elements enclosed in parentheses `()`. Once a tuple is created, elements cannot be added, removed, or modified.

---

## 2. Why We Use Tuples (Tuples vs Lists)
1. **Data Protection (Write-Safety):** Prevents accidental modification of constant data (e.g., GPS coordinates, RGB colors, configuration settings).
2. **Speed & Performance:** Because tuples are immutable, Python optimizes their memory allocation. Iterating through a tuple is faster than iterating through a list.
3. **Dictionary Keys:** Because tuples are immutable, they are **hashable**, meaning they can be used as keys in Python dictionaries (lists cannot).
4. **Function Returns:** Python uses tuples internally whenever a function returns multiple values separated by commas.

---

## 3. Syntax & The Single-Element Trap

### Standard Creation:
```python
t = (1, 2, 3)
empty_tuple = ()
constructed = tuple([1, 2, 3])
```

### ⚠️ The Single-Element Comma Trap:
Parentheses in Python are also used for grouping mathematical expressions `(10 + 5)`. Therefore:
```python
x = ("Apple")   # ❌ String, NOT a tuple!
y = ("Apple",)  # ✅ Tuple (Trailing comma identifies it as a tuple)
```

---

## 4. Indexing & Slicing
Tuples support the exact same zero-based positive and negative indexing as lists:
```python
coords = (28.61, 77.20, 150.0)
print(coords[0])      # 28.61 (First item)
print(coords[-1])     # 150.0 (Last item)
print(coords[:2])     # (28.61, 77.20)
print(coords[::-1])   # (150.0, 77.20, 28.61) - Reversed
```

---

## 5. Tuple Packing & Unpacking

### Packing:
```python
# Packing multiple items into a single tuple (parentheses are optional)
person = 101, "Alok", "India"
```

### Unpacking:
```python
roll, name, country = person
# roll = 101, name = "Alok", country = "India"
```

### Extended Unpacking with `*` (Starred Expression):
```python
data = (10, 20, 30, 40, 50)
first, *middle, last = data
# first = 10, middle = [20, 30, 40], last = 50
```

---

## 6. Built-in Tuple Methods

Tuples have only **two** built-in methods because they cannot be modified:

| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`count()`** | `t.count(value)` | Returns the number of occurrences of `value`. |
| **`index()`** | `t.index(value)` | Returns the zero-based index of the first occurrence. |

---

## 7. Comparison: Tuple vs List

| Feature | Tuple | List |
| :--- | :--- | :--- |
| **Syntax** | Parentheses `(1, 2)` | Square brackets `[1, 2]` |
| **Mutability** | **Immutable** (cannot be modified) | **Mutable** (can add, edit, delete) |
| **Memory** | Smaller memory footprint | Larger memory footprint (over-allocated buffer) |
| **Performance** | Faster access and iteration | Slower due to dynamic resize overhead |
| **Hashable?** | Yes (can be dictionary keys / set items) | No (unhashable type) |
| **Use Case** | Fixed constants, function return values | Dynamic collections that change over time |

---

## 8. Common Mistakes
1. **Attempting to modify a tuple:**
   ```python
   # ❌ TypeError: 'tuple' object does not support item assignment
   t = (1, 2, 3)
   t[0] = 99
   ```
2. **Forgetting the comma for single-element tuples:**
   Writing `val = (5)` gives an `int`, not a `tuple`. Use `val = (5,)`.
3. **Misunderstanding mutable objects inside a tuple:**
   If a tuple contains a list `t = (1, [10, 20])`, the tuple itself cannot be reassigned, but the inner list can be modified (`t[1].append(30)` works!).

---

## 9. Quick Revision Notes
- Tuples are immutable and ordered.
- A single-element tuple requires a trailing comma: `(x,)`.
- Unpack with matching variable count or use `*rest`.
- Only 2 methods: `.count()` and `.index()`.
- Use tuples when you want data to remain read-only.

---

## 10. Practice Questions & Answers

### Q1: How do you swap two variables in Python using a tuple?
**Answer:**
```python
a = 10
b = 20
a, b = b, a  # Uses tuple packing and unpacking under the hood!
```

### Q2: What is the output of `len((10))` vs `len((10,))`?
**Answer:** `len((10))` raises `TypeError: object of type 'int' has no len()`. `len((10,))` returns `1`.

### Q3: Can you delete an individual element from a tuple?
**Answer:** No. Individual elements cannot be deleted. However, you can delete the entire tuple from memory using `del my_tuple`.

### Q4: How do you add an element to an existing tuple?
**Answer:** Because tuples are immutable, you cannot modify the existing tuple. You must concatenate and create a new tuple:
```python
t = (1, 2, 3)
t = t + (4,)  # Creates a new tuple (1, 2, 3, 4)
```

### Q5: Write a function `divide_remainder(a, b)` that returns quotient and remainder as a tuple:
```python
def divide_remainder(a, b):
    quotient = a // b
    remainder = a % b
    return quotient, remainder

q, r = divide_remainder(17, 5)
print(f"Quotient: {q}, Remainder: {r}")  # Quotient: 3, Remainder: 2
```
