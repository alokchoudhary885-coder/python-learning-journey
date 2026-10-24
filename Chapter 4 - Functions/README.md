# Chapter 4 - Functions, Functional Tools & Python Modules

This chapter provides a comprehensive exploration of Python functions, functional programming tools (`map`, `filter`, `reduce`), variable scope, and Python modules and the import system.

## Topics Covered
- Function definition (`def`) and return statements
- **Types of Arguments:** Positional, Keyword, Default, `*args`, and `**kwargs`
- **Variable Scope:** Local vs Global variables, variable shadowing, and the `global` keyword
- **Function Aliasing:** Treating functions as first-class objects
- **Nested Functions:** Inner helper functions and scope encapsulation
- **Ternary Operator:** Conditional expressions (`x if condition else y`)
- **Anonymous Functions:** Single-line `lambda` expressions & why lambda is not used everywhere
- **Functional Tools:**
  - `map()`: Transforming collections with functions and lambdas
  - `filter()`: Extracting elements matching criteria
  - `reduce()`: Cumulative aggregation using `functools`
- **Recursion:** Base cases, recursive cases, and call stack unwinding
- **Python Modules & Imports:**
  - Defining custom modules (`my_module.py`) and importing them (`main.py`)
  - Built-in vs standard library vs third-party modules (`math`, `random`)
  - Module aliasing with `as` (`module_aliasing.py`)
  - The actual Python import hierarchy: `sys.modules`, `sys.meta_path`, `sys.path`, finders, loaders, and preventing module shadowing (`import_hierarchy_demo.py`)

## Files in this Chapter

### Runnable Practice & Demonstration Scripts
- `practice.py`: Basic function declarations, arithmetic operations, and keyword argument handling.
- `types_of_arguments.py`: Comprehensive guide to positional, keyword, default, `*args`, and `**kwargs`.
- `variable_scope.py`: Local vs global variables, namespace behavior, and `global` keyword.
- `function_aliasing.py`: Aliasing function references, memory identity, and deleting original references.
- `nested_functions.py`: Inner helper functions and returning functions.
- `ternary_operator.py`: Inline conditional expressions and compact functions.
- `lambda_functions.py`: Anonymous functions with lambda, ternary operators, and `filter()`.
- `map_function.py`: Comprehensive `map()` demonstrations, multiple iterables, and 5 solved exercises.
- `reduce_function.py`: `reduce()` accumulator mechanics, initializer usage, and map/filter/reduce comparison.
- `lambda_vs_def.py`: Side-by-side comparison of `def` vs `lambda`, PEP 8 guidelines, and debugging stack traces.
- `my_module.py`: Sample user-defined module with functions and `if __name__ == "__main__":` guard.
- `main.py`: Importing and using functions from `my_module.py`.
- `math_module_demo.py`: Standard library `math` module demonstration (constants, rounding, powers, GCD).
- `random_module_demo.py`: Standard library `random` module demo (randint, choice, sample, shuffle, seeds).
- `random_module_functions.py`: Comprehensive guide to random distributions, weighted choices, and practical generators.
- `import_hierarchy_demo.py`: Step-by-step inspection of `sys.modules`, `sys.meta_path`, `sys.path`, and `__file__`.
- `module_aliasing.py`: Aliasing modules and functions with `as`, industry conventions, and best practices.
- `special_variables.py`: Exploration of `__name__`, `__file__`, `__doc__`, `__all__`, and `__dict__`.
- `datetime_module_demo.py`: Standard library `datetime` module demo (now, strftime, strptime, timestamps).
- `datetime_classes_demo.py`: Deep dive into `date`, `time`, `datetime`, `timedelta`, and `timezone` classes.
- `calendar_module_demo.py`: Standard library `calendar` module demo (month grids, isleap, weekday, monthrange).
- `arithmetic_module.py`: Pure business calculation logic module.
- `formatting_module.py`: Text, header, and currency formatting utility module.
- `multiple_modules_demo.py`: Orchestrating calculations and formatting across multiple modules.
- `recursion.py`: Clean recursive factorial implementation with formula expansion.
- `assignment.py`: Nine progressive practical assignments covering all concepts with solutions.

### Topic-Specific Study & Revision Notes
- `notes.md`: Chapter-wide synthesis notes and index.
- `map_function.md`: 10-section guide on `map()` with Q&A.
- `reduce_function.md`: 10-section guide on `reduce()` with Q&A.
- `why_not_lambda_everywhere.md`: 10-section analysis of `lambda` vs `def`.
- `modules_in_python.md`: 10-section guide on predefined and custom modules.
- `random_module.md`: 10-section guide on random functions, weighted selections, and reproducibility.
- `multiple_modules.md`: 10-section guide on coordinating multiple modules and avoiding circular imports.
- `special_variables.md`: 10-section guide on Python special (dunder) variables.
- `datetime_module.md`: 10-section guide on datetime formatting (strftime/strptime) and timestamps.
- `datetime_classes.md`: 10-section guide on date, time, datetime, timedelta, and timezone classes.
- `calendar_module.md`: 10-section guide on calendar generation, leap years, and weekday indexing.
- `python_import_hierarchy.md`: 10-section guide on import mechanics and shadowing risks.
- `module_aliasing.md`: 10-section guide on `import ... as ...` conventions.

## How to Run
Run any script directly from this folder:
```bash
python map_function.py
python reduce_function.py
python lambda_vs_def.py
python main.py
python math_module_demo.py
python random_module_demo.py
python import_hierarchy_demo.py
python module_aliasing.py
python assignment.py
```
