---
layout: single
classes: wide
title: "Semester 3 - Python - Assignment 1"
excerpt: "Flashcards for Python"
sidebar:
    nav: "s3python"
header:
  teaser: /assets/images/bca/s3-python-assignment-4.jpg
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


# Assignment IV


Q1. What is the type of the following variable?

```
aTuple = ("Orange")
print(type(aTuple))
```

- list
- tuple
- array
- str

Answer: `str`

Q2. Select true statements regarding the Python tuple.

- We can remove the item from tuple but we cannot update items of the tuple.
- We cannot delete the tuple.
- We cannot remove the items from the tuple.
- We cannot update items of the tuple.

Answer: `True statements: We cannot update items of the tuple. We cannot remove the items from the tuple.` 




Q3. What is the output of the following?

    ```
    aTuple = (10, 20, 30, 40, 50, 60, 70, 80)
    print(aTuple[2:5], aTuple[:4], aTuple[3:])
    ```

Answer 3: `(30, 40, 50)` `(10, 20, 30, 40)` `(40, 50, 60, 70, 80)` 


Q4. What is the output of the following?

    ```
    aTuple = "Yellow", 20, "Red"
    a, b, c = aTuple
    print(a)
    ```

Answer 4: `Yellow` 


Q5. What is the output of the following tuple operation?

    ```
    aTuple = (100, 200, 300, 400, 500)
    aTuple.pop(2)
    print(aTuple)
    ```

Answer 5: `AttributeError` 
    
Q6. Select all the correct ways to remove the key "marks" from a dictionary.

    ```
    student = {
        "name": "Emma",
        "class": 9,
        "marks": 75
    }
    
    student.pop("marks")
    del student["marks"]
    ```

Answer 6: 
```
student.pop("marks")
del student["marks"]
``` 
    
Q7. What is the output of the following?

    ```
    sampleDict = dict([
        ('first', 1),
        ('second', 2),
        ('third', 3)
    ])
    print(sampleDict)
    ```

Answer 7: `{'first': 1, 'second': 2, 'third': 3}` 


Q8. What is the output of the following dictionary operation?

```
dict1 = {"name": "Mike", "salary": 8000}
temp = dict1.pop("age")
print(temp)
```

Answer 8: `KeyError: ‘age’` 


Q9. Write a Python program to add an item to a tuple.

Answer 9:
```
# original tuple
my_tuple = (1, 2, 3, 4)
# item to be added
new_item = 5
# concatenate the original tuple with the new item tuple
new_tuple = my_tuple + (new_item,)
# print the original tuple and the new tuple
print("Original Tuple:", my_tuple)
print("New Tuple:", new_tuple)
``` 

Q10. Write a Python program to convert a list to a tuple.

```
# original list
my_list = [1, 2, 3, 4, 5]
# convert the list to a tuple
my_tuple = tuple(my_list)
# print the original list and the new tuple
print("Original List:", my_list)
print("New Tuple:", my_tuple)
``` 

Q11. Write a Python program to reverse a tuple.

```
# define the original tuple
my_tuple = (1, 2, 3, 4, 5)
# create a new tuple with the elements in reverse order
reversed_tuple = my_tuple[::-1]
# print the original tuple and the reversed tuple
print("Original Tuple:", my_tuple)
print("Reversed Tuple:", reversed_tuple)
``` 

Q12. Write a Python program to sum all the items in a dictionary.

```
# our dictionary
my_dict = {"a": 1, "b": 2, "c": 3}
sum = 0
for value in my_dict.values():
    sum += value
# print the sum
print("Sum of items in the dictionary:", sum)
``` 

Q13. Write a Python program to get the maximum and minimum values of a dictionary.

```
# dictionary
my_dict = {'a': 5, 'b': 10, 'c': 3, 'd': 8}
# Get the maximum value
max_value = max(my_dict.values())
# Get the key corresponding to the maximum value
max_key = max(my_dict, key=my_dict.get)
# Get the minimum value
min_value = min(my_dict.values())
# Get the key corresponding to the minimum value
min_key = min(my_dict, key=my_dict.get)
# Print
print("Maximum value is:", max_value, "with key:", max_key)
print("Minimum value is:", min_value, "with key:", min_key)
``` 

Q14. Write a Python program to get the key, value, and item in a dictionary.

```
# Create the dictionary
my_dict = {'a': 5, 'b': 10, 'c': 3, 'd': 8}
# Get the keys, values, and items of the dictionary
keys = my_dict.keys()
values = my_dict.values()
items = my_dict.items()
# Print the keys, values, and items
print("Keys:", keys)
print("Values:", values)
print("Items:", items)
``` 

Q15. Write a Python program to drop empty items from a given dictionary.

    Original Dictionary: `{'c1': 'Red', 'c2': 'Green', 'c3': None}`
    
    New Dictionary after dropping empty items: `{'c1': 'Red', 'c2': 'Green'}`

```
# Create the original dictionary
original_dict = {'c1': 'Red', 'c2': 'Green', 'c3': None}
# Create an empty dictionary to hold the non-empty items
new_dict = {}
# Loop through the original dictionary and add non-empty items to the new dictionary

for key, value in original_dict.items():
    if value is not None:
        new_dict[key] = value
# Print
print("Original Dictionary:", original_dict)
print("New Dictionary after dropping empty items:", new_dict)
```