# Python Sets: Creation, Methods, Mathematical Operations, and Frozenset
# ======================================================================
# A set is an unordered, unindexed, and mutable collection of UNIQUE elements.


# --- 1. Set Creation & The Empty Set Trap ---
print("--- 1. Set Creation & Duplicate Elimination ---")
numbers = {1, 2, 3, 4, 2, 3, 1, 5}
print("Original set (duplicates automatically removed):", numbers)

# Crucial Beginner Trap: {} creates an empty dict, NOT an empty set!
empty_dict = {}
empty_set = set()
print(f"{{}}        -> Type: {type(empty_dict)} (Dictionary!)")
print(f"set()     -> Type: {type(empty_set)} (Set!)")


# --- 2. Adding & Removing Elements ---
print("\n--- 2. Adding and Removing Elements ---")
languages = {"Python", "Java", "C++"}
print("Initial set:", languages)

# add(): Adds a single element
languages.add("Go")
print("After add('Go'):", languages)

# update(): Adds multiple elements from an iterable
languages.update(["Rust", "JavaScript"])
print("After update(['Rust', 'JavaScript']):", languages)

# remove() vs discard():
# discard() is safe (does not raise KeyError if item missing)
languages.discard("Ruby")  # No error
# remove() would raise KeyError if item does not exist
languages.remove("Java")
print("After discard('Ruby') and remove('Java'):", languages)

# pop(): Removes and returns an arbitrary element
popped_lang = languages.pop()
print(f"Popped item: {popped_lang} | Remaining: {languages}")


# --- 3. Mathematical Set Operations (Operators & Methods) ---
print("\n--- 3. Mathematical Set Operations ---")
frontend = {"HTML", "CSS", "JavaScript", "React"}
backend = {"Python", "JavaScript", "Django", "Node"}

print("Frontend Skills:", frontend)
print("Backend Skills :", backend)

# A. Union (All skills combined without duplicates) -> | or union()
all_skills = frontend | backend
print("Union (|)                 :", all_skills)

# B. Intersection (Common skills) -> & or intersection()
fullstack_bridge = frontend & backend
print("Intersection (&)          :", fullstack_bridge)

# C. Difference (In frontend but NOT in backend) -> - or difference()
only_frontend = frontend - backend
print("Difference (frontend - backend):", only_frontend)

# D. Symmetric Difference (In either, but NOT in both) -> ^ or symmetric_difference()
non_overlapping = frontend ^ backend
print("Symmetric Difference (^)  :", non_overlapping)


# --- 4. Membership Testing ($O(1)$ Hash Lookup) ---
print("\n--- 4. Fast Membership Testing ---")
active_user_ids = {1001, 1002, 1003, 1004, 1005}
check_id = 1003
# Sets check membership in O(1) average time, unlike lists O(n)
print(f"Is user ID {check_id} active?", check_id in active_user_ids)


# --- 5. Set Comprehensions ---
print("\n--- 5. Set Comprehension ---")
raw_scores = [12, 45, 12, 78, 90, 45, 23]
# Unique squares of scores > 20
unique_squares = {x ** 2 for x in raw_scores if x > 20}
print("Unique squares:", unique_squares)


# --- 6. Frozenset (Immutable Set) ---
print("\n--- 6. Frozenset (Immutable Set) ---")
# frozenset cannot be modified after creation, making it hashable!
immutable_set = frozenset(["Admin", "Editor", "Viewer"])
print("Frozenset:", immutable_set)

try:
    immutable_set.add("Superuser")
except AttributeError as err:
    print("Caught Expected AttributeError:", err)

# Frozenset can be used as a dictionary key or inside another set!
role_permissions = {
    immutable_set: "All standard corporate roles"
}
print("Dictionary with frozenset key:", role_permissions)
