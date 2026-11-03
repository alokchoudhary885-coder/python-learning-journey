# Python Tuples: Creation, Immutability, Packing, Unpacking, and Operations
# =========================================================================
# A tuple is an ordered, IMMUTABLE sequence of elements enclosed in parentheses ().


# --- 1. Tuple Creation & The Single-Element Comma Trap ---
print("--- 1. Tuple Creation ---")
coordinates = (10.5, 20.8)
colors = ("Red", "Green", "Blue", "Green")

print("Coordinates tuple:", coordinates)
print("Type of coordinates:", type(coordinates))

# Crucial Beginner Trap: A single item in parentheses without a comma is NOT a tuple!
not_a_tuple = ("Python")
is_a_tuple = ("Python",)

print(f"('Python')  -> Type: {type(not_a_tuple)} (String!)")
print(f"('Python',) -> Type: {type(is_a_tuple)} (Tuple!)")


# --- 2. Indexing and Slicing ---
print("\n--- 2. Indexing & Slicing ---")
numbers = (10, 20, 30, 40, 50, 60)
print("First element  :", numbers[0])
print("Last element   :", numbers[-1])
print("Slice [1:4]    :", numbers[1:4])
print("Reversed tuple :", numbers[::-1])


# --- 3. Immutability in Action ---
print("\n--- 3. Immutability Demonstration ---")
# Tuples cannot be modified after creation
try:
    numbers[0] = 999
except TypeError as err:
    print("Caught Expected TypeError:", err)

# Note: If a tuple contains a mutable object (like a list), that list can be modified!
nested_tuple = (1, 2, ["A", "B"])
print("Before modifying nested list:", nested_tuple)
nested_tuple[2].append("C")
print("After modifying nested list :", nested_tuple)


# --- 4. Tuple Packing and Unpacking ---
print("\n--- 4. Packing and Unpacking ---")
# Packing: Combining multiple values into a single tuple
student_record = 101, "Alok", "Computer Science", 92.5
print("Packed tuple:", student_record)

# Unpacking: Extracting elements into separate variables
roll, name, dept, score = student_record
print(f"Unpacked -> Roll: {roll}, Name: {name}, Dept: {dept}, Score: {score}")

# Extended Unpacking with asterisk (*)
data = (1, 2, 3, 4, 5, 6)
first, *middle, last = data
print(f"First: {first} | Middle list: {middle} | Last: {last}")


# --- 5. Tuple Methods (count, index) ---
print("\n--- 5. Built-in Tuple Methods ---")
grades = ("A", "B", "A", "C", "A", "B")
print("Grades tuple:", grades)
print("Count of 'A' :", grades.count("A"))
print("First index of 'C':", grades.index("C"))


# --- 6. Returning Multiple Values from Functions ---
print("\n--- 6. Returning Multiple Values via Tuple ---")
def calculate_min_max_avg(num_list):
    """Functions returning multiple comma-separated values return a tuple."""
    return min(num_list), max(num_list), sum(num_list) / len(num_list)

stats = calculate_min_max_avg([12, 45, 67, 89, 23, 90])
minimum, maximum, average = stats
print(f"Stats returned: {stats}")
print(f"Min: {minimum}, Max: {maximum}, Avg: {average:.2f}")


# --- 7. Tuples as Dictionary Keys (Hashability) ---
print("\n--- 7. Tuples as Hashable Dictionary Keys ---")
# Because tuples are immutable, they are hashable and can serve as dict keys!
# Lists CANNOT be dictionary keys.
locations = {
    (28.6139, 77.2090): "New Delhi",
    (19.0760, 72.8777): "Mumbai",
    (12.9716, 77.5946): "Bengaluru"
}
delhi_coords = (28.6139, 77.2090)
print(f"Location at {delhi_coords}: {locations[delhi_coords]}")
