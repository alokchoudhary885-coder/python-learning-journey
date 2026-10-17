# Chapter 4: Lambda Functions vs Normal def Functions
# ====================================================
# A practical comparison demonstrating when to use lambda and why
# regular 'def' functions are preferred for most real-world code.

# 1. When Lambda IS Useful: Quick, One-Line Callbacks & Sorting Keys
students = [
    {"name": "Alok", "score": 88},
    {"name": "Priya", "score": 95},
    {"name": "Rahul", "score": 72},
    {"name": "Sneha", "score": 91},
]

# Using lambda as a sorting key (ideal use case)
students_by_score = sorted(students, key=lambda s: s["score"], reverse=True)

print("--- 1. Good Use of Lambda: Sorting Key ---")
for student in students_by_score:
    print(f"  {student['name']}: {student['score']}")


# 2. Comparison: Simple Math Transformation
# Both work, but PEP 8 recommends 'def' over assigning a lambda to a variable!
# PEP 8 Rule: Always use a def statement instead of an assignment statement
# that binds a lambda expression directly to an identifier.

# Discouraged by PEP 8:
cube_lambda = lambda x: x ** 3

# Recommended by PEP 8:
def cube_def(x):
    """Return the cube of x."""
    return x ** 3


print("\n--- 2. Direct Assignment Comparison ---")
print("Lambda cube(4):", cube_lambda(4))
print("Def cube(4)   :", cube_def(4))


# 3. Why 'def' is Better: Tracebacks & Debugging
# Notice how __name__ behaves:
print("\n--- 3. Function Names in Introspection & Debugging ---")
print("Name of cube_def   :", cube_def.__name__)       # 'cube_def'
print("Name of cube_lambda:", cube_lambda.__name__)    # '<lambda>'
# In error stack traces, '<lambda>' makes it difficult to pinpoint which
# lambda caused the error when multiple lambdas exist.


# 4. Why 'def' is Better: Multi-Step Logic and Documentation
# A lambda CANNOT contain multiple statements, loops, or docstrings.

# Attempting this complex logic in lambda would be unreadable or impossible:
def calculate_grade_report(student_record):
    """
    Evaluates student score, assigns letter grade,
    and returns a formatted summary report.
    """
    name = student_record["name"]
    score = student_record["score"]

    if score >= 90:
        grade = "A+"
        status = "Distinction"
    elif score >= 75:
        grade = "A"
        status = "First Class"
    elif score >= 50:
        grade = "B"
        status = "Pass"
    else:
        grade = "F"
        status = "Fail"

    return f"{name}: {score}/100 ({grade} - {status})"


print("\n--- 4. Complex Business Logic with def ---")
for student in students:
    print(" ", calculate_grade_report(student))


# 5. Overusing Lambda Makes Code Hard to Read (Anti-pattern)
# Overly complex lambda (hard to read and debug):
bad_calc = lambda a, b, c: (a + b) * c if a > 0 else (b - a) // (c if c != 0 else 1)

# Clean, understandable 'def' equivalent:
def clean_calc(a, b, c):
    divisor = c if c != 0 else 1
    if a > 0:
        return (a + b) * c
    return (b - a) // divisor


print("\n--- 5. Readability Demonstration ---")
print("Bad Lambda Result :", bad_calc(5, 10, 2))
print("Clean Def Result  :", clean_calc(5, 10, 2))
