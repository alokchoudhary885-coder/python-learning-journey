# The 4 Pillars of Object-Oriented Programming (OOP)

## 1. Definition
The four core pillars of Object-Oriented Programming are **Encapsulation** (bundling data and hiding internal state), **Abstraction** (exposing only essential interfaces while concealing implementation details), **Inheritance** (deriving new classes from existing ones), and **Polymorphism** (allowing different classes to be treated through a unified interface).

## 2. Summary of the 4 Pillars
| Pillar | Core Concept | Python Implementation |
|---|---|---|
| **Encapsulation** | Data hiding & access control | Public, protected (`_`), private (`__`) attributes, `@property` getters/setters |
| **Abstraction** | Enforcing blueprints & contracts | `from abc import ABC, abstractmethod` |
| **Inheritance** | Code reuse & parent-child hierarchies | `class Child(Parent):`, `super().__init__()` |
| **Polymorphism** | "Many forms" — unified method names | Method overriding, duck typing, operator overloading (`__add__`) |

## 3. Syntax Reference
```python
# Encapsulation
class Account:
    def __init__(self):
        self.__balance = 0  # Private

# Abstraction
from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self): pass

# Inheritance
class Dog(Animal):
    def make_sound(self): return "Bark"

# Polymorphism
def sound(entity):
    print(entity.make_sound())
```

## 4. Simple Explanation of How They Work Together
- **Abstraction** sets the rules: What *must* be done (e.g. `Vehicle` requires a `start()` method).
- **Encapsulation** protects the state: How values are stored safely (e.g. `fuel_level` cannot be set to a negative number).
- **Inheritance** eliminates duplication: Children inherit generic logic from parents (e.g. `Car` inherits `brand` from `Vehicle`).
- **Polymorphism** enables flexible execution: The caller doesn't need to know whether an object is a `Car`, `Boat`, or `Plane`—calling `.start()` works seamlessly for all of them.

## 5. Practical Example
```python
# Polymorphism with inheritance
class Employee:
    def __init__(self, name, base_salary):
        self.name = name
        self.base_salary = base_salary

    def calculate_bonus(self):
        return self.base_salary * 0.05

class Manager(Employee):
    def calculate_bonus(self):
        return self.base_salary * 0.20  # Overridden for managers

staff = [Employee("Alok", 40000), Manager("Priya", 80000)]
for member in staff:
    print(f"{member.name}'s Bonus: Rs. {member.calculate_bonus():,.2f}")
```

## 6. Expected Output
```text
Alok's Bonus: Rs. 2,000.00
Priya's Bonus: Rs. 16,000.00
```

## 7. Important Differences: Abstraction vs Encapsulation
| Feature | Encapsulation | Abstraction |
|---|---|---|
| **Focus** | How data is protected and bundled | What features are visible to the outside world |
| **Implementation** | Access modifiers (`_`, `__`), getters/setters | Abstract Base Classes (`ABC`, `@abstractmethod`) |
| **Level** | Implementation-level data hiding | Design-level interface specification |

## 8. Common Mistakes
1. **Directly Accessing Private Attributes:** Calling `obj.__pin` raises `AttributeError`. Use provided getter methods or public APIs.
2. **Forgetting to Implement Abstract Methods:** If a subclass inherits from an `ABC` but forgets to implement an `@abstractmethod`, Python refuses to instantiate it (`TypeError`).
3. **MRO Diamond Problem in Multiple Inheritance:** Unintended method resolution order when multiple parents share a common ancestor. Use `Class.__mro__` to inspect order.

## 9. Short Revision Notes
- Encapsulation = Data Hiding.
- Abstraction = Interface Contract.
- Inheritance = Code Reusability.
- Polymorphism = Common Interface, Different Behaviors.
- `super()` calls the parent method safely according to MRO.

## 10. Practice Questions with Answers

### Q1. How does Python enforce private attributes?
**Answer:** Python performs **Name Mangling**, transforming `__attribute` into `_ClassName__attribute` to prevent accidental external access and name collisions in subclasses.

### Q2. What happens if you try to instantiate an abstract class directly?
**Answer:** Python raises `TypeError: Can't instantiate abstract class ... without an implementation for abstract method ...`.

### Q3. What is the role of `super().__init__()` in a child class?
**Answer:** It calls the constructor of the parent class according to the Method Resolution Order (MRO), ensuring the parent's attributes are initialized properly.

### Q4. What is "Duck Typing" in Python?
**Answer:** It is a dynamic polymorphism concept based on the phrase: *"If it walks like a duck and quacks like a duck, it's a duck."* Python focuses on whether an object has the required method or attribute, rather than checking its exact class type.

### Q5. How do you overload the `+` operator for a custom class in Python?
**Answer:** By defining the special magic dunder method `__add__(self, other)` inside the class.
