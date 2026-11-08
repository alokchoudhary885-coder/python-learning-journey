# Exception Handling in Python: try, except, else, finally, raise & Custom Exceptions
# ====================================================================================


# --- 1. Basic try-except (ZeroDivisionError) ---
print("--- 1. Basic Exception Handling ---")
try:
    numerator = 100
    denominator = 0
    result = numerator / denominator
except ZeroDivisionError as err:
    print(f"Error caught gracefully: Cannot divide by zero! ({err})")


# --- 2. Catching Multiple Specific Exceptions ---
print("\n--- 2. Handling Multiple Exception Types ---")
def parse_and_fetch(data_list, index_str):
    try:
        idx = int(index_str)             # May raise ValueError
        value = data_list[idx]           # May raise IndexError
        print(f"Fetched value at index {idx}: {value}")
    except ValueError:
        print(f"Invalid input: '{index_str}' is not an integer!")
    except IndexError:
        print(f"Index out of range: {index_str} is beyond list length ({len(data_list)})")

sample_data = ["Python", "JavaScript", "Rust"]
parse_and_fetch(sample_data, "1")
parse_and_fetch(sample_data, "abc")
parse_and_fetch(sample_data, "10")


# --- 3. The Complete Flow: try - except - else - finally ---
print("\n--- 3. Full try - except - else - finally Flow ---")
def calculate_discount(price_str, discount_pct):
    print(f"\nProcessing price '{price_str}' with {discount_pct}% discount...")
    try:
        price = float(price_str)
        discounted = price - (price * discount_pct / 100)
    except ValueError:
        print("[EXCEPT] Failed to convert price to float!")
    else:
        # 'else' executes ONLY IF NO exception was raised in 'try'
        print(f"[ELSE] Calculation succeeded: Final price = Rs. {discounted:.2f}")
    finally:
        # 'finally' is GUARANTEED to execute no matter what (even on error or return)
        print("[FINALLY] Cleanup complete. Transaction logged.")

calculate_discount("500", 10)
calculate_discount("invalid_price", 10)


# --- 4. The 'raise' Keyword (Enforcing Business Rules) ---
print("\n--- 4. Raising Built-in Exceptions ---")
def register_voter(name, age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age < 18:
        raise PermissionError(f"{name} ({age} yrs) is not eligible to vote yet.")
    return f"Voter '{name}' registered successfully!"

try:
    print(register_voter("Alok", 21))
    print(register_voter("Rohan", 15))
except PermissionError as err:
    print("Caught PermissionError:", err)


# --- 5. Custom User-Defined Exceptions ---
print("\n--- 5. Custom User-Defined Exception ---")
# Best practice: Inherit from built-in 'Exception'
class InsufficientFundsError(Exception):
    """Raised when withdrawal amount exceeds available bank balance."""
    def __init__(self, balance, amount):
        self.balance = balance
        self.amount = amount
        super().__init__(f"Attempted to withdraw Rs. {amount}, but balance is only Rs. {balance}!")


class BankAccount:
    def __init__(self, holder, initial_balance):
        self.holder = holder
        self.balance = initial_balance

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError(self.balance, amount)
        self.balance -= amount
        print(f"Withdrew Rs. {amount}. Remaining Balance: Rs. {self.balance}")


account = BankAccount("Alok", 5000.0)
account.withdraw(2000.0)

try:
    account.withdraw(8000.0)
except InsufficientFundsError as err:
    print("Caught Custom Exception:", err)
