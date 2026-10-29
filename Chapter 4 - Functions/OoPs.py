# Object-Oriented Programming (OOP) - Employee Class Demo
# ========================================================

class Employee:
    def __init__(self, e_id, e_name, e_address, e_age):
        self.e_id = e_id
        self.e_name = e_name
        self.e_address = e_address
        self.e_age = e_age

    def display_employee_details(self):
        print(f"Employee ID      : {self.e_id}")
        print(f"Employee Name    : {self.e_name}")
        print(f"Employee Address : {self.e_address}")
        print(f"Employee Age     : {self.e_age}")
        print("-" * 30)


if __name__ == "__main__":
    print("--- Employee Details ---")
    emp1 = Employee("123", "Alok", "Bihar", 21)
    emp1.display_employee_details()

    emp2 = Employee("124", "Ankit", "Delhi", 29)
    emp2.display_employee_details()
