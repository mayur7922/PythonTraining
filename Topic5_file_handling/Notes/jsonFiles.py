# Constraints on Keys and Values
# Keys:

# Must be strings.
# Should be enclosed in double quotes "".
# Are unique within an object (no duplicate keys).
# Values:

# Can be any of the following data types:
# String: "value"
# Number: 42, 3.14
# Boolean: true, false
# Null: null
# Object: { "key": "value" }
# Array: [1, 2, 3]


# Example of a valid JSON:

# {
#   "name": "Alice",
#   "age": 25,
#   "isStudent": false,
#   "address": {
#     "city": "New York",
#     "zip": "10001"
#   },
#   "hobbies": ["reading", "cycling"]
# }

# Serialization : Converting JSON data into python objects
# Deserialization : Converting python objects into JSON string

# To handle JSON data in Python, you can use the json module. 
# This module allows you to convert Python objects into JSON format and vice versa.

# can i operate directly with the JSON format in python without conversion

# No, you cannot directly operate with JSON format (i.e., as a string) in Python 
# without converting it into Python objects. 
# JSON is a text-based format, 
# while Python works with native data types like dictionaries, lists, etc. 
# To manipulate the data, you need to convert the JSON data into a Python object 
# (like a dictionary or list) 
# and then manipulate it. 
# After manipulating, you can convert it back to JSON format.

# Why you need conversion:
# JSON is a data interchange format, 
# designed to be a language-independent way of representing data.
# Python operates with native data structures l
# ike dictionaries, lists, and others,
#  which are more efficient for manipulating and processing data.

# Steps for conversion:

# JSON to Python object: Use json.loads() or json.load() to convert JSON string to a Python object.

# Python object to JSON: Use json.dumps() or json.dump() to convert a Python object to JSON string.



# 1. json.loads()
# Input: Takes a JSON string as input.
# Usage: Used to parse a JSON string into a Python object.

# Example:

# import json

# json_string = '{"name": "Alice", "age": 25}'
# python_obj = json.loads(json_string)
# print(python_obj)  
# Output: {'name': 'Alice', 'age': 25}

# 2. json.load()
# Input: Takes a file object (file handle) as input.
# Usage: Used to parse JSON data from a file and convert it into a Python object.

# Example:

# import json

# with open('data.json', 'r') as file:
#     python_obj = json.load(file)
# print(python_obj)  
# # Output will depend on the content of 'data.json'

# 1. json.dumps()
# Input: Takes a Python object as input (e.g., dictionary, list).
# Output: Returns a JSON string.
# Usage: Used when you want to convert a Python object into a JSON-formatted string.

# 2. json.dump()
# Input: Takes a Python object and a file object (e.g., a file handle) as input.
# Output: Writes the JSON data directly to the file.
# Usage: Used when you want to write a Python object to a file in JSON format.