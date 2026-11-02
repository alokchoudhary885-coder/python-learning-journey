# Python Lists: Creation, Indexing, Slicing, Methods, and Comprehensions
# =======================================================================
# A list is an ordered, mutable collection that allows duplicate elements.


# --- 1. List Creation & Indexing ---
print("--- 1. List Creation & Indexing ---")
fruits = ["Apple", "Banana", "Cherry", "Date", "Elderberry"]

print("Original list :", fruits)
print("Length (len)  :", len(fruits))
print("First element :", fruits[0])
print("Last element  :", fruits[-1])
print("Second to last:", fruits[-2])


# --- 2. Slicing Lists [start:stop:step] ---
print("\n--- 2. List Slicing ---")
print("fruits[1:4]  :", fruits[1:4])       # Elements at index 1, 2, 3
print("fruits[:3]   :", fruits[:3])        # First 3 elements
print("fruits[2:]   :", fruits[2:])        # From index 2 to end
print("fruits[::2]  :", fruits[::2])       # Every second element
print("fruits[::-1] :", fruits[::-1])      # Reversed list via slice


# --- 3. Adding Elements: append(), insert(), extend() ---
print("\n--- 3. Adding Elements ---")
cart = ["Milk", "Bread"]
print("Initial cart:", cart)

# append: Adds single item to the end
cart.append("Eggs")
print("After append('Eggs'):", cart)

# insert: Adds item at specific index
cart.insert(1, "Butter")
print("After insert(1, 'Butter'):", cart)

# extend: Appends all items from another iterable
cart.extend(["Cheese", "Yogurt"])
print("After extend(['Cheese', 'Yogurt']):", cart)


# --- 4. Removing Elements: pop(), remove(), clear() ---
print("\n--- 4. Removing Elements ---")
# pop: Removes and returns element by index (default: last element)
removed_item = cart.pop()
print(f"Popped item: {removed_item} | Remaining cart: {cart}")

removed_first = cart.pop(0)
print(f"Popped index 0 ({removed_first}) | Remaining: {cart}")

# remove: Removes first matching occurrence by value
cart.remove("Eggs")
print("After remove('Eggs'):", cart)


# --- 5. Searching, Counting & Sorting ---
print("\n--- 5. Searching, Counting & Ordering ---")
scores = [45, 92, 78, 92, 88, 64, 92, 53]
print("Scores list:", scores)
print("Count of 92:", scores.count(92))
print("Index of 78:", scores.index(78))
print("Is 88 in scores?", 88 in scores)

# sorted() returns a NEW sorted list, original remains unchanged
sorted_copy = sorted(scores)
print("sorted() new list:", sorted_copy)
print("Original scores  :", scores)

# sort() sorts the list IN-PLACE
scores.sort(reverse=True)
print("After in-place scores.sort(reverse=True):", scores)


# --- 6. List Comprehensions (Pythonic Transformation & Filtering) ---
print("\n--- 6. List Comprehensions ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Squares of all numbers
squares = [n ** 2 for n in numbers]
print("Squares:", squares)

# Even numbers only (Filtering with if)
evens = [n for n in numbers if n % 2 == 0]
print("Evens only:", evens)

# Conditional expression: Label Odd/Even
labels = ["Even" if n % 2 == 0 else "Odd" for n in numbers[:5]]
print("First 5 labels:", labels)
