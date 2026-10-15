# Chapter 1 - Assignment: Python Fundamentals
#
# Task 1: Declare variables for product name, quantity, and price per unit.
# Calculate and print the total cost.
#
# Task 2: Write an if-else block with proper indentation to check if a number is positive,
# negative, or zero.
#
# Task 3: Use single-line and multi-line comments to explain your logic.

# Solution for Task 1: Total Cost Calculator
product_name = "Notebook"
quantity = 5
price_per_unit = 45.0

total_cost = quantity * price_per_unit
print("Product:", product_name)
print("Quantity:", quantity)
print("Price per unit: Rs.", price_per_unit)
print("Total Cost: Rs.", total_cost)

# Solution for Task 2: Number Sign Checker
check_number = 15

if check_number > 0:
    print(check_number, "is Positive")
elif check_number < 0:
    print(check_number, "is Negative")
else:
    print("The number is Zero")
