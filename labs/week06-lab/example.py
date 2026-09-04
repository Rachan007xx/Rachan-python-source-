# Part 1
# example
def say_hello():
    """Prints a simple hello message"""
    print("Hello, World!")
    print("Welcome to Python functions!")

print("Calling say_hello():")
say_hello()
print()


# Part 2
# example1
def greet_person(name):
    """Greets a person by name"""
    print(f"Hello, {name}! Nice to meet you.")

print("Calling greet_person with different names:")
greet_person("Alice")
greet_person("Bob")
greet_person("Charlie")
print()


# example3
def calculate_rectangle_area(length, width):
    """Calculates and displays rectangle area"""
    area = length * width
    print(f"Rectangle with length {length} and width {width}")
    print(f"Area = {length} × {width} = {area}")
    print()

print("Calculating rectangle areas:")
calculate_rectangle_area(5, 3)
calculate_rectangle_area(10, 7)


# Part 3
# example1
def add_numbers(a, b):
    """Adds two numbers and returns the result"""
    return a + b

print("Using functions that return values:")
sum1 = add_numbers(5, 3)
sum2 = add_numbers(10, 7)
print(f"5 + 3 = {sum1}")
print(f"10 + 7 = {sum2}")
print(f"Sum of both results: {sum1 + sum2}")
print()


# example2
def get_circle_info(radius):
    """Calculates circle area and circumference"""
    pi = 3.14159
    area = pi * radius * radius
    circumference = 2 * pi * radius
    return area, circumference

print("Circle calculations:")
radius = 5
area, circumference = get_circle_info(radius)
print(f"Circle with radius {radius}:")
print(f"Area: {area:.2f}")
print(f"Circumference: {circumference:.2f}")
print()


# Part 4
# example1
def greet_with_title(name, title="Mr./Ms."):
    """Greets with a title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")
greet_with_title("Johnson", "Dr.")
greet_with_title("Brown", "Prof.")
print()


# example2
def show_profile(name, age, country="Unknown"):
    """Displays a profile with default country"""
    print(f"Profile: {name}, Age: {age}, Country: {country}")

print("Multiple default parameters:")
show_profile("Alice", 18)
show_profile("Bob", 25)
show_profile("Charlie", 30, "USA")
