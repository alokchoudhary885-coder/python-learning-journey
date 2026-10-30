# Instance Variables in Python OOP

## 1. Definition
**Instance Variables** are variables that are bound to a specific object (instance) of a class. The value of an instance variable varies from one object to another. Each object maintains its own private copy of instance variables stored in its `__dict__` namespace.

---

## 2. Why We Use Instance Variables
- Real-world objects have unique identities and states. For example, two students have different names, roll numbers, and marks.
- Instance variables guarantee that modifying data for one object does not unintentionally alter or corrupt any other object's data.

---

## 3. Where and How to Declare Instance Variables

There are **3 locations** where an instance variable can be created in Python:

| Location | How to Declare | Example |
| :--- | :--- | :--- |
| **1. Inside Constructor (`__init__`)** | Using `self.variable_name = value` | `def __init__(self, name): self.name = name` |
| **2. Inside Instance Method** | Using `self.variable_name = value` | `def add_grade(self, g): self.grade = g` |
| **3. Outside the Class** | Using `object_reference.variable_name = value` | `s1 = Student()`<br>`s1.age = 21` |

> [!NOTE]
> The most recommended and standard place to declare instance variables is inside the constructor `__init__()`. This guarantees that every object begins with a well-defined initial state.

---

## 4. Where and How to Access Instance Variables

There are **2 locations** where instance variables can be accessed:

| Location | Access Syntax | Example |
| :--- | :--- | :--- |
| **1. Inside the Class** | Using `self.variable_name` | `print(self.name)` |
| **2. Outside the Class** | Using `object_reference.variable_name` | `print(s1.name)` |

---

## 5. Where and How to Delete Instance Variables

When an instance variable is no longer needed (e.g. temporary tokens, cached session data), it can be deleted using the `del` keyword in **2 locations**:

| Location | Deletion Syntax | Example |
| :--- | :--- | :--- |
| **1. Inside the Class** | `del self.variable_name` | `def clear_temp(self): del self.token` |
| **2. Outside the Class** | `del object_reference.variable_name` | `del s1.city` |

### What Happens After Deletion?
- The key is immediately removed from the object's `__dict__` dictionary.
- Attempting to access the deleted variable will raise an `AttributeError: '<ClassName>' object has no attribute '<variable_name>'`.
- Deleting an instance variable from one object **does not** delete or affect that variable in other objects of the same class.

---

## 6. How It Works Internally (`__dict__`)

Every Python object stores its instance variables inside an internal dictionary called `__dict__`.

```python
class Student:
    def __init__(self, name):
        self.name = name

s = Student("Alok")
print(s.__dict__)  # {'name': 'Alok'}

s.age = 21         # Dynamically added outside class
print(s.__dict__)  # {'name': 'Alok', 'age': 21}

del s.age          # Deleted
print(s.__dict__)  # {'name': 'Alok'}
```

---

## 7. Important Differences: Instance Variables vs Class Variables

| Feature | Instance Variable | Class / Static Variable |
| :--- | :--- | :--- |
| **Scope** | Specific to a single object | Shared across all objects of the class |
| **Memory** | Multiple copies (one per instance) | Single copy shared by all instances |
| **Created With** | `self.var` or `obj.var` | Declared directly inside class body |
| **Deletion Impact** | Deleting removes it only for that object | Deleting removes it for the entire class |

---

## 8. Common Mistakes
1. **Accessing an instance variable before creating it:**
   Calling an instance method that reads `self.course` before calling the method that creates `self.course` will trigger an `AttributeError`.
2. **Accessing an attribute after deleting it:**
   Always check with `hasattr(obj, 'var_name')` or use a `try...except AttributeError` block.
3. **Assuming `del obj.var` deletes the class variable:**
   If a class variable with the same name exists, deleting the instance variable will simply expose the class variable underneath (un-shadowing).

---

## 9. Quick Revision Notes
- Declare inside class using `self.var = val`.
- Declare outside class using `obj.var = val`.
- Access inside with `self.var`, outside with `obj.var`.
- Delete inside with `del self.var`, outside with `del obj.var`.
- Check all active instance variables of an object using `obj.__dict__`.

---

## 10. Practice Questions & Answers

### Q1: What is the output of the following code?
```python
class Test:
    def __init__(self):
        self.a = 10
    def change(self):
        self.b = 20

t = Test()
print(t.__dict__)
t.change()
print(t.__dict__)
```
**Answer:**
```text
{'a': 10}
{'a': 10, 'b': 20}
```
`self.b` is created only when `t.change()` is called.

### Q2: How can you safely delete an instance variable without crashing if it doesn't exist?
**Answer:**
```python
if hasattr(obj, 'temp_data'):
    del obj.temp_data
```

### Q3: If `t1` and `t2` are objects of class `Demo`, does `del t1.x` delete `x` from `t2`?
**Answer:** No. Each object has its own separate copy of instance variables in its own `__dict__`. Deleting from `t1` has no effect on `t2`.

### Q4: Write a class `User` that allows adding and deleting an instance variable `secret_pin`.
```python
class User:
    def __init__(self, username):
        self.username = username
        self.secret_pin = None

    def set_pin(self, pin):
        self.secret_pin = pin

    def clear_pin(self):
        if hasattr(self, "secret_pin"):
            del self.secret_pin
```

### Q5: Can we declare an instance variable inside a static method using `self`?
**Answer:** No. Static methods do not receive `self` as a parameter, so you cannot use `self.var` inside a static method.
