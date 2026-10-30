# Instance Variables in Python OOP: Declaration, Access, and Deletion
# ====================================================================
# Instance variables are variables whose values are specific to each object instance.


class Student:
    def __init__(self, roll_no, name):
        # 1. Declared INSIDE Constructor using 'self'
        self.roll_no = roll_no
        self.name = name

    def add_course(self, course_name):
        # 2. Declared INSIDE Instance Method using 'self'
        self.course = course_name

    def display(self):
        # 1. Accessed INSIDE Class using 'self'
        print(f"Roll: {self.roll_no} | Name: {self.name}", end="")
        if hasattr(self, "course"):
            print(f" | Course: {self.course}", end="")
        if hasattr(self, "city"):
            print(f" | City: {self.city}", end="")
        print()

    def remove_course(self):
        # 1. Deleted INSIDE Class using 'del self.var'
        if hasattr(self, "course"):
            del self.course
            print(f"Course deleted from inside class for {self.name}.")


if __name__ == "__main__":
    # --- 1. DECLARATION OF INSTANCE VARIABLES ---
    print("--- 1. Declaring Instance Variables ---")
    s1 = Student(101, "Alok")
    s2 = Student(102, "Ayush")

    # Declared inside instance method
    s1.add_course("Python Full Stack")

    # 3. Declared OUTSIDE Class using object reference
    s1.city = "Jaipur"
    s2.city = "Delhi"

    print("s1 attributes:", s1.__dict__)
    print("s2 attributes:", s2.__dict__)

    # --- 2. ACCESSING INSTANCE VARIABLES ---
    print("\n--- 2. Accessing Instance Variables ---")
    # Accessed inside class via method
    s1.display()
    s2.display()

    # 2. Accessed OUTSIDE Class using object reference
    print("Outside access -> s1 name:", s1.name)
    print("Outside access -> s1 city:", s1.city)

    # --- 3. DELETING INSTANCE VARIABLES ---
    print("\n--- 3. Deleting Instance Variables ---")
    # Case A: Delete from inside class using 'del self.var'
    s1.remove_course()
    print("s1 attributes after removing course:", s1.__dict__)

    # Case B: Delete from outside class using 'del object.var'
    print("Deleting 'city' from outside class for s1...")
    del s1.city
    print("s1 attributes after deleting city:", s1.__dict__)

    # --- 4. ACCESS AFTER DELETION (Error Handling) ---
    print("\n--- 4. Accessing Attribute After Deletion ---")
    try:
        print("Trying to access s1.city:", s1.city)
    except AttributeError as err:
        print("AttributeError caught successfully:", err)

    # Note: Deleting from s1 does NOT affect s2
    print("s2 city is still intact:", s2.city)
