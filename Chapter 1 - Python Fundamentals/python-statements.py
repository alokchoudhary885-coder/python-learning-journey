# Python Statements
# =================

# 1. Assignment Statement
name = "Alok"
age = 21
marks = 85

print(name)
print(age)
print(marks)


# 2. Expression Statement
print(10 + 20)
print("Hello")


# 3. Input Statement
user_name = input("Enter your name: ")
print("Hello", user_name)


# 4. Conditional Statement
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")


# 5. For Loop Statement
for i in range(5):
    print(i)


# 6. While Loop Statement
count = 1

while count <= 5:
    print(count)
    count += 1


# 7. Break Statement
for i in range(10):
    if i == 5:
        break
    print(i)


# 8. Continue Statement
for i in range(5):
    if i == 2:
        continue
    print(i)


# 9. Pass Statement
if age >= 18:
    pass


# 10. Import Statement
import math

print(math.sqrt(25))


# 11. Multiple Statements in One Line
x = 10; y = 20; print(x + y)