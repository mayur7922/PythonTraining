
# Magic methods in Python, 
# also known as special or dunder (double underscore) methods, are predefined methods that 
# allow you to define how objects of your class behave in various situations. 
# These methods are called automatically by Python 
# when certain operations are performed on objects.

# For example

# 1) __init__(self):

# Called when an object is created. It's used to initialize the object's attributes.
# Example: object = MyClass()

# 2) __str__(self):

# Called by str() and print() to get a human-readable string representation of an object.
# Example: print(object) will call __str__.

# 3) __eq__(self, other):

# Called when using the equality operator (==) to compare two objects.
# Example: object1 == object2

# 4)__add__(self, other):

# Called when using the addition operator (+) between objects.
# Example: object1 + object2