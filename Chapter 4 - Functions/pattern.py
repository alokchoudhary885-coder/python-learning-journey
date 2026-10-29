# Star and Number Patterns in Python
# ===================================

# 1. Right-Angled Triangle Pattern
print("--- 1. Right-Angled Triangle ---")
rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end=" ")
    print()

# 2. Number Triangle
print("\n--- 2. Number Triangle ---")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()

# 3. Half Diamond Star Pattern
print("\n--- 3. Half Diamond Star Pattern ---")
n = 4
for i in range(1, n + 1):
    print("* " * i)
for i in range(n - 1, 0, -1):
    print("* " * i)
