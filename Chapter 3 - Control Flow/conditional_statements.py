# Conditional Statements in Python
# =================================
# Decision making statements control the flow of program execution based on conditions.


# --- 1. Basic if-elif-else ---
score = 85

print("--- 1. Basic if-elif-else (Grade System) ---")
if score >= 90:
    grade = "A+"
elif score >= 80:
    grade = "A"
elif score >= 70:
    grade = "B"
elif score >= 60:
    grade = "C"
else:
    grade = "Fail"

print(f"Score: {score} -> Grade: {grade}")


# --- 2. Multiple Conditions with Logical Operators (and, or, not) ---
print("\n--- 2. Logical Operators in Decisions ---")
age = 22
has_license = True
has_dui_record = False

if age >= 18 and has_license and not has_dui_record:
    print("Eligible to rent a car: YES")
else:
    print("Eligible to rent a car: NO")


# --- 3. Nested if-else ---
print("\n--- 3. Nested if-else (ATM Withdrawal Simulation) ---")
account_balance = 10000.0
withdrawal_amount = 3500.0
is_pin_valid = True

if is_pin_valid:
    if withdrawal_amount <= account_balance:
        if withdrawal_amount % 100 == 0:
            account_balance -= withdrawal_amount
            print(f"Dispensing Rs. {withdrawal_amount}. Remaining: Rs. {account_balance}")
        else:
            print("Amount must be a multiple of 100!")
    else:
        print("Insufficient balance!")
else:
    print("Invalid PIN entered.")


# --- 4. Python 3.10+ Structural Pattern Matching (match-case) ---
print("\n--- 4. match-case Statement (Alternative to switch-case) ---")
status_code = 404

match status_code:
    case 200:
        message = "200 OK: Request succeeded"
    case 301:
        message = "301 Moved Permanently: Resource redirected"
    case 400:
        message = "400 Bad Request: Invalid input format"
    case 404:
        message = "404 Not Found: Page or item does not exist"
    case 500:
        message = "500 Internal Server Error: Server crashed"
    case _:
        message = f"Unknown status code ({status_code})"

print("Server Response:", message)


# --- 5. Short-Circuit Evaluation ---
print("\n--- 5. Short-Circuit Evaluation ---")
# Python evaluates conditions left-to-right and stops as soon as the result is known
def check_heavy_computation():
    print("Heavy computation function called!")
    return True

flag = False
# Because flag is False, the 'and' condition immediately fails without calling the function
if flag and check_heavy_computation():
    print("Condition passed")
else:
    print("Short-circuit bypassed function call safely.")
