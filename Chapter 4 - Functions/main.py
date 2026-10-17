# Chapter 4: Importing and Using a User-Defined Module (main.py)
# ==============================================================
# This script demonstrates how Python imports and executes a custom module.

# 1. Importing the entire module
import my_module

# 2. Importing specific functions from a module
from my_module import calculate_circle_area, greet

if __name__ == "__main__":
    print("--- 1. Using Functions Imported from my_module ---")
    
    # Calling via the module namespace:
    message = my_module.greet("Alok")
    print("Greeting:", message)
    
    # Accessing module-level variables:
    print("Module Author :", my_module.AUTHOR)
    print("Module Version:", my_module.MODULE_VERSION)

    # Calling directly imported function:
    area = calculate_circle_area(7)
    print(f"Area of circle with radius 7: {area:.2f}")

    # Using add() via module prefix
    sum_result = my_module.add(45, 55)
    print("Sum of 45 + 55:", sum_result)

    print("\n--- 2. Understanding __name__ and Module Location ---")
    print("In this file (main.py), __name__ is        :", __name__)
    print("In the imported module, my_module.__name__ is:", my_module.__name__)
    print("Path of imported my_module on disk       :", my_module.__file__)
    print("\nNotice that the test prints inside my_module's `if __name__ == '__main__':` block did NOT run here!")
