# Chapter 4: Variable Scope — Local and Global Variables
# ========================================================

# 1. Global Variable
# A variable defined outside any function is global.
# It can be read by any function in this file.
app_name = "Python Learning App"
user_count = 100


def show_app_details():
    # Reading global variables inside a function
    print("Inside show_app_details():")
    print("  App Name:", app_name)
    print("  Current Users:", user_count)


# 2. Local Variable
# A variable defined inside a function is local to that function.
# It exists only while the function is running.
def calculate_discount(price):
    discount_rate = 0.10  # Local variable
    discount_amount = price * discount_rate  # Local variable
    print(f"Inside calculate_discount(): Discount = Rs. {discount_amount}")
    return price - discount_amount


# 3. Variable Shadowing (Local vs Global with the same name)
counter = 10  # Global variable


def reset_counter_locally():
    counter = 0  # This creates a NEW local variable named 'counter'
    print("Inside reset_counter_locally(): local counter =", counter)


# 4. Modifying Global Variables using the 'global' Keyword
# Without 'global', assigning to a variable inside a function creates a local variable.
total_score = 50


def add_bonus(points):
    global total_score  # Informs Python to use the module-level global variable
    total_score += points
    print(f"Inside add_bonus(): updated global total_score = {total_score}")


# 5. Execution and Verification
if __name__ == "__main__":
    print("--- 1. Reading Global Variables ---")
    show_app_details()

    print("\n--- 2. Local Variables Scope ---")
    final_price = calculate_discount(500)
    print("Final price returned:", final_price)
    # Trying to access `discount_rate` here would raise NameError:
    # print(discount_rate)  # NameError: name 'discount_rate' is not defined

    print("\n--- 3. Variable Shadowing ---")
    print("Before calling reset_counter_locally(), global counter =", counter)
    reset_counter_locally()
    print("After calling reset_counter_locally(), global counter =", counter)

    print("\n--- 4. Modifying with 'global' Keyword ---")
    print("Before bonus, total_score =", total_score)
    add_bonus(25)
    print("After bonus, total_score =", total_score)
