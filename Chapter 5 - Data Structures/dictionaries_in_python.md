# Python Dictionaries: The Complete Guide

## 1. Definition
A **Dictionary** in Python is an **ordered** (from Python 3.7+), **mutable**, and **indexed by keys** collection of key-value pairs enclosed in curly braces `{}`.

Each key must be **unique** and **immutable** (hashable), while values can be of any data type and can be duplicated.

---

## 2. Why We Use Dictionaries
- **Label-based lookup:** Access data using descriptive human-readable keys (e.g. `user["email"]`) rather than arbitrary integer indices (`user[3]`).
- **Blazing Fast Performance ($O(1)$ Search):** Dictionaries are implemented using **Hash Tables**. Finding, inserting, or deleting a key takes average $O(1)$ constant time complexity regardless of dictionary size.
- **JSON & API Standard:** Modern web APIs and databases transmit data almost exclusively in JSON, which maps directly to Python dictionaries.

---

## 3. Syntax & Key Requirements

```python
# Empty dictionary
d1 = {}
d2 = dict()

# Key-Value pairs
person = {
    "name": "Alok",
    "age": 21,
    "skills": ["Python", "Git", "SQL"]
}
```

### ⚠️ Valid vs Invalid Keys (Hashability Rule):
Keys **must** be immutable:
- ✅ Allowed as keys: `str`, `int`, `float`, `tuple`, `bool`
- ❌ NOT allowed as keys: `list`, `set`, `dict` (raises `TypeError: unhashable type: 'list'`)

---

## 4. Safe Lookup: `dict[key]` vs `dict.get()`

```python
data = {"user": "alok885"}

# 1. Square brackets [key]
print(data["user"])    # "alok885"
# print(data["email"]) # ❌ Crashes with KeyError!

# 2. get(key, default) method
print(data.get("email"))                 # None (Safe!)
print(data.get("email", "not_found@x.com"))  # Fallback default value
```

---

## 5. Essential Dictionary Methods Reference

| Method | Syntax | Description |
| :--- | :--- | :--- |
| **`keys()`** | `d.keys()` | Returns a dynamic view of all keys in the dictionary. |
| **`values()`** | `d.values()` | Returns a dynamic view of all values in the dictionary. |
| **`items()`** | `d.items()` | Returns a view of `(key, value)` tuple pairs. |
| **`get()`** | `d.get(k, [d])` | Returns value for key `k` or fallback `d` without crashing. |
| **`update()`** | `d.update(other)` | Merges another dictionary or key-value iterable into `d`. |
| **`pop()`** | `d.pop(k, [d])` | Removes key `k` and returns its value. |
| **`popitem()`** | `d.popitem()` | Removes and returns the last inserted `(key, value)` pair. |
| **`setdefault()`** | `d.setdefault(k, d)` | Returns value if key exists; if not, inserts key with default `d`. |
| **`clear()`** | `d.clear()` | Removes all elements from the dictionary. |

---

## 6. Dictionary Comprehensions

Transform or filter dictionaries concisely:
```python
# Squaring numbers
squares = {x: x * x for x in range(1, 6)}
# Output: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Inverting a dictionary (swapping keys and values)
original = {"A": 1, "B": 2, "C": 3}
inverted = {val: key for key, val in original.items()}
# Output: {1: 'A', 2: 'B', 3: 'C'}

# Filtering
passed_students = {name: score for name, score in {"Alok": 85, "Rahul": 32, "Priya": 91}.items() if score >= 40}
# Output: {'Alok': 85, 'Priya': 91}
```

---

## 7. Master Comparison: List vs Tuple vs Dictionary

| Feature | List | Tuple | Dictionary |
| :--- | :--- | :--- | :--- |
| **Syntax** | `[1, 2, 3]` | `(1, 2, 3)` | `{"key": "value"}` |
| **Indexed By** | Integers `0, 1, 2` | Integers `0, 1, 2` | Unique, immutable keys |
| **Mutability** | **Mutable** | **Immutable** | **Mutable** |
| **Lookup Time** | $O(n)$ search by value | $O(n)$ search by value | **$O(1)$** hash table search by key |
| **Duplicates** | Allowed | Allowed | Keys must be unique; Values can duplicate |

---

## 8. Common Mistakes
1. **Modifying a dictionary while iterating over it:**
   ```python
   # ❌ RuntimeError: dictionary changed size during iteration
   d = {"a": 1, "b": 2}
   for k in d:
       if d[k] == 1: del d[k]
   # ✅ Pythonic fix: Iterate over a list of keys:
   for k in list(d.keys()):
       if d[k] == 1: del d[k]
   ```
2. **Accessing missing keys with brackets `dict[key]`:**
   Always use `.get(key, default)` when a key might not exist.
3. **Using mutable objects as keys:**
   `{[1, 2]: "numbers"}` raises `TypeError: unhashable type: 'list'`. Use a tuple instead: `{(1, 2): "numbers"}`.

---

## 9. Quick Revision Notes
- Dictionaries store `key: value` mappings.
- Keys must be unique and immutable; values can be any type.
- `.get(key, default)` avoids `KeyError`.
- Iterate through `(k, v)` with `for k, v in d.items():`.
- Constant time $O(1)$ lookup speed via hash table.

---

## 10. Practice Questions & Answers

### Q1: What happens if you define a dictionary with duplicate keys?
```python
d = {"a": 1, "b": 2, "a": 3}
print(d)
```
**Answer:** Output is `{'a': 3, 'b': 2}`. In Python, duplicate keys are not allowed; the later assignment overwrites the earlier value.

### Q2: How do you merge two dictionaries in Python 3.9+?
**Answer:** Using the merge union operator `|` or in-place update `|=`:
```python
d1 = {"a": 1}
d2 = {"b": 2}
merged = d1 | d2  # {'a': 1, 'b': 2}
```

### Q3: How can you count word frequencies in a sentence using a dictionary?
**Answer:**
```python
text = "apple banana apple orange banana apple"
freq = {}
for word in text.split():
    freq[word] = freq.get(word, 0) + 1
print(freq)  # {'apple': 3, 'banana': 2, 'orange': 1}
```

### Q4: What does `dict.popitem()` do?
**Answer:** It removes and returns the **last inserted** `(key, value)` pair from the dictionary as a tuple in LIFO (Last-In-First-Out) order.

### Q5: Can a tuple containing a list be used as a dictionary key?
**Answer:** No. Even though the outer structure is a tuple, because it contains a mutable list `(1, [2, 3])`, Python cannot compute a consistent hash and raises `TypeError: unhashable type: 'list'`. All elements inside the tuple must also be hashable.
