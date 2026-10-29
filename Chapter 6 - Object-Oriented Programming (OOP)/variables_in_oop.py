# Variables in Python OOP: Instance vs Class (Static) Variables
# =============================================================
# In Python, variables in a class belong to two namespaces:
# 1. Instance Variables (unique per object)
# 2. Class / Static Variables (shared across all objects)


class Student:
    # --- Class Variable (Shared across all students) ---
    college_name = "National Engineering College"
    total_students = 0

    def __init__(self, roll_no, name, branch):
        # --- Instance Variables (Specific to this instance) ---
        self.roll_no = roll_no
        self.name = name
        self.branch = branch

        # Increment shared class counter
        Student.total_students += 1

    def display(self):
        print(f"[{self.roll_no}] {self.name} - Branch: {self.branch} | College: {self.college_name}")


if __name__ == "__main__":
    print("--- 1. Creating Instances with Unique Instance Variables ---")
    s1 = Student(101, "Alok", "Computer Science")
    s2 = Student(102, "Ayush", "Information Technology")

    s1.display()
    s2.display()
    print("Total Students enrolled:", Student.total_students)

    print("\n--- 2. Inspecting Object and Class Namespaces (__dict__) ---")
    # Instance __dict__ only contains its own instance variables
    print("s1.__dict__:", s1.__dict__)
    print("s2.__dict__:", s2.__dict__)
    # Class __dict__ contains college_name and methods
    print("Has 'college_name' in s1.__dict__?", "college_name" in s1.__dict__)
    print("Has 'college_name' in Student.__dict__?", "college_name" in Student.__dict__)

    print("\n--- 3. Modifying Class Variable via Class Name ---")
    # Changing via Student affects all instances reading it
    Student.college_name = "Indian Institute of Technology"
    print("After updating via Student class:")
    print("s1 sees college as:", s1.college_name)
    print("s2 sees college as:", s2.college_name)

    print("\n--- 4. Attribute Shadowing Trap (Common Beginner Mistake) ---")
    # If we assign via an instance: s1.college_name = "..."
    # Python does NOT change the class variable! It creates an instance variable in s1!
    s1.college_name = "Harvard University (Exchange Program)"

    print("s1 college_name (shadowed instance attribute):", s1.college_name)
    print("s2 college_name (still points to class variable):", s2.college_name)
    print("Student.college_name (original class variable)   :", Student.college_name)
    print("Now in s1.__dict__:", s1.__dict__)
