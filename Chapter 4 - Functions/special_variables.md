# Python Special (Dunder) Variables

## 1. Definition
**Special variables** in Python (often called **dunder variables**, short for *double underscore*) are pre-defined system attributes managed automatically by the Python runtime to store module metadata, execution context, and namespace information.

## 2. Why We Use Special Variables
- **Execution Control:** `__name__` allows a single file to act as both an executable script and an importable library.
- **File Introspection:** `__file__` locates assets, templates, or relative data files from disk.
- **Documentation:** `__doc__` allows automated generation of documentation from comments.
- **Export Control:** `__all__` provides an explicit list of public functions and variables for safe imports.
- **Dynamic Introspection:** `__dict__` provides direct access to the internal symbol table.

## 3. Syntax & Common Special Variables
| Special Variable | Type | Description |
|---|---|---|
| `__name__` | `str` | `"__main__"` when run directly; module's name when imported |
| `__file__` | `str` | Absolute/relative file system path to the current module |
| `__doc__` | `str` | Triple-quoted documentation string of the module/function |
| `__all__` | `list` | List of public names exported on `from module import *` |
| `__dict__` | `dict` | Symbol dictionary mapping names to objects in the namespace |
| `__package__` | `str` | Name of the parent package (or `""` if top-level) |
| `__annotations__` | `dict` | Type annotations defined on variables or functions |

## 4. Simple Explanation of How They Work
- When Python loads a `.py` file, the interpreter automatically populates these attributes before executing the code.
- If executed from terminal (`python app.py`), Python assigns `__name__ = "__main__"`.
- If another script executes `import app`, Python assigns `__name__ = "app"`.

## 5. Practical Example
```python
"""Module for User Authentication."""

__all__ = ["login"]

def login(user):
    """Authenticates the user."""
    return f"{user} logged in"

def _secret_hash():
    return "12345"

if __name__ == "__main__":
    print("Module Doc :", __doc__)
    print("Module Name:", __name__)
    print("Script Path:", __file__)
    print("Public API :", __all__)
```

## 6. Expected Output
```text
Module Doc : Module for User Authentication.
Module Name: __main__
Script Path: C:\path\to\auth.py
Public API : ['login']
```

## 7. Important Differences: `__name__` in Direct Execution vs Import
| Context | Command | Value of `__name__` | `if __name__ == '__main__':` |
|---|---|---|---|
| **Direct script execution** | `python auth.py` | `"__main__"` | Evaluates to `True` (runs tests) |
| **Imported by other file** | `import auth` | `"auth"` | Evaluates to `False` (skipped) |

## 8. Common Mistakes
1. **Misspelling Dunder Names:** Writing `_name_` or `__Name__` instead of `__name__` raises `NameError`.
2. **Accessing `__file__` on Built-in Modules:** Built-in C modules (like `sys`) do not have a `__file__` attribute; doing `sys.__file__` raises `AttributeError`.
3. **Misunderstanding `__all__`:** Thinking `__all__` prevents `import my_module.private_func`. `__all__` ONLY restricts wildcard imports (`from my_module import *`).

## 9. Short Revision Notes
- Dunder = double underscore on both sides (`__variable__`).
- `__name__ == "__main__"` is the universal Python boilerplate for script entry points.
- `__file__` gives the path of the script on disk.
- `__doc__` exposes docstrings to Python's `help()` function.
- `__all__` controls wildcard exports.

## 10. Practice Questions with Answers

### Q1. What does `__name__` evaluate to when a module is imported by another script?
**Answer:** It evaluates to the module's string name (e.g., `"my_module"`), not `"__main__"`.

### Q2. How can you find the path of a script at runtime using Python code?
**Answer:** By inspecting `__file__`:
```python
import os
print(os.path.abspath(__file__))
```

### Q3. What is the purpose of defining `__all__ = ["add", "subtract"]` in a module?
**Answer:** It restricts `from module import *` to only export `add` and `subtract`, hiding all other functions and variables from wildcard imports.

### Q4. Does the `sys` module have a `__file__` attribute? Why or why not?
**Answer:** No. `sys` is compiled directly into the CPython binary as a built-in module, so it does not exist as a `.py` file on disk.

### Q5. How do you print the docstring of a function named `calculate_area` programmatically?
**Answer:**
```python
print(calculate_area.__doc__)
```
