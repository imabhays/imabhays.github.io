---
layout: single
classes: wide
title: "Distributed System - Important Topics - Part 2"
excerpt: "DE - Important Topics"
sidebar:
    nav: "s4ds"
header:
  teaser: /assets/images/bca/s4-ds-p2.jpg
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

## Clients, Servers & Clients-Server Arhchitecture

- **Client**: a process that requests a service from a server
- **Server**: a process that offers a service
- Clients follow request/reply model wrt to using services.

- Servers are organized to do one of two things:
  - Wait
  - Service

- Several ways to organize servers
  - Iterative: Handles request and returns response directly.
  - Concurrent: Uses multi-threading or multi-process, passes request to separate thread or process, no waiting.
- A server can be stateless or stateful. 
  - Stateless server does not remember anything from one request to another. For example, a HTTP server is stateless.
  - Stateful servers maintains information about its clients.

## Clients-Server Arhchitecture

### 1. Centralized Architecture

#### Client-Server Architecture

![image-center](/assets/images/bca/s4-ds/s4-ds-client-server-1.png){: .align-center}{: width="500" }

*Basic Client-Server model*
{: style="color:gray; font-size: 80%; text-align: center;"}

- **Basic Client-Server Model**: Based on client-server interaction/request-reply behavior. Server implements a service, and the client requests that service.
- **Multiple-Client/Single-Server**: All clients connect to a single server.

![image-center](/assets/images/bca/s4-ds/s4-ds-client-server-2.png){: .align-center}{: width="600" }

*Multiple Clients/Multiple Servers*
{: style="color:gray; font-size: 80%; text-align: center;"}

- **Multiple-Client/Multiple-Servers**: Clients can connect to multiple servers for different services.
- **Connection Protocols**: Can be implemented via simple connectionless or connection-oriented protocols.

#### Multitier Systems
- **Multitiered Client-Server**: Distributes traditional server functionality over multiple servers. 
- Each server becomes a client of the next server.

![image-center](/assets/images/bca/s4-ds/s4-ds-client-server-3.png){: .align-center}{: width="700" }

*Two-tiered architecture*
{: style="color:gray; font-size: 80%; text-align: center;"}

<br>

![image-center](/assets/images/bca/s4-ds/s4-ds-client-server-4.png){: .align-center}{: width="600" }

*Three-tiered architecture. An example of a server acting as client.*
{: style="color:gray; font-size: 80%; text-align: center;"}

- **Example**: In a website, the web server acts as an entry point, passing requests to an application server, which interacts with a database server.

### 2. Decentralized Architecture

#### Peer-to-Peer Architecture
- **Basic Concept**: Offers a flexible means for nodes to join and leave the network. All processes provide the same logical services.
- **Overlay Networks**: Processes in a P2P system form an overlay network to keep track of all other processes.
- **Types**: Unstructured overlays and structured overlays like Chord.

#### Hybrid Architecture
- **Combination**: Combines client-server and P2P architectures.
- **Examples**: Superpeer networks, collaborative distributed systems, and edge-server systems.


## Code Migration

### What is Code Migration?
- Code migration involves transferring programs or even running processes between nodes in a distributed system.

### Reasons for Migrating Code
- **Performance**: The most common reason. Code can be moved to balance load or to process data close to its location.
- **Resource Management**: Code can be moved to better utilize resources on a server or client.
- **Flexibility**: Allows for dynamic downloading of software needed for specific tasks.



A process consists of three segments:
- **Code segment**: contains the actual code
- **Resource  segment**: contains the state
- **Execution segment**: contains context of thread executing the object’s code

<br>

![image-center](/assets/images/bca/s4-ds/s4-ds-code-mig-1.png){: .align-center}{: width="700" }

*Alternatives for code migration*
{: style="color:gray; font-size: 80%; text-align: center;"}

### Types of Code Migration
- **Weak Mobility**: Transfers only the code segment, always starts the transferred program anew.
- **Strong Mobility**: Transfers the execution segment, allowing a running process to be stopped and moved.

Also, migration can be sender-initiated or receiver-initiated:
- **Sender initiated**: uploading code to a server. Ex: Client sending a query to database server.
- **Receiver-initiated**: downloading code from a server by a client. Ex: client downloading Java applets from a server.  

### Migration in heterogeneous systems
- Main problem
  - The target machine may not be suitable to execute the migrated code.
  - The definition of process/thread/processor context is highly dependent on local hardware, operating system and runtime system.
- Only solution:
  - Abstract machine implemented on different platforms.
  - Interpreted languages, effectively having their own VM Virtual machine monitors.

### Migrating a Virtual Machine
- Migrating images: 3 alternatives
  - Transfers memory pages to the new machine, resends any modified pages during migration.
  - Halts the current virtual machine, transfers memory, and then starts the new virtual machine.
  - Initiates processes on the new machine right away, pulling in memory pages as required.


## Basic Communication Protocols, Remote Procedure Call, Message Oriented Communication

### Layered Network Communication Protocols

![image-center](/assets/images/bca/s4-ds/s4-ds-middleware-1.png){: .align-center}{: width="600" }

*Layers, interaces and protocols in the OSI model*
{: style="color:gray; font-size: 80%; text-align: center;"}

- **Low-level layers**
  - **Physical layer**: Transmitting bits between sender and receiver
  - **Data link layer**: Transmitting frames over a link, error detection and correction
  - **Network layer**: Routing of packets between source host and destination host
    - **IP**: Internet's network layer protocol
- **Transport layer**: Process-to-process communication
  - **TCP and UDP**: Internet's transport layer protocols
    - **TCP**: Connection-oriented, reliable communication
    - **UDP**: Connectionless, unreliable communication
- **Higher-level layers**
  - **Session and presentation layers**: Not present in the Internet protocol suite
  - **Application layer**: Contains applications and their protocols
    - E.g., Web and HTTP, Email and SMTP

### Middleware Layer
- Middleware Provides common services and protocols for various applications
  - **High-level communication services**: RPC, multicasting
  - **Security protocols**: Authentication protocols, authorization protocols
  - **Distributed Locking Protocols**: For mutual exclusion
  - **Distributed Commit Protocols**: For transaction management

  ![image-center](/assets/images/bca/s4-ds/s4-ds-middleware-2.png){: .align-center}{: width="600" }

*An adapted reference model for networked communication. The Session and Presentation layer have been replaced by a single middleware layer that contains application-independent protocols. Network and Transport services have been grouped into communication services as normally offered by an OS, which, in turn, manages the specific lowest-level hardware used to establish communication.*
{: style="color:gray; font-size: 80%; text-align: center;"}

<br>

### Transient vs Persistent Communication
- **Transient Communication**: Middleware discards undeliverable messages immediately, e.g., Applications using TCP (FTP), UDP (Video streaming)
- **Persistent Communication**: Messages stored until the receiver can accept them, e.g., Email

### Synchronous vs Asynchronous Communication
- **Synchronous Communication**: Real-time communication where information is exchanged with others immediately.
- **Asynchronous Communication**: It doesn't require immediate response. Sender continues execution immediately after sending, message stored by middleware for later processing.

### Remote Procedure Call

  ![image-center](/assets/images/bca/s4-ds/s4-ds-rpc-1.png){: .align-center}{: width="500" }

*RPC between a client and a server*
{: style="color:gray; font-size: 80%; text-align: center;"}

- allows one application to trigger actions in another application (remote) without direct access to its internal procedures.
- Synchronous ‐ based on blocking messages
- Message‐passing details hidden from application
- Procedure call parameters used to transmit data
- Client calls local “stub” which does messaging and marshaling
- Example of RPC frameworks: SUNRPC,DCE RPC, XML‐RPC, SOAP



#### Basic RPC Operation
<br>

  ![image-center](/assets/images/bca/s4-ds/s4-ds-rpc-2.png){: .align-center}{: width="700" }

*The steps involved in a doing a remote computation through RPC.*
{: style="color:gray; font-size: 80%; text-align: center;"}

1. Client program calls client stub.
2. Client stub packs parameters into message (marshaling), calls local OS.
3. Client's OS sends message to remote OS.
4. Remote OS delivers message to server stub.
5. Server stub unpacks message, calls server procedure.
6. Server does work, returns result to stub.
7. Server stub packs result in message, calls local OS.
8. Server's OS sends message to client's OS.
9. Client's OS delivers message to client stub.
10. Client stub unpacks result (unmarshalling), returns to client program.

### Message Oriented Communication

- A way for applications to communicate by inserting messages into specific queues.
- Messages are forwarded over a series of communication servers and eventually delivered to the destination.
- Each application has its own private queue for receiving messages.

**Basic interface to a queue in a message-queuing system:**

| Operation | Description |
|-----------|-------------|
| PUT       | Append a message to a specified queue |
| GET       | Block until the specified queue is nonempty, and remove the first message |
| POLL      | Check a specified queue for messages, and remove the first. Never block |
| NOTIFY    | Install a handler to be called when a message is put into the specified queue |


  ![image-center](/assets/images/bca/s4-ds/s4-ds-message-comm-1.png){: .align-center}{: width="700" }

*Relationship between queue-level addressing and network-level addressing.*
{: style="color:gray; font-size: 80%; text-align: center;"}


- **Queue managers**: Queues are managed by queue managers. 
  - An application can put messages only into a local queue. 
  - Getting a message is possible by extracting it from a local queue only
  - The system keeps track of where each queue is located on the network















