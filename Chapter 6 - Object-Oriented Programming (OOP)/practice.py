# Chapter 6 Practice: OOP Variables, Methods, and Lifecycle
# ==========================================================

# 1. Practice Problem 1: Declaring Instance Variables in 3 Ways
class Laptop:
    brand = "Dell"  # Static variable (shared)

    def __init__(self, model):
        # Place 1: Inside constructor
        self.model = model

    def upgrade_ram(self, ram_size):
        # Place 2: Inside instance method
        self.ram = ram_size


print("--- Exercise 1: Three Ways to Declare Variables ---")
lap1 = Laptop("Inspiron 15")
lap1.upgrade_ram("16GB")

# Place 3: Outside class
lap1.storage = "512GB SSD"

print("Laptop Details:", lap1.__dict__)


# 2. Practice Problem 2: Accessing and Deleting Instance Variables
print("\n--- Exercise 2: Accessing and Deleting Instance Variables ---")
print("Access inside: Handled via method or self")
print("Access outside: lap1.brand ->", lap1.brand, "| lap1.model ->", lap1.model)

# Deleting from outside class
print("Deleting 'storage' from outside...")
del lap1.storage
print("After deletion, lap1 attributes:", lap1.__dict__)

# Checking safely with hasattr
if not hasattr(lap1, "storage"):
    print("Verified: 'storage' is no longer present on lap1!")


# 3. Practice Problem 3: Single Shared Value vs Instance Variable
print("\n--- Exercise 3: Single Shared Value in Action ---")
class College:
    college_name = "Apex Institute of Technology"  # Single shared value

    def __init__(self, student_name):
        self.student_name = student_name  # Unique per student


c1 = College("Alok")
c2 = College("Ayush")

print(f"c1: {c1.student_name} studies at {c1.college_name}")
print(f"c2: {c2.student_name} studies at {c2.college_name}")

# Changing college name once updates all students
College.college_name = "Apex University"
print(f"After University Upgrade:")
print(f"c1 sees: {c1.college_name}")
print(f"c2 sees: {c2.college_name}")


# 4. Practice Problem 4: Local Variables Scope
print("\n--- Exercise 4: Local Variables are Temporary ---")
class BillCalculator:
    def calculate_total(self, price, qty):
        tax = 18.0                       # Local variable
        subtotal = price * qty           # Local variable
        total = subtotal + (subtotal * tax / 100)  # Local variable
        return total


calc = BillCalculator()
final_bill = calc.calculate_total(500, 2)
print("Calculated Total Bill: Rs.", final_bill)
print("Does calc have 'subtotal' attribute?", hasattr(calc, "subtotal"))
