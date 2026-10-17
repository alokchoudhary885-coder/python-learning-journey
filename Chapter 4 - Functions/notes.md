# Chapter 4 - Functions, Functional Tools & Python Modules

## 1. Definition
Python functions are versatile first-class objects that support flexible parameter passing (**positional, keyword, default, `*args`, `**kwargs`**), **variable scope** (local vs global), and **recursion**. Python provides functional tools like **`map()`** for transforming collections, **`filter()`** for conditional extraction, and **`reduce()`** for cumulative aggregation. Code is organized into reusable files called **modules**, which Python resolves and loads using a structured import hierarchy.

## 2. Syntax
```python
# 1. Functions & Arguments
def calculate(base, rate=0.05, *discounts, **metadata):
    return (base * (1 + rate)) - sum(discounts)

# 2. Functional Tools
mapped_data = list(map(lambda x: x * 2, [1, 2, 3]))
filtered_data = list(filter(lambda x: x > 2, [1, 2, 3, 4]))

from functools import reduce
reduced_val = reduce(lambda acc, x: acc + x, [1, 2, 3, 4])

# 3. Modules & Aliasing
import math as m
from my_module import calculate_circle_area
```

## 3. Example
```python
from functools import reduce
import math as m

# Functional pipeline:
# Step 1: Filter even numbers
# Step 2: Double them using map()
# Step 3: Sum them using reduce()
numbers = [1, 2, 3, 4, 5, 6, 7, 8]

even_nums = list(filter(lambda x: x % 2 == 0, numbers))
doubled_evens = list(map(lambda x: x * 2, even_nums))
total_sum = reduce(lambda acc, x: acc + x, doubled_evens)

print("Original Numbers :", numbers)
print("Even Numbers     :", even_nums)
print("Doubled Evens    :", doubled_evens)
print("Total Sum        :", total_sum)
print("Square root of sum via alias (m.sqrt):", m.sqrt(total_sum))
```

## 4. Output
```text
Original Numbers : [1, 2, 3, 4, 5, 6, 7, 8]
Even Numbers     : [2, 4, 6, 8]
Doubled Evens    : [4, 8, 12, 16]
Total Sum        : 40
Square root of sum via alias (m.sqrt): 6.324555320336759
```

## 5. Explanation
- **`filter()`** checks each number against `x % 2 == 0` and keeps only `[2, 4, 6, 8]`.
- **`map()`** transforms each filtered number by multiplying by 2, yielding `[4, 8, 12, 16]`.
- **`reduce()`** aggregates the list elements sequentially: $((4 + 8) + 12) + 16 = 40$.
- **`import math as m`** loads the standard math module and binds it to the short alias `m`.

## 6. Important Points
- **Functional Tools:** `map()` and `filter()` return lazy iterators; always cast to `list()` to inspect or reuse. `reduce()` returns a scalar value and requires `from functools import reduce`.
- **Lambda Limitations:** Lambdas are strictly single-expression; use `def` for multi-line logic, error handling, or when functions need documentation.
- **Import Hierarchy:** Python checks `sys.modules` cache first, then `sys.meta_path` finders, and uses `sys.path` to locate `.py` files.
- **Entry Guard:** Always protect top-level runnable code in modules with `if __name__ == "__main__":`.

## 7. Common Mistakes
- **Shadowing Standard Library:** Naming local files `math.py`, `random.py`, or `test.py` causes Python to import the local file instead of the standard library.
- **Calling Instead of Passing in `map()`/`filter()`:** Writing `map(func(), items)` instead of `map(func, items)`.
- **Wildcard Imports (`from module import *`):** Pollutes the namespace and leads to accidental variable shadowing.
- **Empty Iterable in `reduce()`:** Calling `reduce(func, [])` without an initializer raises `TypeError`.

## 8. Practice Questions
1. Use `map()` to convert a list of strings `["10", "20", "30"]` to integers.
2. Given a list of numbers `[5, 12, 18, 25, 30]`, use `filter()` to find numbers divisible by both 2 and 3.
3. Compute the product of numbers from 1 to 5 using `reduce()`.
4. What happens when a script named `random.py` tries to execute `import random`? Explain why.
5. Create a module with a function `is_prime(n)` and demonstrate importing it using an alias.

---

## 📑 Dedicated Topic Notes Index

For in-depth revision notes, detailed step-by-step traces, common pitfalls, and 5+ solved practice questions for each specific topic, refer to:

- [map() Function Notes](file:///c:/python-learning-journey/Chapter%204%20-%20Functions/map_function.md)
- [reduce() Function Notes](file:///c:/python-learning-journey/Chapter%204%20-%20Functions/reduce_function.md)
- [Why Lambda Is Not Used Everywhere Notes](file:///c:/python-learning-journey/Chapter%204%20-%20Functions/why_not_lambda_everywhere.md)
- [Python Modules & Structure Notes](file:///c:/python-learning-journey/Chapter%204%20-%20Functions/modules_in_python.md)
- [The Actual Python Import Hierarchy Notes](file:///c:/python-learning-journey/Chapter%204%20-%20Functions/python_import_hierarchy.md)
- [Module Aliasing Notes](file:///c:/python-learning-journey/Chapter%204%20-%20Functions/module_aliasing.md)
