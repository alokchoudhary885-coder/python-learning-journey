# Chapter 6: Encapsulation in Python
# Demonstrates data hiding, public, protected (_), private (__) attributes, and property getters/setters.

class BankAccount:
    def __init__(self, account_holder, initial_balance, pin):
        self.holder = account_holder         # Public attribute
        self._account_type = "Savings"       # Protected attribute (convention)
        self.__balance = initial_balance     # Private attribute (name mangling)
        self.__pin = pin                     # Private attribute

    # Getter property for balance (read-only access)
    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        print(f"Deposited Rs. {amount:,.2f}. New Balance: Rs. {self.__balance:,.2f}")

    def withdraw(self, amount, entered_pin):
        if entered_pin != self.__pin:
            print("Transaction Failed: Invalid PIN.")
            return False
        if amount > self.__balance:
            print("Transaction Failed: Insufficient funds.")
            return False

        self.__balance -= amount
        print(f"Withdrawn Rs. {amount:,.2f}. Remaining Balance: Rs. {self.__balance:,.2f}")
        return True

    # Property for changing PIN with verification
    def change_pin(self, old_pin, new_pin):
        if old_pin != self.__pin:
            print("PIN change failed: Incorrect old PIN.")
            return False
        if len(str(new_pin)) != 4:
            print("PIN change failed: New PIN must be 4 digits.")
            return False
        self.__pin = new_pin
        print("PIN successfully updated.")
        return True


if __name__ == "__main__":
    account = BankAccount("Alok Choudhary", 5000.0, 1234)

    print("--- 1. Public Access ---")
    print("Account Holder:", account.holder)
    print("Current Balance (via getter property): Rs.", account.balance)

    print("\n--- 2. Valid Transaction ---")
    account.deposit(2000.0)
    account.withdraw(1500.0, entered_pin=1234)

    print("\n--- 3. Invalid PIN Attempt ---")
    account.withdraw(500.0, entered_pin=9999)

    print("\n--- 4. Data Hiding & Name Mangling ---")
    # Directly accessing private attribute raises AttributeError
    try:
        print(account.__balance)
    except AttributeError as e:
        print("Direct access blocked:", e)

    # Python mangles private names to _ClassName__attr
    print("Access via mangled name:", account._BankAccount__balance)
