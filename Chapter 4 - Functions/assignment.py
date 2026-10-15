# Chapter 4 - Assignment: Functions, Recursion, Scope & Functional Tools
# =======================================================================
# Task 1: Write a function `calculate_power(base, exp)` that computes base^exp.
# Task 2: Write a function `calculate_average(*numbers)` that accepts variable numbers and returns average.
# Task 3: Write a recursive function `sum_of_digits(n)` that returns the sum of digits of a number.
# Task 4: Write a visitor counter using a global variable `visitor_count` and a function `register_visitor()`.
# Task 5: Demonstrate function aliasing and a nested helper function for currency formatting.
# Task 6: Use a lambda function with ternary operator and `filter()` to filter passing marks (>= 40).

# --- Solution 1: Power Function ---
def calculate_power(base, exp):
    """Calculates base raised to exponent exp."""
    result = 1
    for _ in range(exp):
        result *= base
    return result


# --- Solution 2: Average with *args ---
def calculate_average(*numbers):
    """Calculates the average of arbitrary numerical arguments."""
    if not numbers:
        return 0.0
    return sum(numbers) / len(numbers)


# --- Solution 3: Recursive Sum of Digits ---
def sum_of_digits(n):
    """
    Recursively calculates sum of digits of a positive integer.
    Base case: Single digit number (n < 10) returns n.
    Recursive case: (n % 10) + sum_of_digits(n // 10).
    """
    n = abs(n)
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)


# --- Solution 4: Global Variable Visitor Counter ---
visitor_count = 0


def register_visitor(visitor_name):
    """Increments the global visitor_count and welcomes the visitor."""
    global visitor_count
    visitor_count += 1
    return f"Welcome {visitor_name}! You are visitor #{visitor_count}."


# --- Solution 5: Function Aliasing & Nested Helper ---
def invoice_generator(customer, amount):
    """Outer function using nested helper to format amount."""
    def format_inr(val):
        return f"Rs. {val:,.2f}"

    return f"Invoice for {customer}: {format_inr(amount)}"


# Create an alias for invoice_generator
generate_bill = invoice_generator


# --- Solution 6: Lambda, Ternary Operator & filter() ---
# Lambda with ternary operator to label marks
grade_label = lambda m: "Passed" if m >= 40 else "Failed"


if __name__ == "__main__":
    print("--- Task 1: Power Calculation ---")
    print("2^5 =", calculate_power(2, 5))
    print("3^3 =", calculate_power(3, 3))

    print("\n--- Task 2: Variable Arguments Average ---")
    print("Average of (10, 20, 30):", calculate_average(10, 20, 30))
    print("Average of (5, 15, 25, 35, 45):", calculate_average(5, 15, 25, 35, 45))

    print("\n--- Task 3: Recursive Sum of Digits ---")
    number = 12345
    print(f"Sum of digits of {number}:", sum_of_digits(number))
    print(f"Sum of digits of 987:", sum_of_digits(987))

    print("\n--- Task 4: Global Variable Visitor Counter ---")
    print(register_visitor("Alok"))
    print(register_visitor("Rahul"))
    print(register_visitor("Priya"))
    print("Final total visitors recorded:", visitor_count)

    print("\n--- Task 5: Function Aliasing & Nested Helper ---")
    print(generate_bill("Alok Enterprises", 15400.50))
    print("Is alias identical to original?:", generate_bill is invoice_generator)

    print("\n--- Task 6: Lambda, Ternary & filter() ---")
    scores = [25, 55, 38, 70, 85, 39, 92]
    passed_scores = list(filter(lambda s: s >= 40, scores))
    print("Original Scores:", scores)
    print("Passed Scores (>= 40):", passed_scores)
    print("Score 38 status:", grade_label(38))
    print("Score 70 status:", grade_label(70))
