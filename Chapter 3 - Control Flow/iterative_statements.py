# Iterative Statements in Python: For Loops, While Loops, and Loop Control
# =========================================================================


# --- 1. For Loop with range() ---
print("--- 1. For Loops with range() ---")
print("Counting 1 to 5:")
for num in range(1, 6):
    print(num, end=" ")
print()

print("Even numbers (step=2):")
for even in range(2, 11, 2):
    print(even, end=" ")
print()

print("Countdown (negative step):")
for count in range(5, 0, -1):
    print(count, end=" ")
print()


# --- 2. Iterating Over Sequences (Strings, Lists) ---
print("\n--- 2. Iterating Over Sequences ---")
tech_stack = ["Python", "FastAPI", "PostgreSQL", "Docker"]
for tech in tech_stack:
    print(f"Skill: {tech}")

# Iterating with index using enumerate()
print("\nIndexed skills:")
for idx, skill in enumerate(tech_stack, start=1):
    print(f"{idx}. {skill}")


# --- 3. While Loop ---
print("\n--- 3. While Loop (Power of 2 Doubling) ---")
value = 1
while value <= 32:
    print(value, end=" ")
    value *= 2
print()


# --- 4. Loop Control Statements: break, continue, pass ---
print("\n--- 4. Loop Control Keywords ---")

# 'continue': Skips the current iteration
print("Printing odd numbers using continue (1-9):")
for n in range(1, 10):
    if n % 2 == 0:
        continue
    print(n, end=" ")
print()

# 'break': Terminates the loop prematurely
print("Stopping search on first match with break:")
numbers = [12, 45, 78, 99, 23, 56]
target = 99
for item in numbers:
    if item == target:
        print(f"Found target {target}! Breaking out of loop.")
        break
    print(f"Checking {item}...")


# --- 5. The Python for...else and while...else Construct ---
print("\n--- 5. for...else Construct (Linear Search) ---")
# In Python, 'else' after a loop runs ONLY if the loop finishes NATURALLY (without break)!
def search_product(catalog, search_item):
    for product in catalog:
        if product.lower() == search_item.lower():
            print(f"Product '{search_item}' is in stock!")
            break
    else:
        print(f"Product '{search_item}' was NOT found in catalog.")


store_items = ["Mouse", "Keyboard", "Monitor", "Webcam"]
search_product(store_items, "keyboard")
search_product(store_items, "printer")


# --- 6. Nested Loops (Multiplication Grid) ---
print("\n--- 6. Nested Loops (3x3 Matrix Grid) ---")
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:2d}", end=" ")
    print()
