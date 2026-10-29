# Types of Inheritance & `super()` in Python OOP

## 1. Definition
**Inheritance** is a mechanism where a new class (derived / child / subclass) adopts attributes and methods from an existing class (base / parent / superclass).

It allows code reusability, establishes an "IS-A" relationship (e.g., `Dog` IS-A `Animal`), and provides a clean foundation for method overriding and polymorphism.

---

## 2. Why We Use Inheritance
1. **Code Reusability:** Write standard logic once in the parent class; avoid duplicating code across multiple related classes.
2. **Extensibility:** Add new specialized features in child classes without modifying existing, tested parent classes (Open-Closed Principle).
3. **Consistency:** Enforces a shared interface and common properties across child classes.

---

## 3. The 5 Types of Inheritance

```text
1. Single:       Parent ----> Child
2. Multilevel:   Grandparent ----> Parent ----> Child
3. Multiple:     ParentA + ParentB ----> Child
4. Hierarchical: Parent ----> ChildA & ChildB
5. Hybrid:       Combination (e.g. Hierarchical + Multiple)
```

| Type | Structure | Description |
| :--- | :--- | :--- |
| **Single** | `A -> B` | One child inherits from one parent class. |
| **Multilevel** | `A -> B -> C` | Child inherits from a class which itself is a child of another class. |
| **Multiple** | `(A, B) -> C` | Child inherits simultaneously from two or more parent classes. |
| **Hierarchical** | `A -> (B, C)` | Multiple children inherit from a single common parent class. |
| **Hybrid** | Mixed | Any combination of two or more of the above forms. |

---

## 4. Syntax & The `super()` Function
The built-in `super()` function allows a child class to call methods and constructors of its parent without hardcoding the parent's class name:

```python
class Parent:
    def __init__(self, name):
        self.name = name

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name)  # Clean parent delegation
        self.age = age
```

---

## 5. Multiple Inheritance & The Diamond Problem

When class `D` inherits from `B` and `C`, and both `B` and `C` inherit from `A`:
```text
      A
     / \
    B   C
     \ /
      D
```
If both `B` and `C` implement method `test()`, which one does `D.test()` call?
- Python solves this deterministically using **Method Resolution Order (MRO)** powered by the **C3 Linearization Algorithm**.
- Search order: `D -> B -> C -> A -> object`.
- You can inspect the lookup order of any class with `ClassName.__mro__` or `ClassName.mro()`.

---

## 6. Practical Example (All 5 Types Demo)

```python
# Single
class Animal:
    def speak(self): return "Sound"

class Dog(Animal):
    def speak(self): return "Bark"

# Multilevel
class Puppy(Dog):
    def weep(self): return "Whimper"

# Multiple
class Flyer:
    def fly(self): return "Flying high"

class Swimmer:
    def swim(self): return "Swimming deep"

class Duck(Flyer, Swimmer):
    pass

# Hierarchical
class Cat(Animal):
    def speak(self): return "Meow"
```

---

## 7. `isinstance()` vs `issubclass()`
- `isinstance(object, Class)`: Checks if an object is an instance of a class or any of its subclasses.
  ```python
  d = Dog()
  print(isinstance(d, Animal))  # True
  ```
- `issubclass(SubClass, SuperClass)`: Checks if a class directly or indirectly inherits from another class.
  ```python
  print(issubclass(Puppy, Animal))  # True
  ```

---

## 8. Common Mistakes
1. **Calling `Parent.__init__(self)` instead of `super().__init__()`:**
   In multiple inheritance, hardcoding parent names can lead to duplicate initialization of base classes. Always prefer `super()`.
2. **Violating MRO order in multiple inheritance:**
   If inheritance order violates C3 linearization (e.g. subclass listed before superclass in parents tuple), Python raises `TypeError: Cannot create a consistent method resolution order (MRO)`.
3. **Forgetting to pass required parent arguments:**
   If `Parent` constructor requires `name`, calling `super().__init__()` with 0 args raises `TypeError`.

---

## 9. Quick Revision Notes
- Python fully supports multiple inheritance (unlike Java).
- `super()` dynamically follows the MRO chain.
- Every class in Python 3 implicitly inherits from the built-in `object` base class.
- Use `ClassName.__mro__` to view the search path Python takes when finding methods or attributes.

---

## 10. Practice Questions & Answers

### Q1: What does `Child.mro()` return?
**Answer:** It returns a list of classes in the exact order Python will search when looking for methods and attributes on an instance of `Child`, ending at `object`.

### Q2: Why is multiple inheritance sometimes considered risky, and how does Python mitigate it?
**Answer:** It can cause ambiguity when two parents define methods with identical names (Diamond problem). Python mitigates this using C3 Linearization (MRO) which guarantees a predictable, depth-first, left-to-right lookup order.

### Q3: What is the output of `isinstance(True, int)` in Python?
**Answer:** `True`. In Python, the `bool` class is an internal subclass of `int` (`issubclass(bool, int) == True`).

### Q4: How do you override a parent method in a child class while still calling the parent's implementation?
**Answer:**
```python
class Parent:
    def greet(self):
        print("Hello from Parent")

class Child(Parent):
    def greet(self):
        super().greet()  # Calls parent method
        print("Hello from Child")
```

### Q5: Write a 3-level multilevel inheritance hierarchy: `Person` -> `Employee` -> `Manager`.
```python
class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, emp_id):
        super().__init__(name)
        self.emp_id = emp_id

class Manager(Employee):
    def __init__(self, name, emp_id, department):
        super().__init__(name, emp_id)
        self.department = department
```
