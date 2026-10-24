# Chapter 6: Classes and Objects in Python
# Demonstrates class definition, __init__ constructor, self, instance vs class variables, and methods.

class Student:
    # Class variable (shared across all instances)
    college_name = "Global Engineering Institute"
    student_count = 0

    def __init__(self, name, roll_no, branch):
        # Instance variables (unique to each object)
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.marks = []
        Student.student_count += 1

    def add_marks(self, *scores):
        """Instance method to record scores."""
        self.marks.extend(scores)

    def calculate_average(self):
        """Instance method to calculate average score."""
        if not self.marks:
            return 0.0
        return sum(self.marks) / len(self.marks)

    def display_details(self):
        """Displays formatted student profile."""
        avg = self.calculate_average()
        print(f"Roll No : {self.roll_no}")
        print(f"Name    : {self.name}")
        print(f"Branch  : {self.branch}")
        print(f"Average : {avg:.2f}")
        print(f"College : {Student.college_name}")

    @classmethod
    def get_total_students(cls):
        """Class method to inspect class state."""
        return cls.student_count

    @staticmethod
    def is_passing_grade(score):
        """Static utility method that does not access instance or class state."""
        return score >= 40


if __name__ == "__main__":
    print("--- 1. Creating Objects (Instances) ---")
    student1 = Student("Alok Choudhary", 101, "CSE")
    student2 = Student("Priya Sharma", 102, "IT")

    student1.add_marks(85, 90, 78)
    student2.add_marks(92, 88, 95)

    print("\n--- Student 1 Details ---")
    student1.display_details()

    print("\n--- Student 2 Details ---")
    student2.display_details()

    print("\n--- 2. Class Methods and Variables ---")
    print("Total registered students:", Student.get_total_students())

    print("\n--- 3. Static Method Call ---")
    print("Is 38 passing?:", Student.is_passing_grade(38))
    print("Is 75 passing?:", Student.is_passing_grade(75))
