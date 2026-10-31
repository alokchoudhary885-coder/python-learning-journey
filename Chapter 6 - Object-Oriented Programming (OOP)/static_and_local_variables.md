# Static, Instance, and Local Variables in Python OOP

## 1. Overview & Definition

In Python Object-Oriented Programming, all variables fall into **three fundamental categories** based on their declaration, scope, and memory lifetime:

| Variable Type | Bound To | Memory Location | How Many Copies? |
| :--- | :--- | :--- | :--- |
| **1. Static / Class Variable** | Class | Class namespace dictionary (`ClassName.__dict__`) | **Only 1 copy** shared by all objects |
| **2. Instance Variable** | Object / Instance | Individual object dictionary (`obj.__dict__`) | **One copy per object** |
| **3. Local Variable** | Method / Function | Stack frame (temporary execution stack) | Created on call, destroyed on return |

---

## 2. Why & When to Use Each Type

- **Static Variable:** Use when a property is **identical and shared** across all objects of a class (e.g. Bank name, IFSC code, College name, Mathematical constants like $\pi$, Object counters).
- **Instance Variable:** Use when each object must maintain its **own unique identity and data** (e.g. Student roll number, Account balance, Employee name).
- **Local Variable:** Use for **temporary intermediate calculations** that are only needed while a specific method runs and should not be saved permanently on the object (e.g. tax slabs, discount rates, loop counters).

---

## 3. The 6 Places to Declare Static Variables in Python

A static variable can be declared in **6 distinct locations**:

```python
class Demo:
    # 1. Directly inside class body (Standard practice)
    a = 10

    def __init__(self):
        # 2. Inside constructor using ClassName
        Demo.b = 20

    def instance_method(self):
        # 3. Inside instance method using ClassName
        Demo.c = 30

    @classmethod
    def class_method(cls):
        # 4. Inside class method using cls or ClassName
        cls.d = 40
        Demo.e = 50

    @staticmethod
    def static_method():
        # 5. Inside static method using ClassName
        Demo.f = 60

# 6. Outside the class using ClassName
Demo.g = 70
```

> [!IMPORTANT]
> Always use `ClassName.var = value` (or `cls.var = value` inside a `@classmethod`) to declare or modify static variables. Never use `self.var = value`, as that creates an instance variable instead!

---

## 4. Where and How to Access Static Variables

Static variables can be accessed in several places:

```python
class Student:
    college = "National University"

    def __init__(self):
        # Inside constructor:
        print(Student.college)  # Recommended
        print(self.college)     # Valid (falls back to class variable)

    def show(self):
        # Inside instance method:
        print(Student.college)

    @classmethod
    def show_class(cls):
        # Inside class method:
        print(cls.college)

    @staticmethod
    def show_static():
        # Inside static method:
        print(Student.college)

# Outside class:
s = Student()
print(Student.college)  # Recommended
print(s.college)        # Valid via object reference
```

---

## 5. Modifying Static Variables vs The Shadowing Trap

### Correct Modification (Global Update):
```python
Student.college = "Apex University"
# Now ALL existing and future student objects will see "Apex University".
```

### The Shadowing Trap (Beginner Mistake):
```python
s1 = Student()
s1.college = "Harvard"  # ❌ Does NOT change Student.college!
```
- What happens: Python creates a **new instance variable** `college` inside `s1.__dict__`.
- Result: `s1.college` gives `"Harvard"`, but `Student.college` and other students (`s2.college`) still see `"Apex University"`.
- This is called **Attribute Shadowing**.

---

## 6. Local Variables: Scope & Stack Lifecycle

Local variables are declared directly inside a method without `self` or `cls`:

```python
class SalaryCalculator:
    def compute(self, basic):
        # 'hra' and 'da' are local variables
        hra = basic * 0.20
        da = basic * 0.10
        total = basic + hra + da
        return total
```

### Key Rules of Local Variables:
1. **Scope:** Limited strictly to the method in which they are declared.
2. **Cannot be accessed outside:** Attempting `print(hra)` outside the method raises `NameError: name 'hra' is not defined`.
3. **Cannot be shared across methods:** A local variable declared in `method1()` cannot be directly read inside `method2()`.
4. **Memory:** Stored in the function call stack frame. As soon as the method finishes, the stack frame is popped and the memory is released immediately.

---

## 7. Master Comparison Table

| Dimension | Static / Class Variable | Instance Variable | Local Variable |
| :--- | :--- | :--- | :--- |
| **Where Declared** | Inside class body or using `ClassName.var` | Inside methods with `self.var` or outside with `obj.var` | Inside method without `self` |
| **Where Stored** | In class dictionary (`ClassName.__dict__`) | In object dictionary (`obj.__dict__`) | In execution call stack |
| **Number of Copies** | **1 copy** shared across all instances | **1 copy per object** | Created on function call |
| **Lifetime** | Exists from class load until program terminates | Exists while object is alive in memory | Exists only while method executes |
| **Access Syntax** | `ClassName.var` (or `cls.var`, `self.var`) | `self.var` or `obj.var` | Plain variable name `var` |
| **Modifying Syntax** | `ClassName.var = new_val` | `self.var = new_val` | `var = new_val` |
| **Can Be Accessed Outside?** | Yes (`ClassName.var`) | Yes (`obj.var`) | **No** (Raises `NameError`) |

---

## 8. Common Mistakes

1. **Attempting to share local variables across methods:**
   ```python
   class Demo:
       def m1(self):
           x = 10
       def m2(self):
           print(x)  # ❌ NameError: name 'x' is not defined
   ```
   *Fix:* Make it an instance variable (`self.x = 10`) if you need it in multiple methods.

2. **Modifying static variables via `self` or `obj`:**
   ```python
   s1.bank_name = "New Bank"  # Creates instance variable, does not update class
   ```
   *Fix:* Use `Bank.bank_name = "New Bank"`.

3. **Mutable static variables (List/Dict Trap):**
   ```python
   class Batch:
       students = []  # ❌ Shared list! All batches will append to the same list.
   ```
   *Fix:* Put mutable collections in `__init__` as instance variables: `self.students = []`.

---

## 9. Quick Revision Notes

- If data varies from object to object -> **Instance Variable** (`self.name = ...`).
- If data is common to all objects -> **Static Variable** (`company = "TCS"`).
- If data is temporary for computation -> **Local Variable** (`tax = salary * 0.1`).
- Modify static variables strictly using **`ClassName.var = new_value`**.
- Inspect object attributes using **`obj.__dict__`** and class attributes using **`ClassName.__dict__`**.

---

## 10. Practice Questions & Answers

### Q1: What is the output of the following code?
```python
class Test:
    x = 10
    def __init__(self):
        self.y = 20

t1 = Test()
t2 = Test()
Test.x = 99
t1.y = 88
print(t1.x, t1.y)
print(t2.x, t2.y)
```
**Answer:**
```text
99 88
99 20
```
`Test.x = 99` updates the single shared static variable for both objects. `t1.y = 88` updates only `t1`'s private instance variable.

### Q2: Can a local variable have the same name as a static variable?
**Answer:** Yes. Inside the method, writing the bare variable name references the local variable. To access the static variable from the same method, use `ClassName.var_name`.

### Q3: Where are local variables stored in memory?
**Answer:** Local variables are stored in the function's stack frame on the call stack, unlike instance and static variables which reside on the heap inside dictionary namespaces.

### Q4: How many copies of an instance variable are created if you instantiate 100 objects?
**Answer:** 100 independent copies (one inside each object's `__dict__`).

### Q5: How many copies of a static variable are created if you instantiate 100 objects?
**Answer:** Exactly 1 copy, stored in the class namespace.

### Q6: Write a class `BankAccount` demonstrating all 3 variable types in action:
```python
class BankAccount:
    bank_name = "HDFC Bank"  # Static variable

    def __init__(self, holder, balance):
        self.holder = holder      # Instance variable
        self.balance = balance    # Instance variable

    def calculate_interest(self):
        rate = 4.5                # Local variable
        return (self.balance * rate) / 100
```
