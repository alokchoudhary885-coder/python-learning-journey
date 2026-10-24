# Chapter 6: Polymorphism in Python
# Demonstrates method overriding, duck typing, and operator overloading.

# 1. Method Overriding (Dynamic Polymorphism)
class Shape:
    def area(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


def print_shape_area(shape_object):
    """Polymorphic dispatch: works with any object providing an area() method."""
    print(f"Area of {type(shape_object).__name__}: {shape_object.area():.2f}")


# 2. Duck Typing ("If it walks like a duck and quacks like a duck...")
class PDFDocument:
    def export(self):
        return "Exporting to PDF document..."


class CSVDocument:
    def export(self):
        return "Exporting to CSV spreadsheet..."


def download_report(document):
    print("Action:", document.export())


# 3. Operator Overloading (Magic Dunder Methods)
class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overloading the + operator (__add__)
    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    # Overloading string representation (__str__)
    def __str__(self):
        return f"Point({self.x}, {self.y})"


if __name__ == "__main__":
    print("--- 1. Method Overriding ---")
    shapes = [Circle(5), Rectangle(4, 6), Circle(2.5)]
    for s in shapes:
        print_shape_area(s)

    print("\n--- 2. Duck Typing ---")
    download_report(PDFDocument())
    download_report(CSVDocument())

    print("\n--- 3. Operator Overloading ---")
    p1 = Point2D(3, 7)
    p2 = Point2D(5, 2)
    p3 = p1 + p2
    print(f"{p1} + {p2} = {p3}")
