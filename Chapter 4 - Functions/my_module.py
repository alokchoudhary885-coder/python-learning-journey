# Chapter 4: User-Defined Module Example (my_module.py)
# ======================================================
# A module is simply a Python file (.py) containing reusable code:
# functions, classes, and variables.

# Module-level variable
MODULE_VERSION = "1.0.0"
AUTHOR = "Alok Choudhary"


def greet(name):
    """Returns a personalized greeting."""
    return f"Hello, {name}! Welcome to Python Modules."


def calculate_circle_area(radius):
    """Calculates the area of a circle: pi * r^2."""
    pi = 3.14159
    return pi * (radius ** 2)


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


# The __name__ == "__main__" pattern:
# When this file is run directly: __name__ == "__main__" (the test code runs).
# When this file is imported by another file: __name__ == "my_module" (the test code is SKIPPED).
if __name__ == "__main__":
    print("--- Running my_module.py directly as a standalone script ---")
    print("Testing greet():", greet("Developer"))
    print("Testing calculate_circle_area(5):", calculate_circle_area(5))
    print("Testing add(10, 20):", add(10, 20))
    print("Module self-test completed successfully.")
