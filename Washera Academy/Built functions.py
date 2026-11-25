# int(), abs(), str(), sum(), min(), max(), type(), bool(), range(), id(), len(), round(), input(), print(), dir() and help() functions

print("Integer value:", int(3.14))   # int() function converts float to integer

print("Absolute value:", abs(-10))    # abs() function returns the absolute value of a number

print("String value:", str(10))     # str() function converts integer to string

print("Sum:", sum([1, 2, 3]))   # sum() function returns the sum of all items in an iterable

print("Minimum:", min(1, 2, 3))   # min() function returns the smallest item in an iterable

print("Maximum:", max(1, 2, 3))   # max() function returns the largest item in an iterable

print("Type:", type(10))   # type() function returns the type of an object

print("Boolean:", bool(1))   # bool() function returns True if the value is true, otherwise False

print("Range:", list(range(5)))   # range() function returns a sequence of numbers

print("ID:", id(10))   # id() function returns the identity of an object
print("Length:", len("Hello World!"))   # len() function returns the length of an object

print("Rounded:", round(3.14))   # round() function rounds a float number to the nearest integer

x = input("Enter a number: ")   # input() function takes user input
print("User Input:", x)   # print() function prints the specified message to the console

print("Message:", "Hello World!")   # print() function prints the specified message to the console

y = input("Enter what you want help with (e.g., int, str, bool, etc.): ")   # input() function takes user input
print("Help:", help(y))   # help() function displays the documentation of an object

print("Directory:", dir())   # dir() function returns a list of valid attributes of the object