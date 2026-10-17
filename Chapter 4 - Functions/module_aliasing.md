# Module Aliasing in Python

## 1. Definition
**Module Aliasing** is the practice of renaming an imported module or function in your script using the `as` keyword. The alias acts as an alternative identifier bound to the imported object in your local namespace.

## 2. Why We Use Aliases
- **Typing Efficiency:** Shortens frequently accessed module names (e.g. `m.sqrt()` instead of `math.sqrt()`).
- **Resolving Name Collisions:** When two modules export functions with the same name, aliasing differentiates them clearly.
- **Industry Standardization:** Widely accepted community standards (like `np` for NumPy and `pd` for Pandas) make code universally readable across data science teams.

## 3. Syntax
```python
# 1. Aliasing a whole module
import module_name as alias_name

# 2. Aliasing specific imported functions or classes
from module_name import function_name as custom_name
```

## 4. Simple Explanation of How It Works
When Python encounters `import math as m`:
1. It locates and loads the `math` module into `sys.modules["math"]`.
2. Instead of binding the identifier `math` in your local scope, it binds the identifier `m` to the module object.
3. Writing `m.sqrt(25)` references the exact same module attributes.

## 5. Practical Examples
```python
# Example 1: Module alias
import math as m
print("Pi:", m.pi)

# Example 2: Function alias during import
from math import factorial as fact
print("Factorial of 4:", fact(4))

# Example 3: Resolving naming conflicts between two modules
# Suppose module_a and module_b both have a 'process_data' function:
# from module_a import process_data as process_raw
# from module_b import process_data as process_clean
```

## 6. Expected Output
```text
Pi: 3.141592653589793
Factorial of 4: 24
```

## 7. Important Differences: Module Aliasing vs Function Aliasing
| Feature | Module Aliasing (`as`) | Runtime Function Aliasing |
|---|---|---|
| **Mechanism** | Import statement syntax (`import math as m`) | Assignment statement (`calc = add`) |
| **When it happens** | At the time of module import | Dynamically during code execution |
| **Use case** | Renaming imported modules or functions | Passing functions as callbacks or shorthand variables |
| **Namespace impact** | Original name is never imported into local scope | Both original name and alias coexist in scope |

## 8. Common Mistakes
1. **Cryptic Single-Letter Aliases:** Renaming modules to arbitrary letters like `import math as x` or `import datetime as d` makes code obscure.
2. **Breaking Standard Conventions:** Using non-standard aliases like `import pandas as pan` or `import numpy as num` confuses collaborators. Always adhere to `np` and `pd`.
3. **Using Original Name After Aliasing:** If you write `import math as m`, trying to write `math.sqrt()` causes `NameError: name 'math' is not defined`.

## 9. Short Revision Notes
- Use `as` to assign an alias.
- Common conventions: `np` for NumPy, `pd` for Pandas, `plt` for `matplotlib.pyplot`.
- If an alias is declared with `import x as y`, only `y` is accessible in that file.
- Aliasing is essential for resolving name collisions between libraries.

## 10. Practice Questions with Answers

### Q1. What happens if you run `import math as m` and then try to call `math.sqrt(9)`?
**Answer:** It raises `NameError: name 'math' is not defined` because the original identifier `math` was not bound to the local namespace; only `m` was bound.

### Q2. How do you import the `random` module with the alias `rd`?
**Answer:**
```python
import random as rd
```

### Q3. Write an import statement that imports only `randint` from `random` and renames it to `rand_int`.
**Answer:**
```python
from random import randint as rand_int
```

### Q4. Mention three industry-standard aliases used in Python data science.
**Answer:**
1. `import numpy as np`
2. `import pandas as pd`
3. `import matplotlib.pyplot as plt`

### Q5. How does `import math as m` differ from `plus = add` in terms of how the alias is created?
**Answer:** `import math as m` creates the alias at import-time using Python's `as` keyword syntax, binding only `m` in scope. `plus = add` creates an alias at runtime via an assignment statement, leaving both `add` and `plus` bound in the scope.
