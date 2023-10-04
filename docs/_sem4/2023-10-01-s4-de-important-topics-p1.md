---
layout: single
classes: wide
title: "Distributed System - Important Topics - Part 1"
excerpt: "DE - Important Topics"
sidebar:
    nav: "s4ds"
header:
  teaser: /assets/images/bca/s4-ds-p1.jpg
author_profile: false
comments: false
share: true
tags:
  - bca
  - distributed systems
  - computer science
  - cs
category:
  - bca
toc: true
toc_sticky: true
toc_label: "On This Page"
toc_icon: "list-ul"

---

## Distributed Systems
- A software system in which components located on networked computers communicate and coordinate their actions by passing messages. 
- A collection of independent computers that appears to its users as a single coherent system.  
- The components interact with each other in order to achieve a common goal. 

## Goals of Distributed Systems

### 1. Resource Sharing
- Cloud-based storage and files
- Peer-to-peer multimedia streaming
- Outsourced mail services
- Content distribution networks for web hosting

### 2. Distribution Transparency
- **Access**: Hides data representation and access methods.
- **Location**: Conceals object location.
- **Relocation**: Masks object movement during use.
- **Migration**: Conceals object movement to another location.
- **Replication**: Hides object replication.
- **Concurrency**: Masks multi-user access.
- **Failure**: Conceals object failure and recovery.

### 3. Openness
- Conforms to well-defined interfaces.
- Supports easy interoperability.
- Enables application portability.
- Allows easy extensibility.

### 4. Scalability
- **Size Scalability**: Scales with the number of users/processes.
- **Geographical Scalability**: Scales over distance.
- **Administrative Scalability**: Scales across admin domains.

## Types Of Distributed Systems

### 1. <u>Distributed Computing Systems</u>
- Primarily used for high-performance applications.
- High-Performance Computing (HPC)

**<u>Examples</u>**
- **Cluster Computing Systems**: 
  - Collection of similar workstations/PCs connected via high-speed LAN.
  - Homogeneous environment (components of same type).
  - Can serve as a supercomputer.
  - Examples: Linux-based Beowulf clusters, MOSIX.
- **Grid Computing**: 
  - Collection of computer resources owned by multiple parties in multiple locations.
  - Heterogeneous environment (components of different types or different vendors).
  - Supports Virtual Organizations (VOs).
  - Examples: EGEE (Europe), Open Science Grid (USA).

### 2. <u>Distributed Information Systems</u>
- Commonly found in traditional office environments.

**<u>Examples</u>**
- **Transaction Processing Systems (TPS)**: POS system, ATMs, Airline/Train Reservation systems
- **Enterprise Application Integration (EAI)**: Apache Camel, IBM Integration Bus
- **Database Management Systems (DBMS)**: Like MySQL, Oracle.
- **Enterprise Resource Planning (ERP)**: Such as SAP, Microsoft Dynamics.
- **Customer Relationship Management (CRM)**: Like Salesforce, HubSpot.

- **Communication Middleware Models/Paradigm**
  - Remote Procedure Call (RPC)
  - Distributed Objects (RMI)  
  - Message-oriented middleware (MOM)

### 3. <u>Distributed Pervasive Systems</u>
- Composed of small components, often in an ad hoc fashion.
- Ubiquitous Systems (available anytime & anywhere)

**<u>Examples</u>**  
- **Mobile Computing**: Involves smartphones, tablets, and laptops.
- **Sensor Networks**: 
  - Organizing a sensor network database, storing and processing data.
- **Internet of Things (IoT)**: Includes smart home devices, industrial IoT.
- **Electronic Health Care Systems**:
  - Questions to be addressed include data storage, loss prevention, alert generation, online feedback, system robustness, and security policies.


## Architecture vs Middleware

### Architecture
- Overall design of software components and their interactions.
- **Role**: Guides the organization and placement of software on machines.

### Middleware
- Software layer on top of OS, standardizes interface for applications.
- **Role**: Manages resources, facilitates communication, and offers services like security.

### Difference
- **Scope**: Architecture is broader; Middleware is a specific layer.
- **Functionality**: Middleware offers specialized services.
- **Flexibility**: Middleware can adapt to changing needs; Architecture is more static.


## Threads Basics & its Role in Distributed Systems  

### Threads
- Smaller units of a program for independent execution.
- Crucial in DS for optimizing performance in multicore and multiprocessor systems.
- **Granularity**: Provides finer control within processes.
- **Flexibility**: Can be replaced by processes for better protection and communication.
- **Concurrency**: Allows multiple operations to be run in parallel.

### Threads Basics
- Threads exist within a process and share the same memory space.
- Thread Context includes minimal information required for sharing the CPU.
- In single-threaded systems, blocking calls can halt the entire process.
- Offers performance gains but requires careful design.
- Threads can be scheduled independently.

### Threads vs Processes (Optional)

|     | Threads                                         | Processes                                         |
|-----|-------------------------------------------------|----------------------------------------------------|
| 1   | Smaller units within a program.                  | A program in execution with its own resources.     |
| 2   | Offer finer control for more tasks.              | Usually single-threaded, coarser tasks.            |
| 3   | Minimal context, mainly processor info.          | Includes CPU values, memory maps, open files.      |
| 4   | Blocking in one thread doesn't halt the process. | Blocking can halt the entire process.              |
| 5   | Better performance in multicore systems.         | Slower due to context switching.                   |
| 6   | Easier to schedule, allows parallel execution.   | Managed by OS, more resource-intensive.            |
| 7   | Can easily share resources like memory.          | Operate with independent resources.                |
| 8   | Threads can affect each other.                   | Processes are isolated from each other.            |
| 9   | Easier communication through shared memory.      | Requires IPC mechanisms, higher overhead.          |
| 10  | Complex design but can be more efficient.        | Simpler to develop but may be less efficient.      |



### Threads in Distributed Systems
- Enables parallelism, improves performance, and is essential for large-scale applications.
- Requires additional intellectual effort for development and debugging.
- Particularly useful in large applications, client-server models, and real-time systems.
- Often relies on Interprocess Communication (IPC) mechanisms for data sharing.
- Easier to scale up applications with well-designed threading.

 
## Virtualizations - Role of Virtualization, Architecture of Virtual Machines

- Virtualization is extending or replacing an existing interface to mimic the behavior of another system, allowing multiple OS and applications to run on a single machine.

![image-center](/assets/images/bca/s4-ds/s4-ds-virtual-1.png){: .align-center}{: width="600" }

*(a) General organization between a program, interface, and system. (b) General organization of virtualizing system A on top of system B.*
{: style="color:gray; font-size: 80%; text-align: center;"}

- <u>Role of Virtualization</u>
  - Initially introduced to allow legacy software to run on expensive mainframe hardware.
  - Important in cloud computing, especially in Infrastructure-as-a-Service (IaaS).
  - Enhances portability and management in distributed systems.
  - Provides isolation, especially relevant in cloud computing, but also introduces new security threats.

### Architecture of Virtual Machines

![image-center](/assets/images/bca/s4-ds/s4-ds-virtual-2.png){: .align-center}{: width="500" }

*This figure shows the different types of interfaces that computer systems generally offer. These interfaces include ISA,the hardware-software interface with privileged instructions for the OS and general instructions for programs, System calls form the OS interface and API, consists of library calls, often hiding system calls.*
{: style="color:gray; font-size: 80%; text-align: center;"}

<br><br>

![image-center](/assets/images/bca/s4-ds/s4-ds-virtual-3.png){: .align-center}{: width="800" }

*(a) <u>Process Virtual Machine</u>: a runtime system that provides an abstract instruction set for executing applications. This type of virtualization is only for a single process.*  
*(b) <u>Native Virtual Machine Monitor</u>: This shows a system implemented as a layer above the original hardware but offering the complete instruction set of that hardware as an interface. It allows multiple and different guest operating systems to run independently and concurrently on the same platform.*  
*(c) <u>Hosted Virtual Machine Monitor</u>: a virtual machine monitor running on top of a trusted host operating system. It can make use of existing facilities provided by the host operating system and is popular in modern distributed systems like data centers and clouds.*
{: style="color:gray; font-size: 80%; text-align: left;"}

<br>