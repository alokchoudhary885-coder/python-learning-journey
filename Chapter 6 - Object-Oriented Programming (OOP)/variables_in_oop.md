# Variables in Python OOP: Instance vs Class (Static) Variables

## 1. Definition
In Python OOP, variables defined in and around classes are divided into two main categories:
1. **Instance Variables**: Variables that belong exclusively to a particular object instance. Defined using `self.var_name` (usually inside `__init__`).
2. **Class Variables (Static Variables)**: Variables defined directly inside the class body, outside any method. They are shared across **all** instances of that class.

---

## 2. Why We Use Both
- **Instance Variables:** Store information that varies from object to object (e.g., student name, roll number, bank balance).
- **Class Variables:** Store information common to all objects of that class (e.g., bank name, interest rate, company name, total object counter), saving memory by sharing one copy.

---

## 3. Comparison Table

| Feature | Instance Variable | Class Variable (Static) |
| :--- | :--- | :--- |
| **Where Defined** | Inside methods using `self.var = value` | Inside class body, outside methods |
| **Memory Allocation** | Allocated separately for each object in its `__dict__` | Allocated once when the class is loaded in `ClassName.__dict__` |
| **Access Syntax** | `self.var` or `obj.var` | `ClassName.var` or `self.var` |
| **Modifying Syntax** | `obj.var = new_val` | `ClassName.var = new_val` |
| **Modification Impact** | Affects only that specific object | Affects all instances reading that class variable |

---

## 4. Syntax
```python
class Car:
    # Class Variable
    wheels = 4

    def __init__(self, brand, model):
        # Instance Variables
        self.brand = brand
        self.model = model
```

---

## 5. Practical Example & Namespace Inspection

```python
class Employee:
    company = "Tech Corp"

    def __init__(self, name):
        self.name = name

e1 = Employee("Alok")
e2 = Employee("Ayush")

# Checking namespaces
print(e1.__dict__)        # {'name': 'Alok'}
print(Employee.__dict__)  # Contains 'company': 'Tech Corp'
```

---

## 6. How Python Resolves Variable Lookup
When you write `e1.company`:
1. Python first checks `e1.__dict__` for an instance variable named `company`.
2. If found, it returns that value immediately.
3. If **not found**, Python looks up `Employee.__dict__` for a class variable named `company`.
4. If still not found, it traverses parent classes through MRO.
5. If nowhere found, it raises `AttributeError`.

---

## 7. The Attribute Shadowing Trap (Crucial Concept)
If you attempt to modify a class variable through an object reference:
```python
e1.company = "New Tech Corp"
```
Python **does NOT** change the class variable! Instead:
- It creates a **new instance variable** `company` inside `e1.__dict__`.
- `e2.company` and `Employee.company` still see `"Tech Corp"`.
- This is called **Attribute Shadowing**. Always update class variables using `ClassName.var = value` or `@classmethod`.

---

## 8. Common Mistakes
1. **Modifying class variables via `self.var = ...`:**
   Creates an instance attribute instead of updating the shared class variable.
2. **Mutable class variables (Lists/Dicts trap):**
   ```python
   class Team:
       members = []  # ❌ Shared list across all teams!
       def add(self, name):
           self.members.append(name)
   ```
   Calling `t1.add("Alok")` will also add `"Alok"` to `t2.members`! Always initialize mutable collections inside `__init__`:
   ```python
   def __init__(self):
       self.members = []  # ✅ Each team gets its own list
   ```

---

## 9. Quick Revision Notes
- Instance variables are unique per instance; Class variables are shared.
- Always modify class variables using `ClassName.var_name = new_value`.
- Avoid mutable default class variables (like `[]` or `{}`) unless intentionally shared.
- Inspect an object's instance variables using `object.__dict__`.

---

## 10. Practice Questions & Answers

### Q1: What is the output of the following code?
```python
class Counter:
    count = 0
    def __init__(self):
        Counter.count += 1

c1 = Counter()
c2 = Counter()
c3 = Counter()
print(Counter.count, c1.count)
```
**Answer:** `3 3`. Each object creation runs `Counter.count += 1`, incrementing the shared class variable to 3.

### Q2: Why is `self.__class__.var` used instead of `ClassName.var`?
**Answer:** `self.__class__.var` is dynamic. If a subclass inherits the method, `self.__class__` refers to the subclass rather than the hardcoded parent class.

### Q3: What is the result of `del obj.var` vs `del ClassName.var`?
**Answer:** `del obj.var` deletes an instance variable from the object's namespace. `del ClassName.var` deletes the class variable from the class definition entirely.

### Q4: How can you check if an attribute exists on an object?
**Answer:** Using the built-in `hasattr(obj, 'attribute_name')` function or `'attribute_name' in obj.__dict__`.

### Q5: Fix this buggy class where all players share the same inventory:
```python
class Player:
    inventory = []
    def pick_item(self, item):
        self.inventory.append(item)
```
**Answer:**
```python
class Player:
    def __init__(self):
        self.inventory = []  # Instance variable unique to each player

    def pick_item(self, item):
        self.inventory.append(item)
```
