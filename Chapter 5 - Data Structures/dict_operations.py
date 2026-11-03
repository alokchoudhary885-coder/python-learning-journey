# Python Dictionaries: Creation, Access, Methods, Comprehensions, and Nested Data
# ==============================================================================
# A dictionary is an ordered (Python 3.7+), mutable collection of key-value pairs.


# --- 1. Dictionary Creation & Hashable Keys ---
print("--- 1. Dictionary Creation ---")
student = {
    "roll_no": 101,
    "name": "Alok",
    "course": "Python Full Stack",
    "score": 92.5,
    "is_enrolled": True
}
print("Student Dictionary:", student)
print("Total keys in dict :", len(student))


# --- 2. Safe Access: dict[key] vs dict.get() ---
print("\n--- 2. Safe Value Access ---")
print("Accessing 'name' via key   :", student["name"])
print("Accessing 'name' via get() :", student.get("name"))

# Missing key comparison:
# student["city"] would crash with KeyError!
# student.get("city", default) returns fallback safely
print("student.get('city')               :", student.get("city"))
print("student.get('city', 'Not Provided'):", student.get("city", "Not Provided"))


# --- 3. Adding and Updating Entries ---
print("\n--- 3. Adding & Updating Elements ---")
# Adding new key-value pair
student["city"] = "Jaipur"
print("After adding 'city':", student)

# Updating existing key
student["score"] = 95.0

# Batch update with update()
student.update({"batch": 167, "grade": "A+"})
print("After batch update:", student)


# --- 4. Removing Items: pop(), popitem(), del ---
print("\n--- 4. Removing Items ---")
# pop(key): Removes specific key and returns its value
popped_batch = student.pop("batch")
print(f"Popped 'batch': {popped_batch}")

# popitem(): Removes and returns the last inserted (key, value) pair
last_item = student.popitem()
print(f"Popped last item (key, val): {last_item}")

# del keyword
del student["is_enrolled"]
print("After del 'is_enrolled':", student)


# --- 5. Iterating Through Dictionaries ---
print("\n--- 5. Iterating Dictionaries ---")
print("Keys only:")
for k in student.keys():
    print(k, end=" ")
print()

print("\nValues only:")
for v in student.values():
    print(v, end=" | ")
print()

print("\nKey-Value pairs (items):")
for key, value in student.items():
    print(f"  {key:10}: {value}")


# --- 6. Dictionary Comprehensions ---
print("\n--- 6. Dictionary Comprehensions ---")
numbers = [1, 2, 3, 4, 5]
# Mapping number -> square
square_map = {n: n ** 2 for n in numbers}
print("Number Squares Map:", square_map)

# Filter with condition
prices_in_usd = {"Laptop": 800, "Mouse": 25, "Monitor": 250, "Cable": 10}
premium_gadgets = {item: price for item, price in prices_in_usd.items() if price >= 100}
print("Premium Gadgets (>= $100):", premium_gadgets)


# --- 7. Nested Dictionaries (Real-World Record) ---
print("\n--- 7. Nested Dictionary (Student Gradebook) ---")
gradebook = {
    "student_1": {"name": "Alok", "marks": {"math": 88, "python": 94}},
    "student_2": {"name": "Ayush", "marks": {"math": 76, "python": 85}}
}

for s_id, data in gradebook.items():
    python_score = data["marks"]["python"]
    print(f"[{s_id}] {data['name']} scored {python_score} in Python.")
