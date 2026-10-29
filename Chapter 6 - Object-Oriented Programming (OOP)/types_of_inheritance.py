# All 5 Types of Inheritance in Python OOP
# ==========================================
# 1. Single Inheritance
# 2. Multilevel Inheritance
# 3. Multiple Inheritance (with Diamond Problem & MRO)
# 4. Hierarchical Inheritance
# 5. Hybrid Inheritance
# + Using `super()` for clean parent constructor delegation


# --- 1. Single Inheritance ---
# One child class derives from one parent class
class Device:
    def __init__(self, brand, power_watts):
        self.brand = brand
        self.power_watts = power_watts

    def power_info(self):
        return f"{self.brand} consumes {self.power_watts}W"


class Smartphone(Device):
    def __init__(self, brand, power_watts, os_name):
        super().__init__(brand, power_watts)  # Delegates to Device.__init__
        self.os_name = os_name

    def device_specs(self):
        return f"{self.power_info()} | OS: {self.os_name}"


# --- 2. Multilevel Inheritance ---
# A class derives from a child class (Grandparent -> Parent -> Child)
class Vehicle:
    def __init__(self, make):
        self.make = make


class FourWheeler(Vehicle):
    def __init__(self, make, fuel_type):
        super().__init__(make)
        self.fuel_type = fuel_type


class ElectricCar(FourWheeler):
    def __init__(self, make, battery_kwh):
        super().__init__(make, fuel_type="Electric")
        self.battery_kwh = battery_kwh

    def display(self):
        return f"{self.make} [{self.fuel_type}] - Battery: {self.battery_kwh} kWh"


# --- 3. Multiple Inheritance & Diamond Problem ---
# A child inherits from two or more parent classes
class Writer:
    def write(self):
        return "Writing technical articles."


class Coder:
    def code(self):
        return "Writing Python programs."


# TechLead inherits from both Writer and Coder
class TechBlogger(Writer, Coder):
    def profile(self):
        return f"Daily activities: {self.write()} AND {self.code()}"


# --- Diamond Problem Demo ---
class Base:
    def greet(self):
        return "Base Greeting"


class Left(Base):
    def greet(self):
        return "Left Greeting"


class Right(Base):
    def greet(self):
        return "Right Greeting"


class Child(Left, Right):
    pass


# --- 4. Hierarchical Inheritance ---
# Multiple child classes inherit from a single parent class
class BankUser:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name


class SavingsCustomer(BankUser):
    def account_type(self):
        return f"Customer {self.name} holds a Savings Account."


class BusinessCustomer(BankUser):
    def account_type(self):
        return f"Corporate User {self.name} holds a Current Account."


# --- 5. Hybrid Inheritance ---
# Combination of two or more types of inheritance
class CollegeMember:
    def __init__(self, name):
        self.name = name


class StudentMember(CollegeMember):
    def role(self):
        return "Learner"


class SportsMember(CollegeMember):
    def sport(self):
        return "Cricket"


# SportsScholar inherits from both StudentMember and SportsMember (Hierarchical + Multiple)
class SportsScholar(StudentMember, SportsMember):
    def scholarship_info(self):
        return f"{self.name} is a {self.role()} playing {self.sport()} on a scholarship."


if __name__ == "__main__":
    print("--- 1. Single Inheritance ---")
    phone = Smartphone("Samsung", 25, "Android 14")
    print(phone.device_specs())

    print("\n--- 2. Multilevel Inheritance ---")
    ev = ElectricCar("Tesla", 85)
    print(ev.display())

    print("\n--- 3. Multiple Inheritance & MRO ---")
    author = TechBlogger()
    print(author.profile())

    diamond_obj = Child()
    print("Diamond greeting resolves to:", diamond_obj.greet())
    print("Method Resolution Order (MRO) for Child:")
    for cls in Child.__mro__:
        print(" ->", cls.__name__)

    print("\n--- 4. Hierarchical Inheritance ---")
    u1 = SavingsCustomer("U101", "Alok")
    u2 = BusinessCustomer("B202", "Alok Enterprises")
    print(u1.account_type())
    print(u2.account_type())

    print("\n--- 5. Hybrid Inheritance ---")
    scholar = SportsScholar("Rahul")
    print(scholar.scholarship_info())
