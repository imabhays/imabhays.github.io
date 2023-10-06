---
layout: single
classes: wide
title: "Distributed System - Important Topics - Part 3"
excerpt: "DE - Important Topics"
sidebar:
    nav: "s4ds"
header:
  teaser: /assets/images/bca/s4-ds-p3.jpg
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

## Names, Identifiers and Addresses, Flat naming, Structured Naming, Attribute-Based naming

### Overview
- Names are identifiers for various things like *entities, locations, and resources.* 
- The goal is to resolve these names to what they actually represent.
  - **Human-Friendly Names**: How to structure names that are easy for humans to understand, such as in file systems or the World Wide Web.
    - Example: World Wide Web, "www.google.com" is easier to remember than IP address like "142.250.191.46".
  - **Location-Independent Naming**: Finding a way to identify entities without depending on their current location.
    - Example: DNS (Domain Name System), Resolves domain names to IP addresses, allowing you to access a website from anywhere.
  - **Attribute-Based Resolution**: Resolving names by using attributes of the entity they refer to.
    - Example: Database Query, Using SQL to find records based on attributes like "age" or "email".

### Names, Identifiers and Addresses
- **Name**: in a distributed system is a string of bits or characters used to refer to an *entity.*
- **Entity**: something that is operated on using some access point.
- Entities: hosts, printers, disks, files, processes, users, mailboxes, web pages, graphical windows, messages,network connections, etc.
- **Address**: Name that refers to an access point of an entity.
  - An entity may have multiple access points and addresses.
- **Identifiers**: Used to uniquely identify an entity. 
- An identifier is a name with the following properties
  - An identifier refers to at most one entity
  - Each entity is referred to by at most one identifier
  - An identifier always refers to the same entity (i.e., it is Never reused)
- **Name resolution** maps a name to its address.
  - Name resolution is performed by a naming system.
  - In a distributed system, a naming system is itself distributed.

- **Naming system**: a middleware that assists in name resolution
- Naming systems are classified into three classes based on the type of names used:
  1. Flat naming
  2. Structured naming
  3. Attribute-based naming

### Flat Naming
- Identifiers are flat names
- fixed sized random bit strings
- does not contain any information on how to locate an entity
- good for machines
- How to resolve flat names?
  - Broadcasting
  - Forwarding pointers
  - Home-based approaches: Mobile IP
  - Distributed Hash Tables: Chord

#### Broadcasting
- Broadcast the identifier to the complete network.
- The entity associated with the identifier responds with its current address.
- Example: Address Resolution Protocol (ARP)
  - Resolve an IP address to a MAC address.
  - In this,
    - IP address is the identifier of the entity
    - MAC address is the address of the access point
- Not scalable in large networks

#### Forwarding Pointers
- for locating mobile entities
- When an entity moves from location A to location B, it leaves behind (in A) a reference to its new location at B.
- Example: Name resolution mechanism
  - Follow the chain of pointers to reach the entity
  - Update the entity’s reference when the present location is found
- Long chains results in longer resolution delays & are prone to failure due to broken links.

#### Home based Approaches
- Each mobile entity has a fixed IP address (home address)
  - Entity’s home address is registered at a naming service
  - Home node keeps track of current address of the entity (care‐of address)
  - Entity updates the home about its current address (care‐of address) whenever it moves

#### Distributed Hash Table (DHT): Chord
- Every node is assigned a random m‐bit identifier
- Every entity is assigned a unique m‐bit key
- Entity with key k falls under jurisdiction of node with the smallest identifier id ≥ k , denoted as succ(k)
- How to resolve a key k to the address of succ(k)?
  - Each node p maintains a finger table with at most m entries, value of the i<sup>th</sup> entry is FT<sub>p</sub>[i]= succ(p+2<sup>i‐1</sup>) 
  - To look up a key k, node p forwards the request to node q with index j where q = FT<sub>p</sub>[j] ≤ k < FT<sub>p</sub>[j+1]
  - If p < k < FT<sub>p</sub>[1], the request is forwarded to FT<sub>p</sub>[1]
  - A lookup requires O(logN) steps, where N is number of nodes in the system.
  - *Please refer to the assignment related to Chord OR the example below*

  ![image-center](/assets/images/bca/s4-ds/s4-ds-chord-1.png){: .align-center}{: width="700" }

*Resolving key 26 from node 1 (in red) and key 12 from node 28 (in green) in a Chord system.*
{: style="color:gray; font-size: 80%; text-align: center;"}


##### Exploiting network proximity
- *Problem*: The logical organization of nodes in the overlay may lead to erratic message transfers in the underlying Internet: node p and node succ(p+1) may be very far apart.
- *Solutions*:
  - **Topology-aware node assignment:** When assigning an ID to a node, make sure that nodes close in the ID space are also close in the network. 
    - Can be very difficult.
  - **Proximity routing**: Maintain more than one possible successor, and forward to the closest.
  - **Proximity neighbor selection**:When there is a choice of selecting who your neighbor will be (not in Chord), pick the closest one.

#### Hierarchical Approches
- Large-scale search tree for which the underlying network is divided
into hierarchical domains. 
- Each domain is represented by a separate directory node.

  ![image-center](/assets/images/bca/s4-ds/s4-ds-heirar.png){: .align-center}{: width="700" }

*Hierarchical organization of a location service into domains, each having an associated directory node.*
{: style="color:gray; font-size: 80%; text-align: center;"}

### Structured Naming

- Flat names are hard to remember, so human-friendly names are used which are structured and organized into *name spaces*.

  ![image-center](/assets/images/bca/s4-ds/s4-ds-struc.png){: .align-center}{: width="700" }

*A general naming graph with a single root node.*
{: style="color:gray; font-size: 80%; text-align: center;"}

- Name Resolution: Process of looking up a name and it's performed by traversing the graph.

- **Two main approaches to name resolution:**

  ![image-center](/assets/images/bca/s4-ds/s4-ds-naming-space.png){: .align-center}{: width="950" }

*Resolving the name "ftp.cs.vu.nl". Iterative name resolution (left) vs Recursive name resolution (right)*
{: style="color:gray; font-size: 80%; text-align: center;"}

- **Iterative Name Resolution:**
  1. Client's name resolver sends the complete name to the root name server.
  2. Root server partially resolves the name and returns the result to the client's resolver, which then contacts the next name server in the hierarchy.
  3. This process continues until the complete name is resolved.

- **Recursive Name Resolution:**
  1. Each name server passes the partially resolved name to the next name server in the hierarchy.
  2. The last name server in the chain returns the fully resolved name to the first name server, which then returns it to the client's resolver.

 **Iterative vs Recursive**
- Iterative involves more steps but less server load.
- Recursive is more efficient in caching and lowers communication costs.

- Name Space implementation: For a large‐scale distributed system is partitioned into three logical layers
  1. **Global layer**: high‐level directory nodes
  2. **Administrational layer**: directory nodes managed by a single organization
  3. **Managerial layer**: nodes that change frequently

  ![image-center](/assets/images/bca/s4-ds/s4-ds-implementation.png){: .align-center}{: width="700" }

*An example partitioning ofthe DNS name space, including Internet‐accessible files, into three layers.*
{: style="color:gray; font-size: 80%; text-align: center;"}

### Attribute based naming
- Also known as directory services
- Entities have a set of associated attributes for searching.
- Attributes can be simple like sender, recipient, subject in an email system.
- Describes an entity in terms of (attribute, value) pairs.
- Naming system returns entities that meet the user's description.
- Examples:
  - In an email system, messages can have attributes like sender, recipient, and subject.
  - In a file system, files could have attributes like file type, owner, and date modified.

- Challenges:
  - Exhaustive search through all descriptors can be performance-intensive.
  - Balancing the load among servers for attribute-based queries is essential.

