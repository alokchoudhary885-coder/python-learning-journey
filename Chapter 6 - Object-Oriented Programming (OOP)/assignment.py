# Chapter 6 - Assignment: OOP Variables, Methods, and Lifecycle
# =============================================================
# Task 1: Declare instance variables in all 3 possible locations (init, method, outside).
# Task 2: Implement sensitive data deletion (inside via 'del self.var' and outside via 'del obj.var').
# Task 3: Demonstrate when to use a single shared value (Static/Class variable) and synchronous updates.
# Task 4: Use temporary local variables inside a method without polluting the instance dictionary.
# Task 5: Build an Employee Directory system combining all variable types and lifecycle operations.


# --- Task 1: Instance Variables in 3 Locations ---
class StudentProfile:
    def __init__(self, roll_no, name):
        # Place 1: Inside constructor
        self.roll_no = roll_no
        self.name = name

    def register_email(self, email):
        # Place 2: Inside instance method
        self.email = email


# --- Task 2: Deleting Instance Variables (Clean Data Cleanup) ---
class UserAuth:
    def __init__(self, username, auth_token):
        self.username = username
        self.auth_token = auth_token

    def logout(self):
        """Clears sensitive session token from inside class."""
        if hasattr(self, "auth_token"):
            del self.auth_token
            return f"User '{self.username}' logged out. Token destroyed."
        return "No active session."


# --- Task 3: Single Shared Value (Static / Class Variable) ---
class BankAccount:
    # Single shared values (Class/Static Variables)
    bank_name = "Reserve Bank of Python"
    branch_ifsc = "RBP000101"
    interest_rate = 4.0  # in percent

    def __init__(self, account_holder, balance):
        # Instance variables (unique per account)
        self.account_holder = account_holder
        self.balance = balance


# --- Task 4: Local Variables for Intermediate Computations ---
class LoanCalculator:
    def calculate_emi(self, principal, tenure_months):
        # Local variables: temporary calculation only, vanish when method returns!
        annual_rate = 0.10
        monthly_rate = annual_rate / 12
        emi = (principal * monthly_rate * ((1 + monthly_rate) ** tenure_months)) / (
            ((1 + monthly_rate) ** tenure_months) - 1
        )
        return round(emi, 2)


# --- Task 5: Employee Directory (Full Integration) ---
class EmployeeRecord:
    company = "Infosys Learning"
    total_active_staff = 0

    def __init__(self, emp_id, full_name, role):
        self.emp_id = emp_id
        self.full_name = full_name
        self.role = role
        EmployeeRecord.total_active_staff += 1

    def assign_mentor(self, mentor_name):
        self.mentor = mentor_name

    def remove_temporary_access(self):
        if hasattr(self, "temp_badge"):
            del self.temp_badge


if __name__ == "__main__":
    print("--- Task 1: Declaring Instance Variables in 3 Locations ---")
    student = StudentProfile(101, "Alok")
    student.register_email("alok@example.com")
    # Place 3: Outside class
    student.phone = "+91-9876543210"
    print("All instance variables declared:")
    for k, v in student.__dict__.items():
        print(f"  {k:10}: {v}")

    print("\n--- Task 2: Deleting Instance Variables ---")
    user = UserAuth("alok_coder", "TOKEN_SECRET_9876")
    user.debug_log = "Verbose debugging ON"  # Dynamically added
    print("Before logout token present:", hasattr(user, "auth_token"))

    # Deleting inside class
    print(user.logout())
    print("After logout token present :", hasattr(user, "auth_token"))

    # Deleting outside class
    print("Deleting 'debug_log' from outside...")
    del user.debug_log
    print("User attributes now:", user.__dict__)

    print("\n--- Task 3: Single Shared Value (Static Variable) ---")
    acc1 = BankAccount("Alok", 15000.0)
    acc2 = BankAccount("Ayush", 25000.0)

    print(f"acc1 Bank: {acc1.bank_name} | acc2 Bank: {acc2.bank_name}")
    print("Initial Interest Rate:", BankAccount.interest_rate, "%")

    # Updating single shared value updates for both accounts synchronously
    BankAccount.interest_rate = 5.25
    print("After updating via BankAccount class:")
    print("acc1 sees interest rate as:", acc1.interest_rate, "%")
    print("acc2 sees interest rate as:", acc2.interest_rate, "%")

    print("\n--- Task 4: Local Variables Isolation ---")
    loan = LoanCalculator()
    monthly_emi = loan.calculate_emi(500000, 36)
    print("Calculated EMI on Rs. 5,00,000 for 36 months: Rs.", monthly_emi)
    print("Are local calculation variables stored in loan.__dict__?", loan.__dict__)

    print("\n--- Task 5: Employee Directory Integration ---")
    emp = EmployeeRecord(1001, "Alok Choudhary", "Software Engineer")
    emp.assign_mentor("Senior Architect")
    emp.temp_badge = "TEMP-VISITOR-PASS"

    print("Employee initialized with badge:", emp.temp_badge)
    emp.remove_temporary_access()
    print("After removing badge, has temp_badge?:", hasattr(emp, "temp_badge"))
    print("Total active staff in company:", EmployeeRecord.total_active_staff)
