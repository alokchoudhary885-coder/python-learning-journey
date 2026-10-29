# Types of Methods in Python OOP

## 1. Definition
In Python, methods inside a class are categorized into three distinct types based on what scope or state they access:
1. **Instance Methods**: Bound to an individual object; access and modify instance state using `self`.
2. **Class Methods**: Bound to the class itself; access and modify class-level state using `cls` via `@classmethod`.
3. **Static Methods**: Independent helper functions logically grouped inside the class; do not receive `self` or `cls`, decorated with `@staticmethod`.

---

## 2. Why We Use Different Methods
- **Instance Methods:** Every object has its own data (e.g., student name, account balance). Instance methods let each object interact with its own data.
- **Class Methods:** When an operation applies to all objects uniformly (e.g., changing school name, tracking total registrations, or creating alternative constructors).
- **Static Methods:** When logic belongs inside the class namespace for clarity (e.g., validating an email, date conversions, or mathematical formulas), but doesn't require reading or mutating instance or class variables.

---

## 3. Comparison Table

| Feature | Instance Method | Class Method (`@classmethod`) | Static Method (`@staticmethod`) |
| :--- | :--- | :--- | :--- |
| **First Parameter** | `self` (the instance) | `cls` (the class) | None (regular arguments only) |
| **Decorator** | None required | `@classmethod` | `@staticmethod` |
| **Can Access Instance Variables?** | Yes (`self.attribute`) | No | No |
| **Can Access Class Variables?** | Yes (`self.class_var`) | Yes (`cls.class_var`) | Yes (via `ClassName.var`) |
| **How to Call** | `obj.method()` | `ClassName.method()` or `obj.method()` | `ClassName.method()` or `obj.method()` |
| **Primary Use Case** | Modifying object state | Factory constructors, updating class state | Utility/helper functions |

---

## 4. Syntax

```python
class Demo:
    class_var = 100

    def instance_method(self, x):
        # Has access to self
        return self.class_var + x

    @classmethod
    def class_method(cls, new_val):
        # Has access to cls
        cls.class_var = new_val

    @staticmethod
    def static_method(a, b):
        # Pure function, no self or cls
        return a + b
```

---

## 5. Practical Example (Factory Pattern & Validation)

```python
class Student:
    school_name = "Kendriya Vidyalaya"

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Instance Method
    def get_info(self):
        return f"{self.name} ({self.age} yrs) - School: {self.school_name}"

    # Class Method (Alternative Constructor)
    @classmethod
    def from_string(cls, data_string):
        # Parses "Alok,21" and returns a new Student instance
        name, age_str = data_string.split(",")
        return cls(name.strip(), int(age_str.strip()))

    # Static Method (Utility Validator)
    @staticmethod
    def is_eligible(age):
        return age >= 5
```

---

## 6. How Factory Constructors Work via `@classmethod`
Instead of forcing users to only create objects with `Student("Alok", 21)`, class methods allow alternative input formats:
```python
s1 = Student("Alok", 21)                    # Standard constructor
s2 = Student.from_string("Ayush, 22")       # Alternative factory constructor
```
`cls(name, age)` inside the class method creates and returns an instance of `Student` (or any subclass that called it).

---

## 7. Important Differences from Normal Functions
- Static methods inside a class prevent global namespace pollution.
- Static methods can be overridden by subclasses if needed.
- Calling `obj.instance_method()` passes `obj` as `self` under the hood (`ClassName.instance_method(obj)`).

---

## 8. Common Mistakes
1. **Calling `@classmethod` without `cls`:**
   ```python
   # ❌ TypeError
   @classmethod
   def update(new_val):
       pass
   ```
   First argument is always `cls`.
2. **Accessing instance variables inside static or class methods:**
   ```python
   # ❌ NameError / AttributeError
   @staticmethod
   def show():
       print(self.name)  # 'self' does not exist here!
   ```
3. **Forgetting `@classmethod` or `@staticmethod` decorators:**
   If you omit `@staticmethod` and do not provide `self`, Python will treat it as an instance method and raise a `TypeError` when called on an object!

---

## 9. Quick Revision Notes
- Use **Instance Method** when you need `self`.
- Use **Class Method** when you need `cls` (e.g., factory methods or modifying class variables).
- Use **Static Method** when you need neither `self` nor `cls`.
- All three can be called from an instance or from the class directly.

---

## 10. Practice Questions & Answers

### Q1: Can a static method access class variables?
**Answer:** Yes, by referencing the class name explicitly (e.g. `ClassName.variable_name`), but not through a `cls` parameter.

### Q2: Why is `@classmethod` preferred over hardcoding the class name for factory constructors?
**Answer:** Because `cls` respects inheritance. If a subclass inherits the class method, `cls(...)` will instantiate the subclass rather than the parent class.

### Q3: When should a method be declared `@staticmethod`?
**Answer:** When the method does not read or modify instance data (`self`) or class data (`cls`), but its functionality logically belongs inside that class (such as input validation or math conversion).

### Q4: What does the following code print?
```python
class Test:
    count = 0
    @classmethod
    def inc(cls):
        cls.count += 1

t1 = Test()
t2 = Test()
t1.inc()
t2.inc()
print(Test.count)
```
**Answer:** Output is `2`. Both `t1.inc()` and `t2.inc()` modify the shared `Test.count` via `cls`.

### Q5: Write a `Temperature` class with static methods `to_celsius(f)` and `to_fahrenheit(c)`.
```python
class Temperature:
    @staticmethod
    def to_celsius(f):
        return (f - 32) * 5 / 9

    @staticmethod
    def to_fahrenheit(c):
        return (c * 9 / 5) + 32
```
