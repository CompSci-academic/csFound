# Python Basics

# Comments
# Single-line comment

# Print statement
print("Hello, World!")

# Variables and Data Types
my_variable = 42
my_float = 3.14
my_string = "Hello"
my_boolean = True

# Type Conversion
int_to_str = str(42)
str_to_float = float("3.14")

# Control Flow

# Conditional Statements
if my_variable > 30:
    print("Variable is greater than 30")
elif my_variable == 30:
    print("Variable is equal to 30")
else:
    print("Variable is less than 30")

# Loops
for i in range(5):
    print(i)

# Functions

# Function Definition
def my_function(arg1, arg2):
    return arg1 + arg2

# Function Call
result = my_function(10, 20)

# Lists

# Creating a List
my_list = [1, 2, 3, 4, 5]

# Accessing Elements
element = my_list[2]

# List Methods
my_list.append(6)
my_list.remove(3)
my_list.sort()

# Strings

# Creating a String
my_string = "Hello, World!"

# String Concatenation
new_string = my_string + " Welcome!"

# String Methods
uppercase_string = my_string.upper()
substring = my_string[7:12]

# Dictionaries

# Creating a Dictionary
my_dict = {"key1": "value1", "key2": "value2"}

# Accessing Values
value = my_dict["key1"]

# Dictionary Methods
keys = my_dict.keys()
values = my_dict.values()

# Tuples and Sets

# Creating a Tuple
my_tuple = (1, 2, 3)

# Creating a Set
my_set = {1, 2, 3}

# File Handling

# Open and Read a File
with open("file.txt", "r") as file:
    contents = file.read()

# Write to a File
with open("file.txt", "w") as file:
    file.write("Hello, File!")

# Exception Handling

# Try and Except
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Error: Division by zero")

# Libraries

# Import a Library
import math

# Using Library Functions
sqrt_result = math.sqrt(16)

# Displaying Results
print("Square root of 16:", sqrt_result)