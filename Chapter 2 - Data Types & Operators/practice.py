# Chapter 2 Practice: Data Types, Conversion & Operators

# 1. Basic Data Types
age = 21
name = "Alok"
temperature = 98.6
is_student = True

print("age:", age, type(age))
print("name:", name, type(name))
print("temperature:", temperature, type(temperature))
print("is_student:", is_student, type(is_student))


# 2. Type Conversion
numeric_string = "10"
converted_int = int(numeric_string)
converted_float = float(numeric_string)

print("\nType Conversion:")
print("Converted to int:", converted_int, type(converted_int))
print("Converted to float:", converted_float, type(converted_float))


# 3. Arithmetic Operators
a = 10
b = 3

print("\nArithmetic Operators:")
print("a + b =", a + b)
print("a - b =", a - b)
print("a * b =", a * b)
print("a / b =", a / b)
print("a % b =", a % b)
print("a ** b =", a ** b)
print("a // b =", a // b)


# 4. Comparison Operators
x = 10
y = 5

print("\nComparison Operators:")
print("x == y:", x == y)
print("x > y :", x > y)
print("x < y :", x < y)
print("x != y:", x != y)


# 5. Logical Operators
user_age = 21
has_id = True

print("\nLogical Operators:")
print("user_age >= 18 and has_id:", user_age >= 18 and has_id)
print("user_age >= 18 or has_id :", user_age >= 18 or has_id)
print("not has_id               :", not has_id)