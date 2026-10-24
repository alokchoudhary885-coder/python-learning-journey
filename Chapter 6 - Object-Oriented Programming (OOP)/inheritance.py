# Chapter 6: Inheritance in Python
# Demonstrates single, multilevel, and multiple inheritance, super(), and MRO.

# 1. Single Inheritance & super()
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def start_engine(self):
        return f"{self.brand} {self.model} engine started."


class Car(Vehicle):
    def __init__(self, brand, model, num_doors):
        super().__init__(brand, model)
        self.num_doors = num_doors

    def describe(self):
        return f"Car: {self.brand} {self.model} with {self.num_doors} doors."


# 2. Multilevel Inheritance
class ElectricCar(Car):
    def __init__(self, brand, model, num_doors, battery_capacity_kwh):
        super().__init__(brand, model, num_doors)
        self.battery_capacity_kwh = battery_capacity_kwh

    def charge(self):
        return f"Charging {self.battery_capacity_kwh} kWh battery."


# 3. Multiple Inheritance & Method Resolution Order (MRO)
class Logger:
    def log(self, message):
        print(f"[LOG]: {message}")


class Notifier:
    def notify(self, message):
        print(f"[ALERT]: {message}")


class SmartDevice(Logger, Notifier):
    def __init__(self, device_name):
        self.name = device_name

    def trigger_event(self, event_name):
        self.log(f"{self.name} received event '{event_name}'")
        self.notify(f"Push notification sent for {event_name}")


if __name__ == "__main__":
    print("--- 1. Single Inheritance ---")
    sedan = Car("Honda", "City", 4)
    print(sedan.describe())
    print(sedan.start_engine())

    print("\n--- 2. Multilevel Inheritance ---")
    ev = ElectricCar("Tata", "Nexon EV", 4, 40.5)
    print(ev.describe())
    print(ev.charge())

    print("\n--- 3. Multiple Inheritance & MRO ---")
    sensor = SmartDevice("Living Room Sensor")
    sensor.trigger_event("Motion Detected")
    print("MRO of SmartDevice:", [cls.__name__ for cls in SmartDevice.__mro__])
