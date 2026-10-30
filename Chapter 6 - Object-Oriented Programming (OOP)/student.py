# Simple Student Practice: Setting, Accessing, and Deleting Instance Variables
# ===========================================================================

class Student:
    def set_data(self, name):
        self.name = name

    def show(self):
        if hasattr(self, "name"):
            print("Student Name:", self.name)
        else:
            print("Variable 'name' does not exist (it has been deleted).")

    def delete(self):
        if hasattr(self, "name"):
            del self.name
            print("Variable 'name' deleted successfully.")


if __name__ == "__main__":
    s1 = Student()

    print("--- 1. Set Variable ---")
    s1.set_data("Alok")

    print("\n--- 2. Access Variable ---")
    s1.show()

    print("\n--- 3. Delete Variable ---")
    s1.delete()

    print("\n--- 4. Verify Variable After Deletion ---")
    s1.show()
