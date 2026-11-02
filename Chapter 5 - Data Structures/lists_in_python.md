# Python Lists: The Complete Guide

## 1. Definition
A **List** in Python is an **ordered**, **mutable** (changeable), and **dynamic** sequence of elements enclosed in square brackets `[]`. Lists can hold heterogeneous data types (integers, floats, strings, objects, and nested lists) and allow duplicate values.

---

## 2. Why We Use Lists
- Storing grouped collections of related records (e.g. shopping carts, student names, search results).
- Fast random access by zero-based index in $O(1)$ time complexity.
- Highly versatile with rich built-in manipulation methods (`append`, `sort`, `pop`, `extend`).

---

## 3. Syntax & Forms

```python
# Empty lists
empty_list = []
empty_via_constructor = list()

# Homogeneous & Heterogeneous
numbers = [10, 20, 30, 40]
mixed = [101, "Alok", 92.5, True, ["Sub", "List"]]
```

---

## 4. Indexing and Slicing Formula

```text
Positive Index:   0     1     2     3     4
Elements:       [ A  ,  B  ,  C  ,  D  ,  E ]
Negative Index:  -5    -4    -3    -2    -1
```

### Slicing Syntax:
```python
list[start : stop : step]
```
- `start`: Inclusive starting index (defaults to `0`).
- `stop`: Exclusive ending index (defaults to `len(list)`).
- `step`: Stride / step size (defaults to `1`). Negative step reverses direction.

---

## 5. Essential List Methods Reference

| Method | Syntax | Description | In-place? |
| :--- | :--- | :--- | :--- |
| `append()` | `list.append(x)` | Adds element `x` to the end | Yes |
| `extend()` | `list.extend(iterable)` | Appends all items from iterable | Yes |
| `insert()` | `list.insert(idx, x)` | Inserts `x` at specified index `idx` | Yes |
| `pop()` | `list.pop([idx])` | Removes and returns element at index (default last) | Yes |
| `remove()` | `list.remove(val)` | Removes first occurrence of value `val` | Yes |
| `sort()` | `list.sort(reverse=False)` | Sorts elements in-place | Yes |
| `sorted()` | `sorted(list)` | Built-in function returning a **new** sorted list | No |
| `reverse()` | `list.reverse()` | Reverses elements in-place | Yes |
| `count()` | `list.count(val)` | Returns number of occurrences of `val` | No |
| `index()` | `list.index(val)` | Returns zero-based index of first occurrence | No |

---

## 6. List Comprehensions: Clean & Fast Transformations

List comprehensions provide a concise way to create lists based on existing iterables:

```python
# Basic: [expression for item in iterable]
squares = [x ** 2 for x in range(1, 6)]
# Output: [1, 4, 9, 16, 25]

# With condition: [expression for item in iterable if condition]
evens = [x for x in range(10) if x % 2 == 0]
# Output: [0, 2, 4, 6, 8]

# With if-else: [true_val if cond else false_val for item in iterable]
status = ["Pass" if score >= 40 else "Fail" for score in [35, 75, 40]]
# Output: ['Fail', 'Pass', 'Pass']
```

---

## 7. Important Differences: `append()` vs `extend()`

```python
a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]] -> Nested sub-list added as a single element!

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]   -> Individual elements appended!
```

---

## 8. Common Mistakes
1. **Confusing `list.sort()` with `sorted(list)`:**
   `list.sort()` modifies the list in place and returns `None`.
   ```python
   # ❌ result will be None!
   result = my_list.sort()
   # ✅ correct:
   my_list.sort()
   # OR
   result = sorted(my_list)
   ```
2. **Shallow Copy Assignment Trap:**
   Writing `b = a` does NOT create a copy! Both `a` and `b` reference the same list in memory.
   Modifying `b` will also modify `a`!
   Use `b = a.copy()` or `b = a[:]` to create an independent copy.
3. **`IndexError` on out-of-range indexing:**
   `fruits[10]` on a 3-element list triggers `IndexError: list index out of range`. (Note: Slicing `fruits[2:10]` is safe and does not raise an error).

---

## 9. Quick Revision Notes
- Lists are ordered, mutable, and indexed from `0`.
- Negative indexing starts from `-1` at the end.
- `append()` adds one element; `extend()` unpacks an iterable.
- `pop()` removes by index; `remove()` removes by value.
- Reverse a list easily with `list[::-1]`.

---

## 10. Practice Questions & Answers

### Q1: What does `my_list[-1::-1]` do?
**Answer:** It reverses the entire list starting from the last element stepping backward by 1 (equivalent to `my_list[::-1]`).

### Q2: What happens if `list.remove(x)` is called when `x` is not in the list?
**Answer:** It raises a `ValueError: list.remove(x): x not in list`. Always verify with `if x in my_list:` before calling `remove()`.

### Q3: How do you remove duplicate elements from a list while ignoring order?
**Answer:** By converting it to a `set` and back to a `list`:
```python
unique = list(set([1, 2, 2, 3, 4, 4]))  # [1, 2, 3, 4]
```

### Q4: What is the time complexity of appending an element vs inserting at index 0?
**Answer:** `append()` is $O(1)$ amortized (adding to end). `insert(0, val)` is $O(n)$ because every existing element must be shifted right by one position in memory.

### Q5: Write a list comprehension to extract words longer than 4 characters from a sentence:
```python
sentence = "Python is an incredible and versatile programming language"
words = [w for w in sentence.split() if len(w) > 4]
print(words)
# Output: ['Python', 'incredible', 'versatile', 'programming', 'language']
```
