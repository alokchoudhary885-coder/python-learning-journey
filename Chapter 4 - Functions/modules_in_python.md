# Python Modules: User-Defined and Predefined Modules

## 1. Definition
A **module** in Python is simply a file with a `.py` extension containing Python definitions (functions, variables, and classes) and statements. Modules allow you to logically group and reuse code across multiple programs.

## 2. Why We Use Modules
- **Maintainability:** Breaks large monolithic programs into small, organized, manageable files.
- **Reusability:** Write a function once in a module and reuse it across multiple projects.
- **Namespace Separation:** Prevents variable and function name collisions by grouping definitions under the module's name.

## 3. Syntax
```python
# 1. Import entire module
import my_module
my_module.some_function()

# 2. Import specific items
from my_module import some_function, some_variable
some_function()

# 3. Import everything (generally discouraged!)
from my_module import *

# 4. Module entry point guard
if __name__ == "__main__":
    # Runs ONLY when this file is executed directly
    pass
```

## 4. Simple Explanation of How Modules Work
1. **Module vs Package vs Library:**
   - **Module:** A single `.py` file (e.g., `math.py`, `my_module.py`).
   - **Package:** A directory containing multiple modules and an `__init__.py` file (e.g., `numpy`, `email`).
   - **Library:** A broad collection of packages and modules designed for a specific domain (e.g., standard library, Matplotlib).
2. **Built-in vs Standard Library vs User-Defined:**
   - **Built-in Modules:** Compiled directly into the Python interpreter binary (written in C, like `sys`, `math`, `time`). No external file needed.
   - **Standard Library Modules:** Shipped with standard Python installation as `.py` files inside the `Lib/` folder (like `random`, `datetime`, `os`).
   - **User-Defined Modules:** Custom `.py` files created by developers in their project workspace.
   - **Third-Party Modules:** External packages installed via `pip` (e.g., `requests`, `pandas`).
3. **Execution on Import:**
   - When Python imports a module for the first time, it compiles it to bytecode and executes all top-level statements.
   - It places the module object into `sys.modules` cache so subsequent imports don't re-run the file.

## 5. Practical Examples
```python
# File: math_operations.py
def add(x, y):
    return x + y

def multiply(x, y):
    return x * y

if __name__ == "__main__":
    print("Self-test: add(2, 3) =", add(2, 3))

# File: app.py
import math_operations

result = math_operations.multiply(4, 5)
print("Product:", result)
```

## 6. Expected Output
When running `app.py`:
```text
Product: 20
```
*(Notice that the self-test print inside `if __name__ == '__main__':` does NOT execute!)*

## 7. Important Differences from Related Concepts
| Feature | `import module` | `from module import func` | `from module import *` |
|---|---|---|---|
| **Namespace** | Kept inside `module.` namespace | `func` added to local namespace | All names dumped into local namespace |
| **Clarity** | Very clear where each function came from | Clear which specific function was imported | Unclear origin; highly error-prone |
| **Collision Risk**| Zero collision risk | Low risk (only if name already exists locally) | Extremely high risk of variable shadowing |

## 8. Common Mistakes
1. **Using `from module import *`:** Dumps dozens of unknown names into your file, overwriting existing functions without warning.
2. **Omitting `if __name__ == "__main__":`:** Any test code or print statements at module level will execute automatically whenever another file imports it.
3. **Module Naming Conflicts:** Naming your script `random.py` or `math.py` shadows the standard library, breaking Python's internal imports.

## 9. Short Revision Notes
- Any `.py` file can be imported as a module.
- `__name__` equals `"__main__"` when run directly, but equals the module's name (e.g. `"my_module"`) when imported.
- Standard library modules come pre-installed with Python; third-party packages need `pip install`.
- Always prefer `import module` or `from module import specific_function` over wildcard `*` imports.

## 10. Practice Questions with Answers

### Q1. What is the difference between a module and a package in Python?
**Answer:** A module is a single `.py` file containing Python code. A package is a directory containing multiple modules and an `__init__.py` file (or organized as a namespace package).

### Q2. Why is `from math import *` discouraged in production code?
**Answer:** It pollutes the local namespace with all names from `math`, making it impossible to see where functions originated and risking accidental variable overwriting.

### Q3. What is the value of `__name__` when a module is imported by another script?
**Answer:** It holds the string name of the module itself (e.g., `"my_module"`), not `"__main__"`.

### Q4. Are built-in modules and standard library modules exactly the same?
**Answer:** No. Built-in modules (like `sys`) are compiled directly into the CPython interpreter binary. Standard library modules (like `random.py`) are written in Python and located in Python's `Lib/` folder on disk. Both ship pre-installed with Python.

### Q5. Write a small user-defined module `converter.py` with a function `km_to_miles(km)` and show how to import and use it.
**Answer:**
```python
# converter.py
def km_to_miles(km):
    return km * 0.621371

# main.py
import converter
print("10 km in miles:", converter.km_to_miles(10))
```
