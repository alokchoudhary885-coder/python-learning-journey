import sys

# Chapter 2 - Assignment: Data Types and Operators
# ===================================================
# Problem 1: Smart Temperature Converter (Celsius to Fahrenheit & Kelvin)
# Problem 2: Bill Split Calculator with Data Type Inspection
# Problem 3: Operator Precedence & Float Arithmetic Output Analysis
# Problem 4: Keyword Correction

def prompt_user(prompt_text, default_val):
    if sys.stdin.isatty():
        try:
            val = input(prompt_text).strip()
            return val if val else default_val
        except (EOFError, KeyboardInterrupt):
            return default_val
    else:
        print(f"{prompt_text}{default_val} (auto-selected)")
        return default_val


# --- Solution 1: Temperature Converter ---
print("--- Problem 1: Temperature Converter ---")
celsius_str = prompt_user("Enter temperature in Celsius (or press Enter for default 25): ", "25")
celsius = float(celsius_str)

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


# --- Solution 2: Bill Split Calculator ---
print("\n--- Problem 2: Bill Split Calculator ---")
bill_str = prompt_user("Enter total bill (or press Enter for default 1200): ", "1200")
friends_str = prompt_user("Enter number of friends (or press Enter for default 4): ", "4")

total_bill = float(bill_str)
friends = int(friends_str)

each_person = total_bill / friends

print("Total Bill: Rs.", total_bill, "| Type:", type(total_bill))
print("Friends:", friends, "| Type:", type(friends))
print("Each Person Pays: Rs.", each_person, "| Type:", type(each_person))


# --- Solution 3: Output Based Questions ---
print("\n--- Problem 3: Output Based Analysis ---")
x = 5
y = 2.0

print("x // y =", x // y, "| Type:", type(x // y))  # Returns 2.0 (float due to float operand)
print("x ** y =", x ** y, "| Type:", type(x ** y))  # Returns 25.0


# --- Solution 4: Corrected Keyword Example ---
print("\n--- Problem 4: Keyword Handling ---")
# 'pass' and 'for' are Python keywords and cannot be used as variable names.
# Corrected variable name:
number = 10
print("Valid variable value:", number)
