# Chapter 2 - Assignment: Data Types and Operators
# ===================================================
# Problem 1: Smart Temperature Converter (Celsius to Fahrenheit & Kelvin)
# Problem 2: Bill Split Calculator with Data Type Inspection
# Problem 3: Operator Precedence & Float Arithmetic Output Analysis
# Problem 4: Keyword Correction

# --- Solution 1: Temperature Converter ---
print("--- Problem 1: Temperature Converter ---")
celsius_input = input("Enter temperature in Celsius (or press Enter for default 25): ")
celsius = float(celsius_input) if celsius_input.strip() else 25.0

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15

print("Celsius:", celsius)
print("Fahrenheit:", fahrenheit)
print("Kelvin:", kelvin)


# --- Solution 2: Bill Split Calculator ---
print("\n--- Problem 2: Bill Split Calculator ---")
bill_input = input("Enter total bill (or press Enter for default 1200): ")
friends_input = input("Enter number of friends (or press Enter for default 4): ")

total_bill = float(bill_input) if bill_input.strip() else 1200.0
friends = int(friends_input) if friends_input.strip() else 4

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