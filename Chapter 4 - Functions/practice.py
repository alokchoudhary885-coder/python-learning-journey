# Chapter 4 Practice: Functions & Keyword Arguments
# Migrated and improved from class practice (function.py & test.py)

# 1. Defining and Calling Functions
def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


# Testing basic functions
sum_result = add(10, 20)
mul_result = multiply(20, 30)

print("Add (10, 20):", sum_result)
print("Multiply (20, 30):", mul_result)


# 2. Function with Default Arguments
def greet_student(name, course="Python"):
    return f"Hello {name}, welcome to {course}!"


print(greet_student("Alok"))
print(greet_student("Alok", "Data Science"))


# 3. Variable-Length Keyword Arguments (**kwargs)
# Fixed version of test.py: kwargs stores arguments as a dictionary
def print_student_profile(**kwargs):
    print("Type of kwargs:", type(kwargs))
    print("Received attributes:")
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# Correct function call (passing keyword arguments)
print("\nProfile 1:")
print_student_profile(name="Alok", age=21, batch=167)

print("\nProfile 2:")
print_student_profile(course="Python", status="Active")
