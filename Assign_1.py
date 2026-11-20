# 1. Integer
a = 10
print("Integer:", a)
print("Type:", type(a))
print("Square:", a ** 2)
# Integer: 10
# Type: <class 'int'>
# Square: 100

# 2. Float
b = 10.5
print("\nFloat:", b)
print("Type:", type(b))
print("Rounded value:", round(b))
# Float: 10.5
# Type: <class 'float'>
# Rounded value: 10

# 3. Complex
c = 3 + 4j
print("\nComplex:", c)
print("Type:", type(c))
print("Real part:", c.real)
print("Imaginary part:", c.imag)
# Complex: (3+4j)
# Type: <class 'complex'>
# Real part: 3.0
# Imaginary part: 4.0

# 4. String
name = "Python"
print("\nString:", name)
print("Type:", type(name))
print("Length:", len(name))
print("Uppercase:", name.upper())
# String: Python
# Type: <class 'str'>
# Length: 6
# Uppercase: PYTHON

# 5. List
my_list = [10, 20, 30, 40]
print("\nList:", my_list)
print("Type:", type(my_list))
print("Length:", len(my_list))
my_list.append(50)
print("After append:", my_list)
# List: [10, 20, 30, 40]
# Type: <class 'list'>
# Length: 4
# After append: [10, 20, 30, 40, 50]

# 6. Tuple
my_tuple = (10, 20, 30)
print("\nTuple:", my_tuple)
print("Type:", type(my_tuple))
print("Length:", len(my_tuple))
# Tuple: (10, 20, 30)
# Type: <class 'tuple'>
# Length: 3

# 7. Dictionary
my_dict = {"Name": "Pranita", "Age": 18}
print("\nDictionary:", my_dict)
print("Type:", type(my_dict))
print("Keys:", my_dict.keys())
print("Values:", my_dict.values())
# Dictionary: {'Name': 'Pranita', 'Age': 18}
# Type: <class 'dict'>
# Keys: dict_keys(['Name', 'Age'])
# Values: dict_values(['Pranita', 18])

# 8. Set
my_set = {10, 20, 30, 30}
print("\nSet:", my_set)
print("Type:", type(my_set))
print("Length:", len(my_set))
# Set: {10, 20, 30}
# Type: <class 'set'>
# Length: 3

# 9. Frozenset
my_frozenset = frozenset([10, 20, 30])
print("\nFrozenset:", my_frozenset)
print("Type:", type(my_frozenset))
# Frozenset: frozenset({10, 20, 30})
# Type: <class 'frozenset'>

# 10. Boolean
x = True
print("\nBoolean:", x)
print("Type:", type(x))
# Boolean: True
# Type: <class 'bool'>

# 11. NoneType
y = None
print("\nNoneType:", y)
print("Type:", type(y))
# NoneType: None
# Type: <class 'NoneType'>

# Built-in Functions
numbers = [10, 20, 30, 40, 50]
print("\n--- Built-in Functions ---")
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
print("Sum:", sum(numbers))
print("Length:", len(numbers))
# --- Built-in Functions ---
# Maximum: 50
# Minimum: 10
# Sum: 150
# Length: 5

import math

# Math Functions
print("\n--- Math Functions ---")
print("Square root of 25:", math.sqrt(25))
print("Power of 2^3:", math.pow(2, 3))
print("Factorial of 5:", math.factorial(5))
print("Ceiling of 4.3:", math.ceil(4.3))
print("Floor of 4.8:", math.floor(4.8))
# --- Math Functions ---
# Square root of 25: 5.0
# Power of 2^3: 8.0
# Factorial of 5: 120
# Ceiling of 4.3: 5
# Floor of 4.8: 4
