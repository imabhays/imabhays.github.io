---
layout: single
classes: wide
title: "Distributed System - Important Topics - Part 4"
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


## Replication
- It is the process of maintaining the data at multiple computers.
- **Necessary for**
  1. Improving performance
  2. Increasing the availability of services
  3. Enhancing the scalability of systems
  4. Securing against malicious attacks
- **Key issue**: if there are many replicas of the same thing, how do we keep all of them up-todate? How do we maintain *consistency* of replicated data? 

## Consistency Models
1. **Data-Centric Consistency Models**
  - Continuous
  - Sequential
  - Causal
2. **Client-Centric Consistency Models**
  - Monotonic Reads
  - Monotonoc Writes
  - Read Your Writes
  - Write Follow Reads

### Data-store (Optional)

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-8.png){: .align-center}{: width="500" }

*The general organization of a logical data store, physically distributed and replicated across multiple processes.*
{: style="color:gray; font-size: 80%; text-align: center;"}

- A data store is a service that stores data, E.g., databases, file systems, web servers
- Consists of multiple servers each containing a copy of all the data items stored in the data store
- Can be read from or written to by any process in a DS.
- Reads are performed locally
- Writes are performed locally first and then propagated to remote replicas 

### 1. **Data-Centric Consistency Models**

#### a. **<u>Continuous Consistency</u>**

- Applications can specify tolerable inconsistencies. Three axes of inconsistencies:

  1. Numerical value deviation between replicas.
  2. Staleness deviation between replicas.
  3. Update operation ordering deviation.
- These are termed as "continuous consistency ranges."

#### b. **<u>Sequential Consistency</u>**

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-1.png){: .align-center}{: width="700" }

*(a) A sequentially consistent data store. (b) A data store that is not sequentially consistent.*
{: style="color:gray; font-size: 80%; text-align: center;"}


- A weaker consistency model, which represents a relaxation of the rules.
- It is also much easier (possible) to implement.
- All clients see all (write) operations performed in the same order:
  - Assumes all operations are executed in some sequential order
  - Program order is maintained (i.e., the order of writes as performed by a single process must be maintained)
  - All processes see the same ordering of operations 

#### c. **<u>Causal Consistency</u>**

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-2.png){: .align-center}{: width="600" }

*This sequence is allowed with a causally-consistent store, but not with a sequentially consistent store.*
{: style="color:gray; font-size: 80%; text-align: center;"}

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-3.png){: .align-center}{: width="700" }

*(a) A violation of a causally-consistent store. (b) A correct sequence of events in a causally-consistent store.*
{: style="color:gray; font-size: 80%; text-align: center;"}

- Weaker than sequential consistency
- Two operations are causally related if:
  - A read is followed by a write in the same client
  - A write of a data item is followed by a read of that data item in any client
- Writes that are potentially causally related must be seen by all processes in the same order.
- Concurrent writes may be seen in a different order on different machines (i.e., by different processes as long as program order is respected). 

### 2. **Client-Centric Consistency Models**

- Client-centric consistency provides guarantees for a single client for its accesses to a data-store

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-4.png){: .align-center}{: width="700" }

*The read operations performed by a single process P at two different local copies of the same data store. (a) A monotonic-read consistent data store. (b) A data store that does not provide monotonic reads.*
{: style="color:gray; font-size: 80%; text-align: center;"}

#### a. **<u>Monotonic reads</u>**: 
- If a process reads the value of a data item x, any successive read operation on x by that process will always return that same value or a more recent value.

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-5.png){: .align-center}{: width="700" }

*The write operations performed by a single process P at two different local copies of the same data store. (a) A monotonic-write consistent data store. (b) A data store that does not provide monotonic-write consistency.*
{: style="color:gray; font-size: 80%; text-align: center;"}

#### b. **<u>Monotonic writes</u>**: 
- A write operation by a process on a data item x is completed before any successive write operation on x by the same process. 

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-6.png){: .align-center}{: width="700" }

*(a) A data store that provides read-your-writes consistency. (b) A data store that does not.*
{: style="color:gray; font-size: 80%; text-align: center;"}

#### c. **<u>Read your writes</u>**: 
- The effect of a write operation by a process on data item x will always be seen by a successive read operation on x by the same process.

  ![image-center](/assets/images/bca/s4-ds/s4-ds-consistency-7.png){: .align-center}{: width="700" }

*(a) A writes-follow-reads consistent data store. (b) A data store that does not provide writes-follow-reads consistency.*
{: style="color:gray; font-size: 80%; text-align: center;"}

#### d. **<u>Writes follow reads</u>**: 
- A write operation by a process on a data item x following a previous read operation on x by the same process is guaranteed to take place on the same or more recent value of x that was read.