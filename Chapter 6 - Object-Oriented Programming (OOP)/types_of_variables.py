# Types of Variables in Python OOP & When to Use a Single Shared Value
# =====================================================================
# In Python OOP, variables are divided into 3 types:
# 1. Static / Class Variables (Single shared value across all objects)
# 2. Instance Variables (Unique value per object)
# 3. Local Variables (Temporary variable inside a method)


class Employee:
    # =========================================================
    # 1. STATIC / CLASS VARIABLE (Single Shared Value)
    # =========================================================
    # When to use: When ALL objects share the EXACT SAME value.
    # Why: Saves memory (1 copy in RAM instead of thousands).
    company_name = "Tech Solutions Ltd"
    pf_percentage = 12.0  # Shared across all employees

    def __init__(self, emp_id, name, basic_salary):
        # =====================================================
        # 2. INSTANCE VARIABLES (Unique to each object)
        # =====================================================
        # When to use: When each object must maintain its OWN state.
        self.emp_id = emp_id
        self.name = name
        self.basic_salary = basic_salary

    def calculate_salary_slip(self):
        # =====================================================
        # 3. LOCAL VARIABLES (Temporary calculation variables)
        # =====================================================
        # When to use: Temporary computation needed only inside method.
        # Destroyed automatically as soon as this method finishes!
        hra = self.basic_salary * 0.20        # 20% HRA
        pf_deduction = self.basic_salary * (Employee.pf_percentage / 100)
        net_salary = self.basic_salary + hra - pf_deduction

        return {
            "Employee": self.name,
            "Company": Employee.company_name,
            "Basic": self.basic_salary,
            "HRA (Local)": hra,
            "PF (Local)": pf_deduction,
            "Net In-Hand": net_salary
        }


if __name__ == "__main__":
    print("--- 1. Creating Objects with Instance Variables ---")
    e1 = Employee(101, "Alok", 50000.0)
    e2 = Employee(102, "Ayush", 70000.0)

    print(f"e1: ID={e1.emp_id}, Name={e1.name}, Basic={e1.basic_salary}")
    print(f"e2: ID={e2.emp_id}, Name={e2.name}, Basic={e2.basic_salary}")

    print("\n--- 2. When to Use a Single Shared Value (Static Variable) ---")
    # Both employees share the exact same company name and PF rate
    print(f"e1 Company: {e1.company_name} | e2 Company: {e2.company_name}")
    print("Do they point to the exact same string in memory?", e1.company_name is e2.company_name)

    # Benefit: If PF rate changes, changing ONE variable updates ALL employees!
    print("\n[Admin Action] Updating PF percentage from 12% to 10% via class...")
    Employee.pf_percentage = 10.0
    print(f"e1 now sees PF rate as: {e1.pf_percentage}%")
    print(f"e2 now sees PF rate as: {e2.pf_percentage}%")

    print("\n--- 3. Local Variables in Action (Method Execution) ---")
    slip1 = e1.calculate_salary_slip()
    for key, val in slip1.items():
        print(f"  {key:15}: {val}")

    print("\n--- 4. Local Variable Scope Verification ---")
    # Local variable 'hra' or 'net_salary' does NOT exist on the object or globally
    print("Does e1 have 'hra' attribute?", hasattr(e1, "hra"))
    print("Does e1 have 'net_salary' attribute?", hasattr(e1, "net_salary"))
    print("Local variables exist only during the method call and vanish afterwards!")
