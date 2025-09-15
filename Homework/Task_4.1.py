class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)


rectangle1 = Rectangle(4, 5)
rectangle2 = Rectangle(7, 3)
rectangle3 = Rectangle(10, 2)

print(f"Rectangle: width = {rectangle1.width}, height = {rectangle1.height}")
print(f"Area: {rectangle1.calculate_area()}")
print(f"Perimeter: {rectangle1.calculate_perimeter()}\n")

print(f"Rectangle: width = {rectangle2.width}, height = {rectangle2.height}")
print(f"Area: {rectangle2.calculate_area()}")
print(f"Perimeter: {rectangle2.calculate_perimeter()}\n")

print(f"Rectangle: width = {rectangle3.width}, height = {rectangle3.height}")
print(f"Area: {rectangle3.calculate_area()}")
print(f"Perimeter: {rectangle3.calculate_perimeter()}")