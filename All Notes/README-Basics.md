# Python Basics 🎓

Master the fundamental concepts you need to start programming in Python.

**Quick Links**: [Main README](README.md) | [Getting Started](README-GettingStarted.md) | [History](README-History.md) | [How It Works](README-HowItWorks.md)

---

## Table of Contents

1. [Syntax & Structure](#syntax--structure)
2. [Variables & Data Types](#variables--data-types)
3. [Operators](#operators)
4. [Control Flow](#control-flow)
5. [Functions](#functions)
6. [Collections](#collections)
7. [Comments](#comments)
8. [Best Practices](#best-practices)

---

## Syntax & Structure

### What is Syntax?

**Syntax** is the set of rules that defines how Python code should be written.

### Key Syntax Rules

```python
# Python uses indentation (spaces/tabs) to define code blocks
if x > 5:
    print("x is greater than 5")  # This line is indented
    print("Still in the if block")

print("Outside the if block")  # Back to no indentation
```

### Indentation is Crucial

- **4 spaces** is the Python standard (never mix spaces and tabs)
- Incorrect indentation = `IndentationError`
- Example:

```python
# CORRECT
if True:
    print("Hello")

# WRONG - Will cause an error
if True:
print("Hello")
```

---

## Variables & Data Types

### What is a Variable?

A **variable** is a named storage location that holds a value. Think of it as a labeled box.

```python
name = "Alice"  # Assign "Alice" to the variable 'name'
age = 25        # Assign 25 to the variable 'age'
```

### Naming Variables

Good variable names:
- Start with a letter or underscore (`_`)
- Can contain letters, numbers, and underscores
- Are descriptive and meaningful
- Use lowercase with underscores (snake_case)

```python
# GOOD
user_name = "Bob"
total_price = 99.99
is_valid = True

# AVOID
x = "Bob"           # Too vague
UserName = "Bob"    # Use lowercase
user-name = "Bob"   # Hyphens not allowed
```

### Python's Main Data Types

#### 1. **String** (text)
```python
name = "Python"           # String with double quotes
greeting = 'Hello'        # String with single quotes
message = """Multi
line
string"""                 # Multi-line string
```

#### 2. **Integer** (whole numbers)
```python
age = 25
count = 0
temperature = -10
large_number = 1_000_000  # Underscores for readability
```

#### 3. **Float** (decimal numbers)
```python
price = 19.99
pi = 3.14159
height = 5.9
```

#### 4. **Boolean** (True or False)
```python
is_student = True
is_raining = False
```

#### 5. **List** (ordered collection)
```python
fruits = ["apple", "banana", "cherry"]
numbers = [1, 2, 3, 4, 5]
mixed = [1, "two", 3.0, True]  # Can mix types
```

#### 6. **Tuple** (immutable list)
```python
coordinates = (10, 20)
rgb_color = (255, 128, 0)
```

#### 7. **Dictionary** (key-value pairs)
```python
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
```

#### 8. **Set** (unique values)
```python
unique_numbers = {1, 2, 3, 4, 5}
```

### Type Checking

```python
x = 42
type(x)              # <class 'int'>

name = "Python"
type(name)           # <class 'str'>
```

### Type Conversion

```python
# Convert string to integer
age_str = "25"
age_int = int(age_str)      # 25

# Convert to string
number = 42
text = str(number)          # "42"

# Convert to float
value = float("3.14")       # 3.14
```

---

## Operators

### Arithmetic Operators

```python
a = 10
b = 3

print(a + b)        # 13  (addition)
print(a - b)        # 7   (subtraction)
print(a * b)        # 30  (multiplication)
print(a / b)        # 3.333... (division - returns float)
print(a // b)       # 3   (floor division - returns integer)
print(a % b)        # 1   (modulo - remainder)
print(a ** b)       # 1000 (exponentiation)
```

### Comparison Operators

Return `True` or `False`

```python
x = 5
y = 10

print(x == y)       # False (equal to?)
print(x != y)       # True  (not equal to?)
print(x < y)        # True  (less than?)
print(x > y)        # False (greater than?)
print(x <= y)       # True  (less than or equal?)
print(x >= y)       # False (greater than or equal?)
```

### Logical Operators

```python
age = 25
is_student = True

# AND - both conditions must be True
if age > 18 and is_student:
    print("Can vote and get student discount")

# OR - at least one condition must be True
if age < 12 or age > 65:
    print("Eligible for special pricing")

# NOT - reverses True/False
if not is_student:
    print("Not a student")
```

### Assignment Operators

```python
x = 10

x += 5      # x = x + 5      (x is now 15)
x -= 3      # x = x - 3      (x is now 12)
x *= 2      # x = x * 2      (x is now 24)
x /= 4      # x = x / 4      (x is now 6.0)
```

---

## Control Flow

### If Statements

```python
age = 20

if age >= 18:
    print("You are an adult")
elif age >= 13:
    print("You are a teenager")
else:
    print("You are a child")
```

### Loops - For Loop

```python
# Loop through a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Loop a specific number of times
for i in range(5):
    print(i)        # Prints 0, 1, 2, 3, 4

# Loop with index
for i in range(len(fruits)):
    print(f"{i}: {fruits[i]}")
```

### Loops - While Loop

```python
count = 0
while count < 5:
    print(count)
    count += 1      # Must increase count, or infinite loop!
```

### Break & Continue

```python
# Break - exit loop early
for i in range(10):
    if i == 5:
        break           # Stops loop when i equals 5
    print(i)            # Prints 0, 1, 2, 3, 4

# Continue - skip to next iteration
for i in range(5):
    if i == 2:
        continue        # Skips when i equals 2
    print(i)            # Prints 0, 1, 3, 4
```

---

## Functions

### What is a Function?

A **function** is a reusable block of code that performs a specific task.

### Basic Function

```python
def greet():
    print("Hello!")

greet()             # Call the function
```

### Function with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Alice")      # Output: Hello, Alice!
greet("Bob")        # Output: Hello, Bob!
```

### Function with Return Value

```python
def add(a, b):
    return a + b

result = add(5, 3)
print(result)       # Output: 8
```

### Default Parameters

```python
def greet(name="Guest"):
    print(f"Hello, {name}!")

greet()             # Output: Hello, Guest!
greet("Alice")      # Output: Hello, Alice!
```

### Multiple Return Values

```python
def get_user_info():
    name = "Alice"
    age = 25
    return name, age

name, age = get_user_info()
print(f"{name} is {age} years old")
```

### Documentation

```python
def add(a, b):
    """
    Add two numbers and return the result.
    
    Args:
        a: First number
        b: Second number
    
    Returns:
        The sum of a and b
    """
    return a + b

print(add.__doc__)  # Prints the docstring
```

---

## Collections

### Lists (Ordered, Mutable)

```python
fruits = ["apple", "banana", "cherry"]

# Access items
print(fruits[0])        # "apple" (first item)
print(fruits[-1])       # "cherry" (last item)

# Add items
fruits.append("date")
fruits.insert(1, "blueberry")

# Remove items
fruits.remove("banana")
removed = fruits.pop()  # Remove last item

# Slicing
print(fruits[1:3])      # Items from index 1 to 2
```

### Dictionaries (Key-Value Pairs)

```python
person = {
    "name": "Alice",
    "age": 25,
    "city": "New York"
}

# Access items
print(person["name"])           # "Alice"

# Add or modify
person["age"] = 26
person["email"] = "alice@email.com"

# Check if key exists
if "name" in person:
    print("Name found")

# Get all keys and values
for key, value in person.items():
    print(f"{key}: {value}")
```

### Tuples (Immutable)

```python
coordinates = (10, 20)

print(coordinates[0])   # 10
print(coordinates[1])   # 20

# Unpacking
x, y = coordinates
print(x, y)             # 10 20
```

---

## Comments

### Single-line Comments

```python
# This is a comment
x = 5  # This is also a comment
```

### Multi-line Comments

```python
"""
This is a multi-line comment.
It can span multiple lines.
Often used for docstrings.
"""

'''
This also works as a multi-line comment.
'''
```

### Why Comments Matter

- Help future you understand the code
- Help other developers understand your code
- Explain the "why", not the "what"

```python
# GOOD - Explains why
# Using modulo to check if number is even
if number % 2 == 0:
    print("Even")

# POOR - Obvious from code
# Check if number mod 2 equals 0
if number % 2 == 0:
    print("Even")
```

---

## Best Practices

### 1. **Use Meaningful Names**

```python
# GOOD
user_age = 25
total_price = 99.99

# AVOID
a = 25
tp = 99.99
```

### 2. **Keep Functions Small**

```python
# GOOD - Does one thing
def calculate_tax(price):
    return price * 0.1

# AVOID - Does too much
def do_everything(price):
    tax = price * 0.1
    total = price + tax
    discount = total * 0.05
    # ... lots more code
```

### 3. **DRY (Don't Repeat Yourself)**

```python
# AVOID - Repetition
print("Hello Alice")
print("Hello Bob")
print("Hello Charlie")

# GOOD - Use a function
def greet(name):
    print(f"Hello {name}")

for name in ["Alice", "Bob", "Charlie"]:
    greet(name)
```

### 4. **Handle Errors Gracefully**

```python
try:
    age = int(input("Enter your age: "))
    print(f"You are {age} years old")
except ValueError:
    print("Please enter a valid number")
```

### 5. **Use Constants**

```python
# GOOD - Clear what the number means
TAX_RATE = 0.1
price = 100
tax = price * TAX_RATE

# AVOID - Magic number
tax = price * 0.1
```

---

## Quick Reference Cheat Sheet

| Concept | Example |
|---------|---------|
| Variable | `name = "Alice"` |
| String | `message = "Hello"` |
| Integer | `age = 25` |
| Float | `price = 19.99` |
| Boolean | `is_valid = True` |
| List | `fruits = ["apple", "banana"]` |
| Dictionary | `person = {"name": "Alice"}` |
| If Statement | `if x > 5: print("Big")` |
| For Loop | `for i in range(5): print(i)` |
| While Loop | `while x < 10: x += 1` |
| Function | `def greet(name): print(f"Hi {name}")` |

---

## Next Steps

Now that you understand Python basics, let's see how Python actually works under the hood:

**Next**: [How Python Works - README-HowItWorks.md](README-HowItWorks.md)

---

## Resources

- **Python Documentation**: [docs.python.org](https://docs.python.org/)
- **Python Tutor**: [pythontutor.com](https://pythontutor.com/) - Visualize code execution
- **Interactive Python Shell**: Type `python` in terminal to start interactive mode

---

**Back to**: [Main README](README.md)
