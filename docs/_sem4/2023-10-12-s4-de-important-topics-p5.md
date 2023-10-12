---
layout: single
classes: wide
title: "Distributed System - Important Topics - Part 5"
excerpt: "DE - Important Topics"
sidebar:
    nav: "s4ds"
header:
  teaser: /assets/images/bca/s4-ds-p5.jpg
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


## Security

- **Security policies**: Precise definition of "which" entities in the system can take "what" actions to protect its assets
- **Security Mechanism**: Means of enforcing that policy
- Distributed System Security:
    1. **Secure Channel**: Communication between users or processes that may be on different machines (authentication, message integrity, confidentiality)
    2. **Access Control**: Authorization to ensure that a user or process performs only those actions that is allowed under the security policy

### Basic Concepts
- **Security**: attempt to protect the services and data it offers against security threats
- **Confidentiality**: ensure no one unauthorized can access the system's assets
- **Integrity**: Alterations to a system’s assets can be made only in an authorized way
- **Availability**: ensure authorized entity can access the assets they need when they need to

### Security Mechanism
- **Encryption**
  - Transform data into something an attacker cannot understand
  - Provides a means to implement confidentiality
  - Provides support for integrity
- **Authentication**
  - Verify the claimed identity of a user, client, server, and so on
- **Authorization**
  - Check whether the client is authorized to perform the action requested
- **Auditing**
  - Auditing tools are used to trace which clients accessed what, and which way

### Secure Channels
- Authenticate communicating parties and ensure message integrity and confidentiality.
- Protects against **interception**, **modification**, and **fabrication** of messages.
- Doesn't always protect against interruption.
- Ensuring confidentiality prevents interception.
- Protocols for mutual authentication and message integrity prevent modification and fabrication.
- Authentication needed for message integrity
    - Shared key (symmetric): one key for encryption and decryption
    - Public-Private key (asymmetric): publik key for encryption & private key for decryption
- Message Integrity & Confidentiality : Besides authentication, secure channel should also provide guarantee message integrity and confidentiality
    - Digital Signatures: uniquely tying signature to the content using RSA, MD5
    - Session Keys: used for confidentiality by communicating entities after authentication

### Access Control
- Post secure channel setup, clients can issue requests to servers.
- Execution of requests depends on the client's **access rights**.
- "**Access control**" verifies access rights.
- "**Authorization**" is about granting access rights.

#### Role Based Access Control

- Protection domains can be implemented as roles, like "manager" or "editor", instead of just groups like "HR" or "Marketing".
- Users log in with specific roles tied to their organizational functions.
- Users can have multiple roles or functions.
- The chosen role upon login defines the user's privileges and operational protection domain.

### DISTRIBUTED INFORMATION SECURITY MANAGEMENT MODEL (DISMM)

- Effective security management process
- Reduced cost of security management
- Subject Matter Expert (SME) contribution
- Formal accountability across the Enterprise
- Improved collaboration across various business teams
- Make security an enterprise priority (vs. being just an IT task)

### Types of Threats (Optional)

- **Interception:** Unauthorized party has gained access to a service or data.
- **Interruption:** Services or data become unavailable, unusable, destroyed, etc.
- **Modification:** Unauthorized changing of data or tampering with a service.
- **Fabrication:** Generating additional data or activity that wouldn't normally exist.

### Methods of Attack (Optional)

- **Eavesdropping:**  Secretly monitoring or intercepting private communications.
- **Masquerading:** Pretending to be another user or system to gain unauthorized access.
- **Message tampering:**
  - Intercepting messages and altering their contents.
  - Commonly known as a "Man-in-the-middle attack".
- **Replaying:** Storing intercepted messages and sending them out later.
- **Denial of service:** Flooding a channel or resource with messages to deny access for others.






