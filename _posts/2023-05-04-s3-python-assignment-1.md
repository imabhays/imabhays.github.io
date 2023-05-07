---
layout: single
classes: wide
title: "Semester 3 - Python - Assignment 1"
excerpt: "Sem 3 - Python Assignment 1"
sidebar:
    nav: "s3python"
header:
  teaser: /assets/images/bca/s3-python-assignment-1.jpg
toc: false
toc_sticky: true
toc_label: "Your Custom Label"
toc_icon: "icon-class-name"
categories: bca
tags:
  - python
  - pythin basics
  - python essentials
  - bca
  - netacad
  - pcap
---

Q1. For any Programming Language requires some basic concepts, Briefly explain the following concepts\
I. Data Type\
II. Data Structures\
III. Variables\
IV. Flow Control Structures
{: .notice}

### Data Types
- Refers to the type of data a variable can store in a program.
- Examples of common data types:
    - Integer (e.g. 5, -10)
    - Float (e.g. 3.14, 0.01)
    - Boolean (true or false)
    - String (e.g. "hello", "goodbye")

### Data Structures
- A way of organizing and storing data in a program.
- Examples of data structures:
    - Arrays (ordered collection)
    - Linked Lists (linear collection)
    - Stacks (Last-In-First-Out collection)
    - Queues (First-In-First-Out collection)
    - Trees (hierarchical collection)

### Variables
- Named storage locations for holding data in a program.
- Variables must be declared with a specific data type.
- The value stored in a variable can be changed during the program execution.

### Flow Control Structures
- Control the flow of execution of a program.
- Examples of flow control structures:
    - If-Else (decision-making structure)
    - Loops (For, While)
    - Switch-Case (multiple-choice decision-making structure)

Q2. Difference between Compiler and Interpreter
{: .notice}

### Difference
- **Compiler**: converts the entire source code into machine code before the program is executed (e.g. C++, C#, Java).
- **Interpreter**: interprets the source code line by line and executes it immediately (e.g. Python, Ruby, JavaScript).
- **Example**: Python uses an interpreter to execute the code, allowing for interactive and dynamic programming.

Q3. Python is a simple programming language ,Explain the following 
a. Python Programming Language applications 
b. Benefits of Python Language over Other Programming Languages 
{: .notice}

### Python Programming Language Applications:
- Web development with frameworks such as Django and Flask
- Scientific computing, data analysis, and visualization with libraries like NumPy, Pandas, and Matplotlib
- Artificial intelligence and machine learning with libraries such as TensorFlow, Keras, and PyTorch
- Game development, especially for creating simple logic or educational games
- Automation for tasks like web scraping, data processing, and file management

### Benefits of Python Language over Other Programming Languages:
- Simple and readable syntax
- Large and active community with plenty of online resources
- Cross-platform compatibility with multiple operating systems
- Versatility for a wide range of applications
- Large number of libraries for complex tasks with minimal code
- Dynamically typed for flexible and rapid development


Q4. Python consist of different operators, Explain 
I. Arithmetic operators on Python 
II. Numerical Operators in Python 
{: .notice}

## *Python Operators:*
### Arithmetic Operators:
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Floor Division (//)
- Modulus/Remainder (%)
- Exponent (**)

### Numerical Operators:
- Comparison operators: Less than (<), Less than or equal to (<=), Greater than (>), Greater than or equal to (>=), Equal to (==), Not equal to (!=)
- Logical operators: And (and), Or (or), Not (not)
- Bitwise operators: And (`&`), Or (`|`), Xor (`^`), Not (`~`), Left shift (`<<`), Right shift (`>>`)

These operators can be used for mathematical operations on numeric data types and comparisons of Boolean values in Python.\
For example:

```
2 + 3        # 5
4 - 2        # 2
3 * 4        # 12
5 / 2        # 2.5
5 // 2       # 2
5 % 2        # 1
2 ** 3       # 8
2 < 3        # True
3 >= 3       # True
2 == 3       # False
2 != 3       # True
(2 < 3) and (3 > 2)   # True
(2 < 3) or (3 < 2)    # True
not (2 < 3)           # False
```

Q5. Explain the different conditional Operators in Python ? 
{: .notice}

## Conditional Operators in Python
- Used to control program flow based on conditions
- Types of conditional operators include:
    - If-Else: performs an action based on a True or False condition
    - If-Elif-Else: checks multiple conditions and performs one action based on the first True condition
    - Nested If: checks multiple conditions inside another if statement
    - Ternary Operator: assigns a value to a variable based on a condition
- Condition can be any expression that evaluates to a Boolean value (True or False)

### If-Else
```
if condition:
    # code if True
else:
    # code if False
```

### If-Elif-Else
```
if condition1:
    # code if condition1 True
elif condition2:
    # code if condition1 False and condition2 True
else:
    # code if condition1 and condition2 False
```

### Nested If
```
if condition1:
    # code if condition1 True
    if condition2:
        # code if condition1 and condition2 True
    else:
        # code if condition1 True and condition2 False
else:
    # code if condition1 False
```

### Ternary Operator
```
value = expression1 if condition else expression2
```

Q6. Difference Between Logical and Bitwise Operator ?
{: .notice}

## Logical and Bitwise Operators in Python
- Used to perform operations on binary data
- Logical operators (and, or, not) operate based on truth values of operands and return Boolean values
- Bitwise operators: And (`&`), Or (`|`), Xor (`^`), Not (`~`), Left shift (`<<`), Right shift (`>>`)
- Examples:

```
# Logical operators
x = True
y = False
print(x and y)  # False
print(x or y)   # True
print(not x)    # False

# Bitwise operators
x = 5 # binary representation: 0000 0101
y = 3 # binary representation: 0000 0011
print(x & y)    # 1
print(x | y)    # 7
print(x ^ y)    # 6
print(~x)       # -6
print(x << 2)   # 20
print(x >> 2)   # 1
```
In summary, logical operators operate based on truth values of operands and return Boolean values, while bitwise operators operate on binary representations of operands.
