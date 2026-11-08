# Python Sets: The Complete Guide

## 1. Definition
A **Set** in Python is an **unordered**, **unindexed**, and **mutable** collection of **unique** elements enclosed in curly braces `{}`. Sets cannot contain duplicate values, and every item inside a set must be **immutable** (hashable).

---

## 2. Why We Use Sets
1. **Automatic Deduplication:** Instantly eliminate duplicate values from any list or collection (`list(set(my_list))`).
2. **Blazing Fast Membership Testing ($O(1)$ Time Complexity):** Checking `item in my_set` uses hash tables and takes $O(1)$ constant time, compared to $O(n)$ linear scan in lists.
3. **Mathematical Set Operations:** Built-in support for union, intersection, set difference, and symmetric difference.

---

## 3. Syntax & The Empty Set Trap

### Standard Set Creation:
```python
fruits = {"apple", "banana", "cherry"}
unique_numbers = set([1, 2, 2, 3, 4, 4, 5])  # {1, 2, 3, 4, 5}
```

### ⚠️ The Empty Set Trap:
In Python, empty curly braces `{}` create an **empty dictionary**, not a set:
```python
x = {}       # ❌ Type is <class 'dict'>
y = set()    # ✅ Type is <class 'set'> (Always use set() for an empty set!)
```

---

## 4. Adding & Removing Elements

| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`add()`** | `s.add(elem)` | Adds a single element to the set. |
| **`update()`** | `s.update(iterable)` | Adds multiple elements from an iterable. |
| **`remove()`** | `s.remove(elem)` | Removes element; **raises `KeyError`** if element is not found! |
| **`discard()`** | `s.discard(elem)` | Removes element; **does NOT raise error** if element is missing (safe!). |
| **`pop()`** | `s.pop()` | Removes and returns an arbitrary element (raises `KeyError` if empty). |
| **`clear()`** | `s.clear()` | Empties all elements from the set. |

---

## 5. Mathematical Set Operations

Python provides both **operator symbols** and **named methods**:

| Operation | Operator | Method Syntax | Meaning |
| :--- | :---: | :--- | :--- |
| **Union** | `A \| B` | `A.union(B)` | All elements from both sets. |
| **Intersection** | `A & B` | `A.intersection(B)` | Elements common to both sets. |
| **Difference** | `A - B` | `A.difference(B)` | Elements in A, but not in B. |
| **Symmetric Difference** | `A ^ B` | `A.symmetric_difference(B)` | Elements in either set, but not both. |
| **Subset Check** | `A <= B` | `A.issubset(B)` | Returns `True` if all elements of A are in B. |
| **Superset Check** | `A >= B` | `A.issuperset(B)` | Returns `True` if A contains all elements of B. |
| **Disjoint Check** | — | `A.isdisjoint(B)` | Returns `True` if A and B have NO common elements. |

---

## 6. What is `frozenset`?
A regular set is mutable, which means it **cannot** be used as a dictionary key or placed inside another set.

A **`frozenset`** is an **immutable set**:
```python
frozen = frozenset([1, 2, 3])
# frozen.add(4) # ❌ AttributeError!
# Can be used as a dictionary key:
data = {frozen: "Immutable Key Valid"}
```

---

## 7. Master Comparison: List vs Tuple vs Set vs Dictionary

| Dimension | List | Tuple | Set | Dictionary |
| :--- | :--- | :--- | :--- | :--- |
| **Syntax** | `[1, 2]` | `(1, 2)` | `{1, 2}` | `{"a": 1}` |
| **Ordered?** | Yes | Yes | **No** (Unordered) | Yes (Python 3.7+) |
| **Mutable?** | Yes | **No** | Yes | Yes |
| **Duplicates?** | Allowed | Allowed | **Not Allowed** | Keys unique; Values duplicate |
| **Indexing** | `0, 1, 2` | `0, 1, 2` | **No Indexing** (`s[0]` fails) | By Keys (`d["key"]`) |
| **Lookup Time** | $O(n)$ | $O(n)$ | **$O(1)$** | **$O(1)$** |

---

## 8. Common Mistakes
1. **Trying to access elements by index:**
   `s[0]` raises `TypeError: 'set' object is not subscriptable`.
2. **Storing mutable objects inside a set:**
   `{[1, 2], [3, 4]}` raises `TypeError: unhashable type: 'list'`. (Use tuples instead: `{(1, 2), (3, 4)}`).
3. **Using `remove()` without checking existence:**
   Use `discard()` instead of `remove()` if you don't want a `KeyError` when the item is missing.

---

## 9. Quick Revision Notes
- Sets store unique, hashable items.
- Sets are unordered — element positions change dynamically.
- `set()` is required for an empty set (`{}` is an empty dictionary).
- Fast $O(1)$ membership testing with `x in s`.
- `frozenset` is an immutable, hashable set.

---

## 10. Practice Questions & Answers

### Q1: How do you remove duplicates from a list while maintaining order?
**Answer:**
Using `dict.fromkeys()` (since dicts preserve insertion order in Python 3.7+):
```python
items = [1, 2, 2, 3, 1, 4]
unique = list(dict.fromkeys(items))  # [1, 2, 3, 4]
```

### Q2: What is the output of `{1, True, "1"}`?
**Answer:** `{1, '1'}`. In Python, `1 == True` is `True` and their hash values are identical. Therefore, `True` is treated as a duplicate of `1` and ignored.

### Q3: How do you find common elements between three sets `A`, `B`, and `C`?
**Answer:** Using the intersection operator: `common = A & B & C` or `A.intersection(B, C)`.

### Q4: What is the difference between `s.discard(x)` and `s.remove(x)`?
**Answer:** If `x` does not exist in the set, `s.remove(x)` raises a `KeyError`, whereas `s.discard(x)` silently ignores it without raising an error.

### Q5: Write a set comprehension that extracts all unique vowels from a string:
```python
text = "Antigravity artificial intelligence"
vowels = {char.lower() for char in text if char.lower() in "aeiou"}
print(vowels)  # {'a', 'e', 'i'}
```
