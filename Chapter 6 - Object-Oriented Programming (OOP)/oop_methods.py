# Types of Methods in Python OOP
# ===============================
# Python classes support three types of methods:
# 1. Instance Methods (bound to an instance, receives 'self')
# 2. Class Methods (bound to the class, receives 'cls' with @classmethod)
# 3. Static Methods (independent utility functions inside a class with @staticmethod)


class BankAccount:
    # Class (static) variable shared across all bank accounts
    bank_name = "State Bank of Learning"
    interest_rate = 4.5  # in percent
    total_accounts_created = 0

    def __init__(self, account_holder, balance=0.0):
        self.account_holder = account_holder  # Instance variable
        self.balance = balance                # Instance variable
        BankAccount.total_accounts_created += 1

    # --- 1. Instance Method ---
    # Operates on the individual object's data using 'self'
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs. {amount} to {self.account_holder}'s account. New Balance: Rs. {self.balance}")
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew Rs. {amount}. Remaining Balance: Rs. {self.balance}")
        else:
            print(f"Insufficient funds or invalid amount for {self.account_holder}!")

    def get_statement(self):
        return f"Account: {self.account_holder} | Balance: Rs. {self.balance:,.2f} | Bank: {self.bank_name}"

    # --- 2. Class Method ---
    # Operates on class state using 'cls', decorated with @classmethod
    @classmethod
    def set_interest_rate(cls, new_rate):
        cls.interest_rate = new_rate
        print(f"[{cls.bank_name}] Global interest rate updated to: {cls.interest_rate}%")

    @classmethod
    def from_string(cls, account_info_str):
        # Alternative constructor / Factory pattern
        holder, balance_str = account_info_str.split("-")
        return cls(holder.strip(), float(balance_str.strip()))

    @classmethod
    def get_total_accounts(cls):
        return f"Total active accounts in {cls.bank_name}: {cls.total_accounts_created}"

    # --- 3. Static Method ---
    # Does not take self or cls. A pure utility function inside class scope.
    @staticmethod
    def is_valid_pan(pan_number):
        # Checks if PAN is a 10-character alphanumeric string
        return len(pan_number) == 10 and pan_number.isalnum()

    @staticmethod
    def calculate_simple_interest(principal, rate, time_years):
        return (principal * rate * time_years) / 100.0


if __name__ == "__main__":
    print("--- 1. Testing Instance Methods ---")
    acc1 = BankAccount("Alok", 5000.0)
    acc1.deposit(2500.0)
    acc1.withdraw(1200.0)
    print(acc1.get_statement())

    print("\n--- 2. Testing Class Methods ---")
    # Factory constructor using class method
    acc2 = BankAccount.from_string("Ayush - 12000.0")
    print(acc2.get_statement())

    # Modifying class variable via class method
    BankAccount.set_interest_rate(5.2)
    print("Current interest rate from acc1:", acc1.interest_rate)
    print("Current interest rate from acc2:", acc2.interest_rate)
    print(BankAccount.get_total_accounts())

    print("\n--- 3. Testing Static Methods ---")
    pan1 = "ABCDE1234F"
    pan2 = "INVALID_PAN_123"
    print(f"Is '{pan1}' valid PAN? ->", BankAccount.is_valid_pan(pan1))
    print(f"Is '{pan2}' valid PAN? ->", BankAccount.is_valid_pan(pan2))

    interest = BankAccount.calculate_simple_interest(10000, BankAccount.interest_rate, 2)
    print(f"Calculated 2-year Simple Interest on Rs. 10,000: Rs. {interest:.2f}")
