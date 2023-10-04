---
layout: single
classes: wide
title: "Semester 3 - DSA - Mock(Theory)"
excerpt: ""
sidebar:
    nav: "s3dsa"
header:
  teaser: /assets/images/bca/s3-dsa-imp2.jpg

author_profile: false
comments: false
share: true
tags:
  - bca
  - dsa
  - algorithm
  - data structure
  - java
category:
  - bca
toc: false
toc_sticky: true
toc_label: "On This Page"
toc_icon: "list-ul"

---

<br>

**Q1. The rate of growth or order of growth of a function f(n), means how fast the function increases its value as
the input size n increases. List and explain various notations used to express orders of growth.**

<u>Answer:</u>

- **Big O Notation (O)**: Describes the upper bound on the time complexity of an algorithm. Represents the maximum time taken for all input sizes.
    - O(1) is constant time complexity. (Best)
    - O(log n) is logarithmic time complexity. (Good)
    - O(n) is linear time complexity. (Fair)
    - O(n log n) is linearithmic time complexity. (Not ideal)
    - O(n^2) is quadratic time complexity. (Worse)
    - O(n^3) is cubic time complexity. (Worse)
    - O(2^n) is exponential time complexity. (Worst)

- **Big Omega Notation (Ω)**: Provides the asymptotic lower bound, representing the minimum time taken by an algorithm for all input sizes.

- **Big Theta Notation (Θ)**: Gives a tight bound on the time complexity, representing both the best-case and worst-case scenarios.

- **Little o Notation (o)**: Provides an upper bound that is not tight, indicating that the actual time complexity is less than the one specified.

- **Little Omega Notation (ω)**: Provides a lower bound that is not tight, indicating that the actual time complexity is more than the one specified.

These notations help analyze and compare the efficiency of algorithms based on their growth with input size.



**Q2. Recursive functions are executed in a Last In First Out-order. Name a suitable data structure for implementing recursive calls and mention any two operations of that data structure.**

<u>Answer:</u> 
- The suitable data structure for implementing recursive calls is the **Stack**. 
- The two primary operations associated with a stack are:
    - **Push**: This operation adds an element to the top of the stack.
    - **Pop**: This operation removes an element from the top of the stack.

Stacks follow a Last-In-First-Out (LIFO) principle, which aligns with the execution order of recursive functions. When a function calls itself recursively, the call information is "pushed" onto the stack, and when the function returns, the information is "popped" off. This ensures the correct order of execution for nested recursive calls.


**Q3. Name any three algorithm design techniques**

<u>Answer:</u>

**<u>Five common algorithm design techniques:</u>**

1. **Divide and Conquer**: This technique involves breaking down a problem into smaller subproblems, solving each subproblem independently, and then combining the solutions to solve the original problem.

2. **Dynamic Programming**: This technique is used when the subproblems overlap. It involves solving each subproblem only once and then storing the results of each subproblem to avoid duplicate work.

3. **Greedy Algorithms**: This technique involves making the locally optimal choice at each stage with the hope that these local choices will lead to a global optimum.

4. **Backtracking**: This technique is used for solving problems where the solution requires the sequence of decisions. If the sequence of decisions made so far has not led to a solution, then the algorithm goes back and tries the next decision.

5. **Brute Force**: This technique involves trying all possible solutions until a satisfactory solution is found. It is simple to implement but may not be efficient for complex problems.


**Q4. Identify the correct way to declare a multidimenstional array in java.**

<u>Answer:</u>

```
dataType[][] arrayName;
int[][] arr;
or
int arr[][];
```

**Q5. The Pre-order traversal in a tree can also be known as**

- Depth first
- Breadth first
- Topological order
- Linear order

<u>Answer:</u>

- Depth first

Pre-order traversal is a type of depth-first traversal. In a pre-order traversal of a tree, the process is as follows: visit the root node, traverse the left subtree, then traverse the right subtree.


**Q6. Which algorithm design techniques is applied in Merge sort?**

- Divide and conquer
- Greedy Approch
- Backtracking
- Dynamic Programming

<u>Answer:</u>
- Divide and conquer

Merge sort is a classic example of the divide and conquer algorithm design technique. The algorithm recursively divides the array into two halves, sorts them, and then merges the sorted halves.


**Q7. What's the most appropriate data structure to implement a priority queue?**

- Heap
- Circular Array
- Linked List
- Binary Trees

<u>Answer:</u>

- Heap

A heap is the most appropriate data structure to implement a priority queue. It allows for efficient insertion of new elements and removal of the element with the highest priority, both operations being O(log n) in complexity. This is more efficient than using a sorted array, unsorted array, or other data structures like linked lists or binary trees for this purpose.


**Q8. Which of the following data structure is linear type?**

- String
- List
- Queue
- All of this

<u>Answer:</u>
- All of this 
- String is datatype but also an array of characters

<br>