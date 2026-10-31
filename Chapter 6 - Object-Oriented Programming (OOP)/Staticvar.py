# Static, Instance, and Local Variables in Python OOP
# ====================================================

# --- Part 1: Static Variable vs Instance Variable ---
class Test1:
    a = 10  # Static / Class Variable (Shared across all objects)

    def __init__(self):
        self.b = 20  # Instance Variable (Unique to each object)


print("--- 1. Static vs Instance Variable ---")
t1 = Test1()
t2 = Test1()

print("Initial values:")
print("t1 -> a:", t1.a, "| b:", t1.b)
print("t2 -> a:", t2.a, "| b:", t2.b)

# Modifying static variable via Class name
Test1.a = 99
print("\nAfter modifying Test1.a = 99:")
print("t1 -> a:", t1.a, "| b:", t1.b)
print("t2 -> a:", t2.a, "| b:", t2.b)
print("Notice: Modifying static variable updates 'a' for BOTH t1 and t2!")

# Modifying instance variable of t1
t1.b = 555
print("\nAfter modifying t1.b = 555:")
print("t1 -> a:", t1.a, "| b:", t1.b)
print("t2 -> a:", t2.a, "| b:", t2.b)
print("Notice: Modifying t1.b changes ONLY t1, not t2!")


# --- Part 2: Local Variables Inside Methods ---
class Test2:
    def m1(self):
        a = 10  # Local variable to method m1
        print("Inside m1() -> local a:", a)

    def m2(self):
        b = 20  # Local variable to method m2
        print("Inside m2() -> local b:", b)
        # Attempting to access 'a' from m1 will raise NameError
        try:
            print("Trying to access 'a' inside m2:", a)
        except NameError as err:
            print("Caught Expected NameError in m2():", err)


print("\n--- 2. Local Variable Scope Demonstration ---")
t = Test2()
t.m1()
t.m2()
