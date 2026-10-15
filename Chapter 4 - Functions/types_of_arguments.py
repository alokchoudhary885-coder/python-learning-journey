# Chapter 4: Types of Function Arguments in Python
# =================================================

# 1. Positional Arguments
# Arguments are passed to the function in the correct positional order.
def calculate_simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


# 2. Keyword Arguments
# Arguments are passed by explicitly specifying the parameter names.
# Order does not matter when using keyword arguments.
def describe_student(name, age, course):
    print(f"Student: {name}, Age: {age}, Course: {course}")


# 3. Default Arguments
# If an argument is not provided during the call, the default value is used.
# Important rule: Default arguments must follow non-default arguments.
def send_email(recipient, subject="Important Notice", domain="@college.edu"):
    full_email = f"{recipient}{domain}"
    print(f"Sending email to: {full_email} | Subject: {subject}")


# 4. Variable-Length Positional Arguments (*args)
# Accepts any number of positional arguments and packs them into a tuple.
def sum_all_numbers(*args):
    print("Received args as tuple:", args)
    total = 0
    for number in args:
        total += number
    return total


# 5. Variable-Length Keyword Arguments (**kwargs)
# Accepts any number of keyword arguments and packs them into a dictionary.
def create_profile(name, **kwargs):
    print(f"Profile Name: {name}")
    print("Additional Info (kwargs dict):", kwargs)
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


# 6. Combined Example: Positional, Default, *args, and **kwargs
def process_order(customer_name, status="Pending", *items, **details):
    print(f"\nOrder for: {customer_name} (Status: {status})")
    print(f"Items ordered ({len(items)}): {items}")
    if details:
        print("Order details:", details)


if __name__ == "__main__":
    print("--- 1. Positional Arguments ---")
    interest = calculate_simple_interest(10000, 5, 2)
    print("Simple Interest:", interest)

    print("\n--- 2. Keyword Arguments ---")
    # Passing arguments out of order using keyword arguments
    describe_student(course="Data Science", name="Alok", age=21)

    print("\n--- 3. Default Arguments ---")
    send_email("alok123")  # Uses default subject and domain
    send_email("alok123", subject="Class Schedule", domain="@gmail.com")

    print("\n--- 4. Variable-Length Positional (*args) ---")
    total_1 = sum_all_numbers(10, 20, 30)
    print("Total:", total_1)
    total_2 = sum_all_numbers(5, 15, 25, 35, 45)
    print("Total:", total_2)

    print("\n--- 5. Variable-Length Keyword (**kwargs) ---")
    create_profile("Alok", city="Delhi", semester=5, grade="A")

    print("\n--- 6. Combined Arguments ---")
    process_order("Alok", "Completed", "Python Book", "Notebook", "Pen", payment="UPI", fast_delivery=True)
