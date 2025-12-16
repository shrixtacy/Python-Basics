# How Python Works 🔧

Understand what happens behind the scenes when you run a Python program.

**Quick Links**: [Main README](README.md) | [Getting Started](README-GettingStarted.md) | [Basics](README-Basics.md) | [History](README-History.md)

---

## Table of Contents

1. [Python Execution Model](#python-execution-model)
2. [Interpreted vs Compiled](#interpreted-vs-compiled)
3. [The Python Interpreter](#the-python-interpreter)
4. [Bytecode & Virtual Machine](#bytecode--virtual-machine)
5. [Memory Management](#memory-management)
6. [Scope & Namespaces](#scope--namespaces)
7. [Performance Tips](#performance-tips)

---

## Python Execution Model

### What Happens When You Run Python Code?

When you execute a Python script, several steps happen automatically:

```
1. SOURCE CODE (.py file)
       ↓
2. PARSER (Syntax check)
       ↓
3. COMPILER (Create bytecode)
       ↓
4. BYTECODE (.pyc file)
       ↓
5. VIRTUAL MACHINE (Execute)
       ↓
6. RESULT (Output)
```

Let's explore each step!

---

## Interpreted vs Compiled

### The Confusion

Many people think Python is "interpreted" because you don't compile it like C++. But it's not that simple!

### Traditional Compiled Languages (C, C++)

```
SOURCE CODE → COMPILER → BINARY (Machine Code) → RUN → OUTPUT
```

- Fast execution (binary is machine code)
- Compilation step required before running
- Binary is specific to your operating system

### Traditional Interpreted Languages (JavaScript, Bash)

```
SOURCE CODE → INTERPRETER → Direct Execution → OUTPUT
```

- Slower (must interpret each line)
- No compilation step
- Easier to run on different systems

### Python (Hybrid Approach)

```
SOURCE CODE → COMPILER → BYTECODE → VIRTUAL MACHINE → OUTPUT
```

- Best of both worlds!
- Code is compiled to bytecode (like compiled languages)
- Bytecode runs on a virtual machine (like interpreted languages)
- This is called **bytecode compilation**

---

## The Python Interpreter

### What is the Python Interpreter?

The **Python interpreter** is a program (written mostly in C) that reads and executes Python code. When you run `python script.py`, you're actually running the interpreter!

### Interactive Mode

```bash
$ python
Python 3.9.7 (default, Sep 10 2021, 14:59:47)
>>>
```

In interactive mode:
- Python processes one line at a time
- Results are printed immediately
- Perfect for learning and testing

### Script Mode

```bash
$ python myscript.py
```

In script mode:
- Python reads the entire file
- Executes the whole thing
- Output only when `print()` is called

### What the Interpreter Does

```python
# myscript.py
x = 5
y = 10
print(x + y)
```

Step by step:

1. **Parse**: Check syntax is correct
2. **Compile**: Create bytecode
3. **Execute**: Run each instruction
4. **Output**: Print "15"

---

## Bytecode & Virtual Machine

### What is Bytecode?

**Bytecode** is an intermediate representation of your Python code. It's not Python code anymore, but it's not machine code either.

### Seeing Bytecode

You can see bytecode using the `dis` module:

```python
import dis

def add(a, b):
    return a + b

dis.dis(add)
```

Output:
```
  2           0 LOAD_FAST                0 (a)
              2 LOAD_FAST                1 (b)
              4 BINARY_ADD
              6 RETURN_VALUE
```

This shows:
- Load variable `a` onto the stack
- Load variable `b` onto the stack
- Add them
- Return the result

### The Python Virtual Machine (PVM)

The **Python Virtual Machine** is a software interpreter that executes bytecode.

```
Bytecode → PVM → Execution
```

Think of it like a computer within your computer!

#### Example Flow

```python
x = 5
y = 3
z = x + y
```

Bytecode:
```
1. LOAD_CONST 5         → Load 5
2. STORE_FAST 'x'       → Store in x
3. LOAD_CONST 3         → Load 3
4. STORE_FAST 'y'       → Store in y
5. LOAD_FAST 'x'        → Load x (5)
6. LOAD_FAST 'y'        → Load y (3)
7. BINARY_ADD           → Add them (8)
8. STORE_FAST 'z'       → Store in z
```

### .pyc Files

When you import a module, Python stores compiled bytecode in `.pyc` files:

```
mymodule.py → Compiled to → __pycache__/mymodule.cpython-39.pyc
```

Next time you import, Python loads the `.pyc` file directly (faster!).

---

## Memory Management

### Variables in Memory

When you create a variable, Python does several things:

```python
x = 42
```

What happens:
1. Python creates an integer object with value 42
2. Python creates a variable name `x`
3. Python links `x` to the object
4. The object is stored in memory

### Reference Counting

Python uses **reference counting** to manage memory:

```python
x = 42          # Object created, reference count = 1
y = x           # Object now has 2 references
z = x           # Object now has 3 references
del x           # Reference count = 2
del y           # Reference count = 1
del z           # Reference count = 0 → Object deleted
```

When reference count reaches 0, Python automatically deletes the object.

### Everything is an Object

In Python, everything is an object with a type and value:

```python
x = 5
print(type(x))          # <class 'int'>
print(id(x))            # Memory address
print(isinstance(x, int))  # True
```

### Memory Layout Example

```python
name = "Alice"
age = 25
```

Memory visualization:
```
Address 0x101: String Object "Alice" (size: ~50 bytes)
Address 0x201: Integer Object 25 (size: ~28 bytes)

Symbol Table:
  'name' → points to 0x101
  'age'  → points to 0x201
```

### Garbage Collection

Python's **garbage collector** automatically removes unused objects:

```python
def create_list():
    my_list = [1, 2, 3]      # Created
    return my_list.pop()      # Returns 3

result = create_list()
# my_list is no longer needed → Garbage collected automatically
```

---

## Scope & Namespaces

### What is Scope?

**Scope** determines where a variable is accessible.

### Namespace

A **namespace** is a mapping from variable names to objects.

### Types of Scope (LEGB Rule)

Python searches for variables in this order:

1. **L**ocal - Inside the current function
2. **E**nclosing - Inside enclosing functions
3. **G**lobal - At the module level
4. **B**uilt-in - Python's built-in namespace

```python
x = "global"

def outer():
    x = "enclosing"
    
    def inner():
        x = "local"
        print(x)        # "local"
    
    inner()
    print(x)            # "enclosing"

print(x)                # "global"
```

### Global Scope

```python
x = 10  # Global scope

def function():
    x = 20  # Local scope (doesn't affect global x)
    print(x)

function()      # 20
print(x)        # 10 (global x unchanged)
```

### Modifying Global Variables

```python
count = 0

def increment():
    global count        # Declare we're using global count
    count += 1

increment()
print(count)            # 1
```

### Local Variables

```python
def function():
    local_var = 42      # Only exists inside this function
    print(local_var)

function()
print(local_var)        # NameError: undefined
```

---

## Performance Tips

### 1. **Use Built-in Functions**

Built-in functions are implemented in C, making them faster:

```python
# SLOW - Manual loop
total = 0
for i in range(1000000):
    total += i

# FAST - Built-in function
total = sum(range(1000000))
```

### 2. **List Comprehensions are Faster**

```python
# SLOW
squares = []
for i in range(1000):
    squares.append(i**2)

# FAST - List comprehension
squares = [i**2 for i in range(1000)]
```

### 3. **Avoid Global Variables**

Local variables are faster to access:

```python
# SLOW
count = 0
def increment():
    global count
    count += 1

# FAST
def increment(count):
    return count + 1
```

### 4. **Use `str.join()` for String Concatenation**

```python
# SLOW - Creates new string each time
text = ""
for word in words:
    text += word

# FAST - More efficient
text = "".join(words)
```

### 5. **Avoid Repeated Function Calls**

```python
# SLOW - len() called many times
for i in range(len(my_list)):
    print(my_list[i])

# FAST - len() called once
length = len(my_list)
for i in range(length):
    print(my_list[i])

# EVEN BETTER - Direct iteration
for item in my_list:
    print(item)
```

### 6. **Import Only What You Need**

```python
# SLOW
import math
result = math.sqrt(16)

# Slightly faster
from math import sqrt
result = sqrt(16)
```

---

## Understanding Error Messages

### Anatomy of an Error

```python
>>> x = 10
>>> y = "hello"
>>> z = x + y
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
```

Breaking it down:
- **Line** - Where the error occurred
- **Error Type** - `TypeError` (type-related problem)
- **Message** - Specific description of what went wrong

### Common Errors

| Error | Meaning | Fix |
|-------|---------|-----|
| `SyntaxError` | Incorrect Python syntax | Check spelling and indentation |
| `NameError` | Variable doesn't exist | Define the variable first |
| `TypeError` | Wrong data type | Check variable types |
| `IndexError` | List index out of range | Check list length |
| `KeyError` | Dictionary key doesn't exist | Check key spelling |
| `ValueError` | Wrong value for operation | Check input data |

---

## Debugging Techniques

### 1. **Print Debugging**

```python
def calculate(x):
    print(f"Input: {x}")
    result = x * 2
    print(f"Result: {result}")
    return result
```

### 2. **Using `type()` and `id()`**

```python
x = 42
print(type(x))      # What type is it?
print(id(x))        # Where is it in memory?
```

### 3. **The `pdb` Debugger**

```python
import pdb

def calculate(x):
    pdb.set_trace()         # Execution pauses here
    result = x * 2
    return result
```

Then use commands:
- `n` - Next line
- `s` - Step into
- `c` - Continue
- `p variable` - Print variable

---

## Summary: How Python Works

```
1. You run: python script.py
2. Python reads the file
3. Parser checks syntax
4. Compiler creates bytecode
5. Virtual machine executes bytecode
6. Results are displayed
```

Key concepts:
- **Bytecode**: Intermediate representation
- **Virtual Machine**: Executes bytecode
- **Reference Counting**: Memory management
- **Scope**: Determines variable accessibility
- **Namespaces**: Maps names to objects

---

## Next Steps

You now understand how Python works internally! Time to explore:

- **Look at the code examples** in this repository
- **Create your own programs** using the concepts from README-Basics.md
- **Use a debugger** when things don't work as expected

---

## Resources

- **Python Documentation**: [docs.python.org](https://docs.python.org/)
- **Python Tutor**: [pythontutor.com](https://pythontutor.com/) - Visualize execution
- **`dis` Module**: `python -m dis scriptname.py`
- **`pdb` Documentation**: [docs.python.org/3/library/pdb.html](https://docs.python.org/3/library/pdb.html)

---

**Back to**: [Main README](README.md)
