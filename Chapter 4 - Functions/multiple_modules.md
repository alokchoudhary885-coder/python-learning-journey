# Working with Multiple Modules in Python

## 1. Definition
Working with **multiple modules** means organizing a program into separate Python files (`.py`), where each file is responsible for a distinct part of the system (such as calculations, formatting, database operations, or user interface).

## 2. Why We Use Multiple Modules
- **Separation of Concerns:** Each module handles one specific domain (e.g., `arithmetic_module.py` for calculations, `formatting_module.py` for text formatting).
- **Maintainability:** Easier to locate and fix bugs in focused files rather than scrolling through a thousands-of-lines single file.
- **Team Collaboration:** Different team members can work on different modules simultaneously without merge conflicts.
- **Reusability:** Utility modules can be shared across multiple projects.

## 3. Syntax
```python
# Importing multiple custom modules in your main script
import arithmetic_module as calc
import formatting_module as fmt

# Using functions across modules
total = calc.compute_final_price(1000)
formatted_total = fmt.format_currency(total["final_total"])
```

## 4. Simple Explanation of How It Works
1. Each module file is parsed and compiled to bytecode on its first import.
2. Python caches every loaded module in `sys.modules`.
3. If Module A and Module B are imported into `main.py`, Python ensures both are loaded and provides distinct namespaces (`calc.` and `fmt.`), preventing variable name clashes.

## 5. Practical Example
```python
# arithmetic_module.py
def add_tax(amount, rate=0.05):
    return amount * (1 + rate)

# formatting_module.py
def format_inr(val):
    return f"Rs. {val:,.2f}"

# app.py
import arithmetic_module as calc
import formatting_module as fmt

bill = calc.add_tax(500)
print(fmt.format_inr(bill))  # Rs. 525.00
```

## 6. Expected Output
```text
Rs. 525.00
```

## 7. Important Differences: Single File vs Multi-Module Architecture
| Feature | Single File Approach | Multi-Module Architecture |
|---|---|---|
| **Code Structure** | Monolithic (everything in one script) | Modular (logical division by responsibility) |
| **Name Collisions** | High risk of variable shadowing | Low risk (names isolated inside module namespaces) |
| **Testing** | Hard to isolate and test single components | Easy to test each module independently |
| **Scalability** | Becomes unmanageable as project grows | Scales cleanly with project requirements |

## 8. Common Mistakes
1. **Circular Imports:** If `module_a.py` imports `module_b.py`, and `module_b.py` imports `module_a.py` at top level, Python raises `ImportError: cannot import name ... from partially initialized module`.
   - *Fix:* Reorganize shared logic into a third common module (e.g., `common.py`) or move imports inside functions.
2. **Missing `if __name__ == "__main__":`:** Without this guard, test prints in imported modules will run unexpectedly in other files.
3. **Wrong Working Directory:** Running `python main.py` from outside the module folder without `PYTHONPATH` configured can cause `ModuleNotFoundError`.

## 9. Short Revision Notes
- Break code into modules based on logical responsibility.
- Use meaningful aliases (`as calc`, `as fmt`) for cleaner calling code.
- Avoid circular dependencies between modules.
- Protect all standalone module test code with `if __name__ == "__main__":`.

## 10. Practice Questions with Answers

### Q1. What is the main benefit of dividing code into multiple modules?
**Answer:** Separation of concerns, code reusability, easier testing, and preventing namespace collisions.

### Q2. What causes a `circular import` error in Python?
**Answer:** When two or more modules depend on each other directly at top-level import time (e.g., A imports B while B imports A before either is fully initialized).

### Q3. How can you solve a circular import problem?
**Answer:**
1. Extract shared variables or functions into a third helper module that both can import.
2. Move the import statement inside the specific function that needs it (local import).

### Q4. If two different modules have a function named `save()`, how do you use both in the same file without conflict?
**Answer:** Use module namespaces or aliases:
```python
import user_module as user
import order_module as order

user.save()
order.save()
```

### Q5. Why should every module include an `if __name__ == "__main__":` block?
**Answer:** It allows the module to be run directly for testing/debugging while preventing that test code from running when the file is imported elsewhere.
