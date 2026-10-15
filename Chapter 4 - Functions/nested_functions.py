# Chapter 4: Nested Functions (Inner Functions) in Python
# =========================================================
# A nested function is a function defined inside another function.
# Inner functions are protected from global access and can serve as private helpers.

# 1. Simple Nested Function
def outer_greeting(student_name):
    print("Inside outer_greeting(): Setting up student profile")

    # Inner function defined within outer_greeting
    def format_title():
        return f"Student: {student_name.strip().title()}"

    # Outer function calls the inner function
    formatted_name = format_title()
    return f"Welcome, {formatted_name}!"


# 2. Nested Function as a Helper for Computations
def calculate_grade(marks_list):
    """Outer function to compute final letter grade."""
    
    # Inner helper function to calculate percentage
    def compute_percentage():
        total = sum(marks_list)
        return (total / (len(marks_list) * 100)) * 100

    percentage = compute_percentage()
    print(f"Percentage calculated by helper: {percentage:.2f}%")

    if percentage >= 90:
        return "Grade A"
    elif percentage >= 75:
        return "Grade B"
    elif percentage >= 50:
        return "Grade C"
    else:
        return "Grade F"


# 3. Returning an Inner Function (Function Factory Pattern)
def make_multiplier(factor):
    """Outer function returns the inner multiplier function."""
    def multiply(number):
        return number * factor
    return multiply


if __name__ == "__main__":
    print("--- 1. Simple Nested Function ---")
    message = outer_greeting("   alok choudhary  ")
    print("Result:", message)

    # Note: Calling format_title() here directly will fail with NameError
    # format_title()  # NameError: name 'format_title' is not defined

    print("\n--- 2. Helper Nested Function ---")
    marks = [85, 78, 92, 88]
    grade = calculate_grade(marks)
    print("Final Result:", grade)

    print("\n--- 3. Returning an Inner Function ---")
    double = make_multiplier(2)
    triple = make_multiplier(3)

    print("Double of 10:", double(10))
    print("Triple of 10:", triple(10))
