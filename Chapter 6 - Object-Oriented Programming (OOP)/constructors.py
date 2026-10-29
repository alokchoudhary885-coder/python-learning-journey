# Constructors in Python OOP
# ===========================
# A constructor is a special method called automatically when a new object is created.
# In Python, the constructor is named `__init__`.


# --- 1. Default Constructor ---
# If we do not write __init__, Python provides a default empty constructor.
class EmptyStudent:
    pass


s1 = EmptyStudent()
print("--- 1. Default Constructor ---")
print("EmptyStudent object created:", s1)


# --- 2. Non-Parameterized Constructor ---
# A constructor that takes only 'self' and initializes default values.
class Course:
    def __init__(self):
        self.course_name = "Python Programming"
        self.duration_weeks = 8

    def show_info(self):
        print(f"Course: {self.course_name} | Duration: {self.duration_weeks} weeks")


print("\n--- 2. Non-Parameterized Constructor ---")
c1 = Course()
c1.show_info()


# --- 3. Parameterized Constructor (Standard Practice) ---
# A constructor that accepts custom arguments during object instantiation.
# (Similar to Grras classroom Employee example)
class Employee:
    def __init__(self, emp_id, emp_name, city, age):
        self.e_id = emp_id
        self.e_name = emp_name
        self.city = city
        self.age = age

    def display(self):
        print(f"ID: {self.e_id} | Name: {self.e_name} | City: {self.city} | Age: {self.age}")


print("\n--- 3. Parameterized Constructor ---")
emp1 = Employee("101", "Alok", "Jaipur", 21)
emp2 = Employee("102", "Ayush", "Ratlam", 24)
emp1.display()
emp2.display()


# --- 4. Constructor with Default Parameter Values ---
# Gives flexibility: pass arguments or fallback to defaults.
class Product:
    def __init__(self, name, price, stock=10, category="General"):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category

    def get_summary(self):
        return f"{self.name} (Cat: {self.category}) - Rs. {self.price} [Stock: {self.stock}]"


print("\n--- 4. Constructor with Default Values ---")
p1 = Product("Laptop", 55000.0, stock=5, category="Electronics")
p2 = Product("Notebook", 45.0)  # uses default stock=10, category="General"
print(p1.get_summary())
print(p2.get_summary())


# --- 5. Demystifying 'self': Memory Address Proof ---
# 'self' refers to the current object instance in memory.
class MemoryCheck:
    def __init__(self):
        print("Inside __init__, id(self) is :", id(self))


print("\n--- 5. 'self' Reference Verification ---")
obj = MemoryCheck()
print("Outside class,  id(obj) is  :", id(obj))
print("Are they identical?", id(obj) == id(obj))
