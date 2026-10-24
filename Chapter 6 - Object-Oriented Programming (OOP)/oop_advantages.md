# Object-Oriented Programming (OOP) in Python: Classes, Objects & Advantages

## 1. Definition
**Object-Oriented Programming (OOP)** is a programming paradigm based on the concept of **objects**, which contain data (attributes/properties) and code (methods/functions). A **class** is a blueprint or template, while an **object** is a concrete instance created from that blueprint.

## 2. Why We Use OOP & Key Advantages
1. **Modularity:** Code is organized into self-contained units (classes) that can be maintained independently.
2. **Reusability (DRY Principle):** Write once and reuse through inheritance and composition without rewriting logic.
3. **Real-World Modeling:** Maps digital software components directly to real-world entities (e.g. Bank Account, User, Student, Car).
4. **Data Security & Protection:** Encapsulation hides internal variables and prevents unauthorized external tampering.
5. **Polymorphism & Extensibility:** New features can be integrated easily without modifying existing working code.

## 3. Syntax & Fundamental Elements
```python
class ClassName:
    class_variable = "shared"  # Belongs to the class

    def __init__(self, param1, param2):
        self.instance_variable = param1  # Unique to each instance

    def instance_method(self):
        return f"Hello, {self.instance_variable}"
```

## 4. Simple Explanation: `self` and `__init__`
- **`__init__` (The Constructor):** A special initializer method automatically called when a new object is created.
- **`self`:** A reference to the specific current instance calling the method. Python passes it automatically as the first argument (`obj.method()` becomes `ClassName.method(obj)`).

## 5. Practical Example
```python
class BankAccount:
    def __init__(self, account_holder, initial_balance=0.0):
        self.holder = account_holder
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return True
        return False

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            return True
        return False

# Creating an object
account = BankAccount("Alok", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(f"{account.holder}'s Balance: Rs. {account.balance}")
```

## 6. Expected Output
```text
Alok's Balance: Rs. 1300.0
```

## 7. Important Differences: Procedural vs Object-Oriented Programming
| Feature | Procedural Programming (POP) | Object-Oriented Programming (OOP) |
|---|---|---|
| **Primary Unit** | Functions | Objects and Classes |
| **Data Focus** | Functions take precedence over data | Data and behavior are bundled together |
| **Data Security** | Data moves openly across functions | Data is hidden inside objects (encapsulation) |
| **Code Reusability** | Limited to function calls | Advanced reusability via inheritance |
| **Complexity Handling** | Becomes messy for large projects | Scales cleanly for enterprise systems |

## 8. Common Mistakes
1. **Forgetting `self` in Method Definitions:** Writing `def display():` inside a class causes `TypeError: display() takes 0 positional arguments but 1 was given`.
2. **Confusing Class and Instance Variables:** Modifying `self.college = ...` creates an instance variable overriding the class attribute for that object only, rather than changing it for all instances.
3. **Calling Class as a Function without Parentheses:** Writing `obj = Student` assigns the class itself, not an instance. You must write `obj = Student(...)`.

## 9. Short Revision Notes
- Class = Blueprint; Object = Instance.
- `__init__` initializes newly created objects.
- `self` refers to the current object.
- Class variables are shared by all instances; instance variables are unique per object.
- OOP's 4 core pillars: Encapsulation, Abstraction, Inheritance, Polymorphism.

## 10. Practice Questions with Answers

### Q1. What is the role of the `self` parameter in Python methods?
**Answer:** `self` is a reference to the current instance of the class. It allows methods to access and modify the specific object's attributes.

### Q2. How does an instance variable differ from a class variable?
**Answer:** An instance variable is tied to a specific object (defined using `self.var`), so each object has its own copy. A class variable is defined inside the class body outside any method and is shared across all instances.

### Q3. Write a Python class `Rectangle` with methods to compute area and perimeter.
**Answer:**
```python
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)
```

### Q4. Can a class exist without an `__init__` constructor method?
**Answer:** Yes. If no `__init__` method is defined, Python uses a default empty constructor.

### Q5. What is the difference between an instance method and a `@staticmethod`?
**Answer:** An instance method takes `self` and can read/modify the object's instance state. A static method takes neither `self` nor `cls`; it behaves like a regular function placed inside the class for logical grouping.
