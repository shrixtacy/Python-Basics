# Getting Started with Python 🚀

Welcome! This guide will help you set up your Python environment and get ready to start learning.

**Quick Links**: [Main README](README.md) | [Basics](README-Basics.md) | [How It Works](README-HowItWorks.md) | [History](README-History.md)

---

## Table of Contents

1. [What is Python?](#what-is-python)
2. [Installing Python](#installing-python)
3. [Choosing an Editor](#choosing-an-editor)
4. [Your First Python Program](#your-first-python-program)
5. [Running Python](#running-python)

---

## What is Python?

Python is a **high-level, interpreted programming language** known for its simplicity and readability. It was designed to be easy to learn, making it perfect for beginners.

### Key Characteristics

- **Easy to Read**: Code written in Python looks almost like English
- **Interpreted**: Executes line-by-line without compilation
- **Dynamically Typed**: You don't need to declare variable types upfront
- **General-Purpose**: Used for web development, data science, automation, AI, and more

---

## Installing Python

### Windows

1. Visit [python.org](https://www.python.org/)
2. Click "Downloads" → Select the latest Python version (3.8+)
3. Run the installer
4. **Important**: Check the box "Add Python to PATH" during installation
5. Click "Install Now"
6. Verify installation by opening Command Prompt and typing:
   ```bash
   python --version
   ```

### macOS

1. Visit [python.org](https://www.python.org/)
2. Download the macOS installer
3. Run the installer and follow the prompts
4. Verify installation by opening Terminal and typing:
   ```bash
   python3 --version
   ```

### Linux

Most Linux distributions come with Python pre-installed. Verify with:
```bash
python3 --version
```

If not installed, use your package manager:
```bash
# Ubuntu/Debian
sudo apt-get install python3

# Fedora
sudo dnf install python3
```

---

## Choosing an Editor

You need a text editor or IDE (Integrated Development Environment) to write Python code.

### Recommended Options

#### 1. **VS Code** (Recommended for Beginners)
- Free and lightweight
- Install the "Python" extension by Microsoft
- Great for learning
- Download: [code.visualstudio.com](https://code.visualstudio.com/)

#### 2. **PyCharm Community Edition**
- Specifically designed for Python
- Free community version available
- More features than VS Code
- Download: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)

#### 3. **Thonny**
- Extremely beginner-friendly
- Built-in Python interpreter
- Simple interface
- Download: [thonny.org](https://thonny.org/)

#### 4. **Mu Editor**
- Designed specifically for teaching Python
- Very clean interface
- Download: [codewith.mu](https://codewith.mu/)

**Our Recommendation**: Start with **VS Code** and the Python extension for the best balance of simplicity and features.

---

## Your First Python Program

### Step 1: Create a File

Create a new file called `hello.py` with the following content:

```python
print("Hello, World!")
```

### Step 2: Save the File

Save it with a `.py` extension (e.g., `hello.py`)

### Step 3: Run the Program

**Using Command Line:**
```bash
python hello.py
```

**Using VS Code:**
- Right-click the file and select "Run Python File in Terminal"
- Or press `Ctrl + F5`

**Expected Output:**
```
Hello, World!
```

Congratulations! You just ran your first Python program! 🎉

---

## Understanding the Program

```python
print("Hello, World!")
```

- **`print()`**: A built-in function that displays text on the screen
- **`"Hello, World!"`**: The text to display (inside quotes)
- **`()`**: Parentheses that indicate we're calling a function

---

## Next Steps

Now that you have Python set up, let's continue learning:

1. **Understand Python's History**: Read [README-History.md](README-History.md) to learn about where Python came from
2. **Learn the Basics**: Move to [README-Basics.md](README-Basics.md) to learn fundamental concepts
3. **Explore Examples**: Check out the `.py` files in this repository

---

## Common Issues & Solutions

### Issue: "python: command not found"
**Solution**: Python is not in your PATH. Reinstall Python and make sure to check "Add Python to PATH"

### Issue: "ModuleNotFoundError"
**Solution**: You're trying to use a library that isn't installed. See the specific README for installation instructions.

### Issue: "SyntaxError"
**Solution**: You have a typo in your code. Check the code carefully for spelling mistakes.

---

## Troubleshooting Tips

1. **Read Error Messages Carefully**: They usually tell you exactly what's wrong
2. **Check Spelling**: Python is case-sensitive (e.g., `Print` is different from `print`)
3. **Verify File Extensions**: Make sure your files end in `.py`
4. **Use Proper Indentation**: Python uses indentation (spaces/tabs) to define code blocks

---

## Resources

- **Official Python Documentation**: [docs.python.org](https://docs.python.org/)
- **Python Community**: [python.org/community](https://www.python.org/community/)
- **Stack Overflow**: Ask questions with the `python` tag

---

## Ready to Learn?

Great! Now that you're all set up, continue with:

**Next**: [Python's History - README-History.md](README-History.md)

---

**Back to**: [Main README](README.md)
