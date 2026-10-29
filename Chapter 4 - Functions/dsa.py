import sys

# DSA Practice: Number Pattern / Floyd's Triangle using a Single Loop
# ====================================================================

def get_input(prompt, default="4"):
    if not sys.stdin.isatty():
        print(f"{prompt}{default} (auto-selected)")
        return default
    try:
        val = input(prompt).strip()
        return val if val else default
    except (EOFError, KeyboardInterrupt):
        return default


raw_input = get_input("Enter the number of rows (press Enter for default 4): ", default="4")
n = int(raw_input) if raw_input.isdigit() else 4

print(f"\nPrinting Floyd's Triangle ({n} rows):")
i = row = 1

while i <= n * (n + 1) // 2:
    print(f"{i:2d}", end=" ")
    if i == row * (row + 1) // 2:
        print()
        row += 1
    i += 1
