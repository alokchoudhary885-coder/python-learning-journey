# Chapter 4: Function Aliasing in Python
# =======================================
# In Python, functions are first-class objects.
# We can assign an existing function to a new variable name.
# This is called Function Aliasing.

def greet(name):
    """Prints a greeting for the given name."""
    return f"Hello, {name}!"


def add(a, b):
    """Returns the sum of two numbers."""
    return a + b


if __name__ == "__main__":
    print("--- 1. Basic Function Aliasing ---")
    # Giving 'greet' an alternative name 'welcome'
    # Notice: We do NOT use parentheses () because we are assigning the function object, not calling it.
    welcome = greet

    print("Calling using original name:", greet("Alok"))
    print("Calling using alias name   :", welcome("Alok"))

    # Both refer to the exact same object in memory
    print("Memory ID of greet  :", id(greet))
    print("Memory ID of welcome:", id(welcome))
    print("Are they identical? :", greet is welcome)

    print("\n--- 2. Deleting the Original Reference ---")
    sum_numbers = add
    print("Sum using alias:", sum_numbers(15, 25))

    # Even if we delete the original reference 'add', the function object
    # still exists in memory as long as 'sum_numbers' points to it!
    del add

    print("Sum using alias after deleting original 'add':", sum_numbers(30, 40))

    try:
        # Trying to call 'add' will now raise a NameError
        add(1, 2)
    except NameError as error:
        print("Expected error when calling deleted name:", error)
