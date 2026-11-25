
"""
Python Arithmetic, Comparison, Logical, and Membership Operators
Beginner-friendly examples.
"""

import math


# ============================================================
# 1. INTEGER ARITHMETIC OPERATIONS
# ============================================================

print("\n===== INTEGER ARITHMETIC =====")

print("Addition:", 1 + 2)
print("Subtraction:", 2 - 1)
print("Multiplication:", 2 * 3)

# Normal division always returns a floating-point number.
print("Division:", 4 / 2)
print("Division:", 6 / 2)
print("Division:", 7 / 2)

# Floor division removes the fractional part.
print("Floor division:", 7 // 2)
print("Modulus (remainder):", 3 % 2)
print("Floor division:", 7 // 3)

# Exponentiation means raising a number to a power.
print("Exponentiation:", 3 ** 2)


# ============================================================
# 2. FLOATING-POINT NUMBERS
# ============================================================

print("\n===== FLOATING-POINT NUMBERS =====")

pi_approximation = 3.14
gravity = 9.81

print("Approximate value of PI:", pi_approximation)
print("Acceleration due to gravity:", gravity)


# ============================================================
# 3. COMPLEX NUMBERS
# ============================================================

print("\n===== COMPLEX NUMBERS =====")

complex_number = 1 + 1j
another_complex_number = 1 - 1j

print("Complex number:", complex_number)
print(
    "Multiplication of complex numbers:",
    complex_number * another_complex_number
)


# ============================================================
# 4. ARITHMETIC USING VARIABLES
# ============================================================

print("\n===== ARITHMETIC USING VARIABLES =====")

a = 3
b = 2

total = a + b
difference = a - b
product = a * b
division = a / b
remainder = a % b
floor_division = a // b
exponentiation = a ** b

print("a =", a)
print("b =", b)
print("a + b =", total)
print("a - b =", difference)
print("a * b =", product)
print("a / b =", division)
print("a % b =", remainder)
print("a // b =", floor_division)
print("a ** b =", exponentiation)

# Avoid using sum as a variable name because sum() is a
# built-in Python function.


# ============================================================
# 5. ARITHMETIC USING TWO NUMBERS
# ============================================================

print("\n===== OPERATIONS WITH TWO NUMBERS =====")

num_one = 3
num_two = 4

total = num_one + num_two
difference = num_two - num_one
product = num_one * num_two
division = num_two / num_one
remainder = num_two % num_one

print("First number:", num_one)
print("Second number:", num_two)
print("Total:", total)
print("Difference:", difference)
print("Product:", product)
print("Division:", division)
print("Remainder:", remainder)


# ============================================================
# 6. AREA OF A CIRCLE
# ============================================================

print("\n===== AREA OF A CIRCLE =====")

radius = 10

# Formula: Area = PI * radius squared
area_of_circle = math.pi * radius ** 2

print("Radius:", radius)
print("Area of circle:", area_of_circle)


# ============================================================
# 7. AREA OF A RECTANGLE
# ============================================================

print("\n===== AREA OF A RECTANGLE =====")

length = 10
width = 20

# Formula: Area = length * width
area_of_rectangle = length * width

print("Length:", length)
print("Width:", width)
print("Area of rectangle:", area_of_rectangle)


# ============================================================
# 8. WEIGHT OF AN OBJECT
# ============================================================

print("\n===== WEIGHT OF AN OBJECT =====")

mass = 75  # Mass in kilograms
gravity = 9.81  # Acceleration in m/s²

# Formula: Weight = mass * gravity
weight = mass * gravity

print("Mass:", mass, "kg")
print("Gravity:", gravity, "m/s²")
print("Weight:", weight, "N")


# ============================================================
# 9. COMPARISON OPERATORS
# ============================================================

print("\n===== COMPARISON OPERATORS =====")

print("3 > 2:", 3 > 2)
print("3 >= 2:", 3 >= 2)
print("3 < 2:", 3 < 2)
print("2 < 3:", 2 < 3)
print("2 <= 3:", 2 <= 3)
print("3 == 2:", 3 == 2)
print("3 != 2:", 3 != 2)


# ============================================================
# 10. COMPARING STRING LENGTHS
# ============================================================

print("\n===== STRING LENGTH COMPARISONS =====")

print("mango == avocado:", len("mango") == len("avocado"))
print("mango != avocado:", len("mango") != len("avocado"))
print("mango < avocado:", len("mango") < len("avocado"))

print("milk != meat:", len("milk") != len("meat"))
print("milk == meat:", len("milk") == len("meat"))

print("tomato == potato:", len("tomato") == len("potato"))
print("python > dragon:", len("python") > len("dragon"))


# ============================================================
# 11. BOOLEAN COMPARISONS
# ============================================================

print("\n===== BOOLEAN COMPARISONS =====")

print("True == True:", True == True)
print("True == False:", True == False)
print("False == False:", False == False)

print("True and True:", True and True)
print("True or False:", True or False)


# ============================================================
# 12. IDENTITY OPERATORS
# ============================================================

print("\n===== IDENTITY OPERATORS =====")

# 'is' checks whether two references point to the same object.
# 'is not' checks whether they point to different objects.
# Use == when you want to compare values.

print("1 == 1:", 1 == 1)
print("1 != 2:", 1 != 2)

# For integer values, use == for numerical comparisons.
print("4 == 2 ** 2:", 4 == 2 ** 2)


# ============================================================
# 13. MEMBERSHIP OPERATORS
# ============================================================

print("\n===== MEMBERSHIP OPERATORS =====")

print("'A' in 'Asabeneh':", "A" in "Asabeneh")
print("'B' in 'Asabeneh':", "B" in "Asabeneh")

print("'coding' in 'coding for all':", "coding" in "coding for all")
print("'a' in 'an':", "a" in "an")


# ============================================================
# 14. LOGICAL OPERATORS
# ============================================================

print("\n===== LOGICAL OPERATORS =====")

# AND: Both conditions must be True.
print("3 > 2 and 4 > 3:", 3 > 2 and 4 > 3)
print("3 > 2 and 4 < 3:", 3 > 2 and 4 < 3)
print("3 < 2 and 4 < 3:", 3 < 2 and 4 < 3)

# OR: At least one condition must be True.
print("3 > 2 or 4 > 3:", 3 > 2 or 4 > 3)
print("3 > 2 or 4 < 3:", 3 > 2 or 4 < 3)
print("3 < 2 or 4 < 3:", 3 < 2 or 4 < 3)

# NOT: Reverses a Boolean value.
print("not (3 > 2):", not (3 > 2))
print("not True:", not True)
print("not False:", not False)
print("not not True:", not not True)
print("not not False:", not not False)


# ============================================================
# END OF PYTHON OPERATIONS LESSON
# ============================================================

print("\n===== END OF LESSON =====")
