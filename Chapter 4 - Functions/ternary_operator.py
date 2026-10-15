# Chapter 4: Ternary Operator (Conditional Expressions) in Python
# ===============================================================
# Syntax:
#     value_if_true if condition else value_if_false
#
# The ternary operator evaluates a condition and returns one of two values in a single line.

# 1. Checking Even or Odd
number = 17
result = "Even" if number % 2 == 0 else "Odd"
print(f"Number {number} is: {result}")


# 2. Assigning Pass or Fail Status
marks = 68
status = "Pass" if marks >= 40 else "Fail"
print(f"Marks: {marks} -> Status: {status}")


# 3. Finding Maximum of Two Numbers
a = 45
b = 82
max_value = a if a > b else b
print(f"Max between {a} and {b} is: {max_value}")


# 4. Using Ternary Operator Inside Functions
def get_ticket_price(age):
    """Returns discounted ticket price based on age in a concise line."""
    return 50 if age < 12 else (70 if age >= 60 else 100)


# 5. Comparing Traditional if-else with Ternary Operator
def check_sign_traditional(n):
    if n >= 0:
        return "Positive or Zero"
    else:
        return "Negative"


def check_sign_ternary(n):
    return "Positive or Zero" if n >= 0 else "Negative"


if __name__ == "__main__":
    print("\n--- Ticket Prices using Ternary Inside Function ---")
    print("Child (age 8)   : Rs.", get_ticket_price(8))
    print("Adult (age 25)  : Rs.", get_ticket_price(25))
    print("Senior (age 65) : Rs.", get_ticket_price(65))

    print("\n--- Comparing Traditional vs Ternary ---")
    print("Traditional (-5):", check_sign_traditional(-5))
    print("Ternary (-5)    :", check_sign_ternary(-5))
