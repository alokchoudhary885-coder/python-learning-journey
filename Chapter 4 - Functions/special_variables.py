"""Demonstration of Python Special (Dunder) Variables.
This module showcases __name__, __file__, __doc__, __all__, and __dict__.
"""

# __all__ defines what is exported when 'from special_variables import *' is used
__all__ = ["greet_user", "APP_NAME"]

APP_NAME = "Python Learning Hub"
_INTERNAL_KEY = "SECRET_123"  # Not in __all__, so not exported in wildcard import


def greet_user(name: str) -> str:
    """Returns a greeting message for a user."""
    return f"Welcome, {name}!"


def _private_helper():
    return "This is private."


if __name__ == "__main__":
    print("--- 1. Module Docstring (__doc__) ---")
    print("Module Docstring:\n", __doc__.strip())

    print("\n--- 2. Module Execution Context (__name__) ---")
    print("Value of __name__:", __name__)
    print("Is this script running directly?:", __name__ == "__main__")

    print("\n--- 3. File Location (__file__) ---")
    print("Path to this file:", __file__)

    print("\n--- 4. Public API Definition (__all__) ---")
    print("Exported symbols (__all__):", __all__)

    print("\n--- 5. Function Docstring & Annotations ---")
    print("greet_user docstring  :", greet_user.__doc__)
    print("greet_user annotations:", greet_user.__annotations__)

    print("\n--- 6. Namespace Inspection (globals() & object.__dict__) ---")
    # globals() returns the dictionary implementing the current module's namespace
    module_namespace = globals()
    print("Number of items in module namespace:", len(module_namespace))
    print("Has APP_NAME in globals()?          :", "APP_NAME" in module_namespace)
    print("Value of APP_NAME from globals()    :", module_namespace["APP_NAME"])
    print("greet_user function __dict__        :", greet_user.__dict__)
