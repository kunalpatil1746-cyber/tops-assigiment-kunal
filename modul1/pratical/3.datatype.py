# Demonstrating variables and different data types in Python

# Integer
age = 25
print("Age:", age, "Type:", type(age))

# Float
height = 5.9
print("Height:", height, "Type:", type(height))

# String
name = "John"
print("Name:", name, "Type:", type(name))

# Boolean
is_student = True
print("Is Student:", is_student, "Type:", type(is_student))

# List (mutable sequence)
fruits = ["apple", "banana", "cherry"]
print("Fruits:", fruits, "Type:", type(fruits))

# Tuple (immutable sequence)
coordinates = (10.5, 20.3)
print("Coordinates:", coordinates, "Type:", type(coordinates))

# Dictionary (key-value pairs)
student = {
    "name": "John",
    "age": 25,
    "grade": "A"
}
print("Student:", student, "Type:", type(student))

# Set (unique elements)
unique_numbers = {1, 2, 3, 4, 4, 5}
print("Unique Numbers:", unique_numbers, "Type:", type(unique_numbers))

# NoneType
nothing = None
print("Nothing:", nothing, "Type:", type(nothing))