# Master Guide: Static, Instance, and Local Variables in Python OOP
# ===================================================================

class Demo:
    # -------------------------------------------------------------
    # 1. PLACES TO DECLARE STATIC / CLASS VARIABLES
    # -------------------------------------------------------------
    # Place 1: Directly inside the class body
    static_1 = "Declared in class body"

    def __init__(self, name):
        # Instance Variable (unique per instance)
        self.name = name

        # Place 2: Inside constructor using ClassName
        Demo.static_2 = "Declared inside constructor"

    def instance_method(self):
        # Place 3: Inside instance method using ClassName
        Demo.static_3 = "Declared inside instance method"

        # Local Variable (lives only while instance_method executes)
        local_calc = 100 * 5
        print(f"Inside instance_method -> local_calc: {local_calc}")

    @classmethod
    def class_method(cls):
        # Place 4: Inside class method using 'cls' or ClassName
        cls.static_4 = "Declared inside class method"

    @staticmethod
    def static_method():
        # Place 5: Inside static method using ClassName
        Demo.static_5 = "Declared inside static method"

        # Local variable inside static method
        temp_flag = True
        print(f"Inside static_method -> temp_flag: {temp_flag}")


if __name__ == "__main__":
    print("--- 1. Testing Declaration Locations ---")
    d1 = Demo("Object-1")
    d2 = Demo("Object-2")

    # Place 6: Outside the class using ClassName
    Demo.static_6 = "Declared outside class"

    d1.instance_method()
    Demo.class_method()
    Demo.static_method()

    print("\nAll 6 Static Variables Created Successfully:")
    print(" 1.", Demo.static_1)
    print(" 2.", Demo.static_2)
    print(" 3.", Demo.static_3)
    print(" 4.", Demo.static_4)
    print(" 5.", Demo.static_5)
    print(" 6.", Demo.static_6)

    # -------------------------------------------------------------
    # 2. ACCESSING STATIC VARIABLES (ClassName vs Object Reference)
    # -------------------------------------------------------------
    print("\n--- 2. Accessing Static Variables ---")
    # Recommended: via ClassName
    print("Via ClassName : Demo.static_1 ->", Demo.static_1)
    # Also works: via object reference
    print("Via Object d1 : d1.static_1   ->", d1.static_1)
    print("Via Object d2 : d2.static_1   ->", d2.static_1)

    # -------------------------------------------------------------
    # 3. MODIFYING STATIC VARIABLES VS ATTRIBUTE SHADOWING
    # -------------------------------------------------------------
    print("\n--- 3. Modifying vs Shadowing Static Variables ---")
    # Rule: Always modify static variables using ClassName!
    Demo.static_1 = "Updated globally via ClassName"
    print("After Demo.static_1 update:")
    print("  d1 sees:", d1.static_1)
    print("  d2 sees:", d2.static_1)

    # Shadowing Trap: Modifying via object reference
    print("\nAttempting update via object: d1.static_1 = 'Shadowed in d1 only'")
    d1.static_1 = "Shadowed in d1 only"

    print("  d1 sees (its own new instance variable):", d1.static_1)
    print("  d2 sees (original static variable)     :", d2.static_1)
    print("  Demo.static_1 (actual class variable)  :", Demo.static_1)

    # Proof via __dict__
    print("\nd1.__dict__ (contains shadow):", d1.__dict__)
    print("d2.__dict__ (clean):", d2.__dict__)

    # -------------------------------------------------------------
    # 4. LOCAL VARIABLES (STACK LIFECYCLE)
    # -------------------------------------------------------------
    print("\n--- 4. Local Variables Isolation ---")
    def calculate_bonus(basic_salary):
        bonus_rate = 0.15          # Local variable
        bonus = basic_salary * bonus_rate  # Local variable
        return bonus

    earned_bonus = calculate_bonus(40000)
    print("Calculated bonus:", earned_bonus)
    try:
        print(bonus_rate)  # Cannot access local variable outside!
    except NameError as e:
        print("Expected NameError outside function:", e)
