# Chapter 4: Lambda Functions & filter() in Python
# ==================================================
# A lambda function is a small, anonymous (unnamed) function.
# It can take any number of arguments, but can only contain ONE expression.
# Syntax:
#     lambda arguments: expression

# 1. Basic Lambda Functions
# Traditional function:
# def square(x):
#     return x * x
square = lambda x: x * x

# Lambda with multiple arguments:
add = lambda a, b: a + b

# Lambda with three arguments:
multiply_three = lambda a, b, c: a * b * c

print("Square of 6:", square(6))
print("Add 10 and 25:", add(10, 25))
print("Multiply 2 * 3 * 4:", multiply_three(2, 3, 4))


# 2. Lambda with Ternary Operator
# Format: lambda args: true_value if condition else false_value
is_even = lambda n: "Even" if n % 2 == 0 else "Odd"
get_max = lambda x, y: x if x > y else y

print("\n--- Lambda with Ternary Operator ---")
print("14 is:", is_even(14))
print("21 is:", is_even(21))
print("Max of 40 and 75:", get_max(40, 75))


# 3. The filter() Built-in Function
# filter(function, iterable) extracts elements from an iterable for which the function returns True.
# It returns a filter object (an iterator), which can be converted to a list using list().

numbers = [12, 17, 24, 35, 40, 51, 60, 73, 88]

# Example A: Filtering even numbers
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print("\n--- filter() with Lambda ---")
print("Original Numbers:", numbers)
print("Even Numbers    :", even_numbers)

# Example B: Filtering odd numbers
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))
print("Odd Numbers     :", odd_numbers)

# Example C: Filtering passing scores (>= 50)
exam_scores = [35, 88, 42, 95, 60, 48, 72]
passing_scores = list(filter(lambda score: score >= 50, exam_scores))
print("Exam Scores     :", exam_scores)
print("Passing Scores  :", passing_scores)

# Example D: Filtering names starting with 'A'
student_names = ["Alok", "Rahul", "Amit", "Priya", "Ankit", "Sneha"]
names_starting_with_a = list(filter(lambda name: name.startswith("A"), student_names))
print("Students with 'A':", names_starting_with_a)


# 4. Comparison: filter() vs Traditional for-loop
def get_evens_traditional(num_list):
    result = []
    for num in num_list:
        if num % 2 == 0:
            result.append(num)
    return result


print("\nTraditional loop result matches filter()?:", get_evens_traditional(numbers) == even_numbers)
