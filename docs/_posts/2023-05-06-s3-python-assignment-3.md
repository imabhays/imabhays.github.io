---
layout: single
classes: wide
title: "Semester 3 - Python - Assignment 3"
excerpt: "Sem 3 - Python Assignment 3"
sidebar:
    nav: "s3python"
header:
  teaser: /assets/images/bca/s3-python-assignment-3.jpg
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

# ASSIGNMENT III

1. Consider the following function:

    ```
    def square(num):
        num_squared = num ** 2
        return num_squared
    ```

    Which line of codes is the function’s signature?
    
    Answer: `def square(num):`


2. What is the output of the following function call?

    ```
    def fun1(name, age=20):
        print(name, age)
    
    fun1('Emma', 25)
    ```

    Answer: `Emma 25`
    
3. What is the output of the following `display_person()` function call?

    ```
    def display_person(*args):
        for i in args:
            print(i)

    display_person(name="Emma", age="25")
    ```
    
    Answer: `TypeError: display_person() got an unexpected keyword argument 'name'`
    
4. What is the output of the `add()` function call?

    ```
    def add(a, b):
        return a+5, b+5
    
    result = add(3, 2)
    print(result)
    ```

    Answer: `(8, 7)`
    
5. Select which is true for Python function:

    - A Python function can return only a single value
    - A function can take an unlimited number of arguments
    - A Python function can return multiple values
    - Python function doesn’t return anything unless and until you add a return statement

    Answer:
    
    - A function can take an unlimited number of arguments
    - A Python function can return multiple values
  
    
6. Write a program to create a function that takes two arguments, name and age, and print their value.

    ```
    def print_name_and_age(name, age):
        print("Name:", name)
        print("Age:", age)
        
    # Call the function
    print_name_and_age("John", 30)
    ```
    
7. Write a program to create function `func1()` to accept a variable length of arguments and print their value.

    ```
    def func1(*args):
        for arg in args:
            print(arg)
    ```
    
8. Write a program to create function `calculation()` such that it can accept two variables and calculate addition and subtraction. Also, it must return both addition and subtraction in a single return call.

    ```
    def calculation(num1, num2):
        add = num1 + num2
        sub = num1 - num2
        return add, sub
    
    # Call the function
    result = calculation(10, 5)
    print(result)
    ```
    
9. Write a program to create a recursive function to calculate the sum of numbers from 0 to 10.

    ```
    def recursive_sum(n):
        if n == 0:
            return 0
        else:
            return n + recursive_sum(n-1)

    # Call the recursive_sum function with argument 10 and print the result
    result = recursive_sum(10)
    print(result)
    ```
    
10. Generate a Python list of all the even numbers between 4 to 30.

    ```
    even_numbers = []
    for num in range(4, 31):
        if num % 2 == 0:
            even_numbers.append(num)
    print(even_numbers)
    ```