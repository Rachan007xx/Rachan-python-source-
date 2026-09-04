# Part 1
# example

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    # Method to get the area
    def get_area(self):
        return self.length * self.width

    # Method to get the perimeter
    def get_perimeter(self):
        return 2 * (self.length + self.width)


rect = Rectangle(10, 5)
print(rect.get_area())       # Should print 50
print(rect.get_perimeter())  # Should print 30


# Part 2
# example

def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")


print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()


# Part 3
# example    

def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()


print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


# Part 4
# example

def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    result = a + b
    return result


print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()


# Part 5
# example

def get_circle_info(radius):
    """Calculates circle area, circumference, and volume"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    volume = (4.0 / 3) * pi * (radius ** 3)
    return area, circumference, volume


print("Circle calculations:")
radius = 5
area, circumference, volume = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print(f"Volume: {volume:.2f}")
print()


def convert_currency(value, currency):
    rate = 33.0
    if currency == "USD":
        print(f"{value} THB = {(value / rate):.2f} USD")
    elif currency == "THB":
        print(f"{value} USD = {(value * rate):.2f} THB")


convert_currency(100, "USD")
convert_currency(100, "THB")
