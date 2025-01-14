# Python Cheat Sheet

## Basics

### Variables and Data Types
```python
# Variable assignment
x = 5       # Integer
y = 3.14    # Float
name = "John"  # String
is_active = True  # Boolean

# Multiple assignment
a, b, c = 1, 2, 3

# Data type conversion
int("10")       # Convert string to integer
float("3.14")   # Convert string to float
str(100)        # Convert integer to string
bool(0)         # Convert to boolean
```

### Comments
```python
# Single-line comment

""" 
Multi-line comment 
"""
```

## Control Structures

### Conditional Statements
```python
if x > 0:
    print("Positive")
elif x == 0:
    print("Zero")
else:
    print("Negative")
```

### Loops
```python
# For loop
for i in range(5):
    print(i)

# While loop
while x > 0:
    print(x)
    x -= 1

# Loop with else
for i in range(3):
    print(i)
else:
    print("Done")

# Break and Continue
for i in range(10):
    if i == 5:
        break
    if i % 2 == 0:
        continue
    print(i)
```

### List Comprehension
```python
squares = [x**2 for x in range(10)]
evens = [x for x in range(10) if x % 2 == 0]
```

## Data Structures

### Lists
```python
fruits = ["apple", "banana", "cherry"]
fruits.append("date")   # Add item
fruits.remove("banana") # Remove item
print(fruits[0])         # Access item

# Sorting with custom comparators
fruits.sort(key=lambda x: len(x))  # Sort by length
fruits.sort(reverse=True)         # Descending order
```

### Dictionaries
```python
person = {"name": "John", "age": 30}
print(person["name"])
person["age"] = 31
person["city"] = "New York"

# Iterating through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")
```

### Tuples
```python
tuple_example = (1, 2, 3)
print(tuple_example[0])

# Unpacking tuples
a, b, c = tuple_example
```

### Sets
```python
set_example = {1, 2, 3}
set_example.add(4)
set_example.remove(2)

# Set operations
set_a = {1, 2, 3}
set_b = {3, 4, 5}
print(set_a | set_b)  # Union
print(set_a & set_b)  # Intersection
print(set_a - set_b)  # Difference
```

## Functions
```python
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))

# Functions with default arguments
def add(a, b=10):
    return a + b

print(add(5))

# Anonymous Functions
square = lambda x: x ** 2
print(square(5))
```

## File Handling
```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

## Object-Oriented Programming

### Classes and Objects
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name}."

p = Person("Alice", 25)
print(p.greet())
```

### Inheritance
```python
class Employee(Person):
    def __init__(self, name, age, job_title):
        super().__init__(name, age)
        self.job_title = job_title

    def work(self):
        return f"{self.name} is working as a {self.job_title}."

emp = Employee("Bob", 30, "Developer")
print(emp.work())
```

## Error Handling
```python
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")
else:
    print("Division successful!")
finally:
    print("Execution finished.")
```

## Advanced Topics

### List Slicing
```python
numbers = [1, 2, 3, 4, 5]
print(numbers[1:4])   # [2, 3, 4]
print(numbers[:3])    # [1, 2, 3]
print(numbers[::2])   # [1, 3, 5]
```

### Lambda Functions
```python
add = lambda x, y: x + y
print(add(3, 5))
```

### Map, Filter, Reduce
```python
from functools import reduce

# Map
numbers = [1, 2, 3, 4]
squared = list(map(lambda x: x**2, numbers))

# Filter
evens = list(filter(lambda x: x % 2 == 0, numbers))

# Reduce
sum_total = reduce(lambda x, y: x + y, numbers)
```

### Generators
```python
def generate_numbers():
    for i in range(5):
        yield i

for num in generate_numbers():
    print(num)
```

### Decorators
```python
def decorator_function(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator_function
def say_hello():
    print("Hello!")

say_hello()
```

## Sorting with Custom Comparators

### Sorting with `key` Argument
The `key` argument in Python's sort functions allows for custom comparison logic when sorting.
```python
# Sorting a list of strings by length
fruits = ["apple", "banana", "kiwi", "cherry"]
fruits.sort(key=len)
print(fruits)  # ['kiwi', 'apple', 'cherry', 'banana']

# Sorting a list of tuples by the second element
pairs = [(1, 3), (4, 1), (2, 2), (5, 0)]
pairs.sort(key=lambda x: x[1])
print(pairs)  # [(5, 0), (4, 1), (2, 2), (1, 3)]
```

### Using `functools.cmp_to_key`
For more complex sorting logic, use `functools.cmp_to_key` to define a comparator function.
```python
from functools import cmp_to_key

# Comparator function
# Sort integers such that even numbers come first

def compare(x, y):
    if x % 2 == 0 and y % 2 != 0:
        return -1
    elif x % 2 != 0 and y % 2 == 0:
        return 1
    else:
        return x - y

numbers = [5, 2, 9, 1, 4, 8]
sorted_numbers = sorted(numbers, key=cmp_to_key(compare))
print(sorted_numbers)  # [2, 4, 8, 1, 5, 9]
```

## Collections Framework

### Counter
```python
from collections import Counter
words = ["apple", "banana", "apple"]
count = Counter(words)
print(count)
```

### defaultdict
```python
from collections import defaultdict
default_dict = defaultdict(int)
default_dict["key"] += 1
print(default_dict["key"])
```

### deque
```python
from collections import deque
dq = deque([1, 2, 3])
dq.append(4)
dq.appendleft(0)
dq.pop()
dq.popleft()
print(dq)
```

### namedtuple
```python
from collections import namedtuple
Point = namedtuple("Point", "x y")
p = Point(10, 20)
print(p.x, p.y)
```

### ChainMap
```python
from collections import ChainMap
dict1 = {"a": 1}
dict2 = {"b": 2}
chain = ChainMap(dict1, dict2)
print(chain["a"], chain["b"])
```


## Strings

### String Basics
```python
# String declaration
text = "Hello, World!"

# String concatenation
message = "Hello" + " " + "World"

# String interpolation
name = "Alice"
print(f"Hello, {name}!")

# String repetition
repeated = "Hi! " * 3

# Accessing characters
first_char = text[0]   # 'H'
last_char = text[-1]   # '!'

# String slicing
substring = text[0:5]  # 'Hello'
```

### String Methods
```python
# String manipulation
upper_text = text.upper()  # 'HELLO, WORLD!'
lower_text = text.lower()  # 'hello, world!'
capitalized = text.capitalize()  # 'Hello, world!'

# Searching and replacing
starts = text.startswith("Hello")  # True
ends = text.endswith("!")          # True
found_index = text.find("World")   # 7
replaced = text.replace("World", "Everyone")  # 'Hello, Everyone!'

# Splitting and joining
words = text.split(" ")  # ['Hello,', 'World!']
joined = "-".join(words)  # 'Hello,-World!'

# Stripping whitespace
trimmed = "  Hello  ".strip()  # 'Hello'

# Checking properties
is_alpha = "abc".isalpha()  # True
is_digit = "123".isdigit()  # True
is_space = " ".isspace()    # True
```

### String Formatting
```python
# Using format()
formatted = "My name is {} and I am {} years old".format("Alice", 30)

# f-strings
name = "Alice"
age = 30
f_string = f"My name is {name} and I am {age} years old"

# Padding and alignment
right_aligned = "{:>10}".format("Hello")  # '     Hello'
left_aligned = "{:<10}".format("Hello")   # 'Hello     '
center_aligned = "{:^10}".format("Hello") # '  Hello   '
```

### Character Operations
```python
# Getting ASCII value
ascii_val = ord('A')  # 65

# Getting character from ASCII value
char = chr(65)        # 'A'

# Checking character properties
is_upper = 'A'.isupper()  # True
is_lower = 'a'.islower()  # True
is_alpha = 'A'.isalpha()  # True
is_digit = '1'.isdigit()  # True
is_alnum = 'A1'.isalnum()  # True
is_space = ' '.isspace()   # True
```
