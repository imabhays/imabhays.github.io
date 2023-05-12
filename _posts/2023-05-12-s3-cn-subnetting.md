---
layout: single
classes: wide
title: "Semester 3 - Computer Networks -Subnetting"
excerpt: "Semester 3 - Computer Networks - Subnetting"
sidebar:
    nav: "s3cn"
header:
  teaser: /assets/images/bca/s3-cn-subnetting.jpg

author_profile: false
comments: false
share: true
tags:
  - bca
  - networking
  - ccna
  - netacad
  - networks
  - computer networks
  - network theory
category:
  - bca
toc: true
toc_sticky: true
toc_label: "On This Page"
toc_icon: "list-ul"

---

## What?

**<u> Subnetting </u>**

- Subnetting is a practice of dividing the network in two more sub networks or subnets.

## Why?

- Speed, security, efficient usage of ip addresses, simplification of large network. Example every department in a large/small organization like accounts, sales, HR etc. needs their own networts for various specified reasons.

## How? (Subnetting IP4)

Understanding of how many subnets & how many host, would solve your question.

Their are many ways you can disect information the given ip address.

Let's take an example of an ip4 address **172.18.0.0**

- we can say this ip is from class B because it's first octet is 172 and class B range is 128 - 191
- since it's class B, subnet mask should be 255.255.0.0 meaning most significant (left most) 16 bits is network portion and rest 16 bits is for hosts.

if we're given this ip with subnet mask then information might change bases on the subnet mask.

```
IP - 172.18.0.0
Subnet Mask - 255.255.192.0
Binary of subnet mask - 11111111.11111111.11000000.00000000
```
We should be looking into how subnetting is done?
- to make new networks (or subnetworks) we need bits just like how first 16 bits are used for network, but those 16 bits are already taken and we've limited total count of 32 bits in an Ip address.
- so we "borrow" bits from host (right most) portion to create new network. We use "borrow" because we can't create new bits but we can only borrow.
- you may ask how many we should take? It depends on need in real life and question in exam. We will will cover this part in examples.

Let's go back to our example again

- Information we can dissect
  - class B
  - third octet in subnet mask is interesting, it represents that subnetting is done.
  - by converting the subnet mask in binary, it's clear that 2 bits are borrowed from host part.(11000000)
  - prefix should be 16 + 2 = /18 (mostly given in question)
  - from 11000000.00000000, we can say that
    - **total subnets** is 2^bits borrowed ( 2 bit borrowed) = 2^2 = 4
    - total hosts ( 14 bits are still left for hosts) = 2^14 = 16,384
    - we always deduct 2 from total number of host because, one is reserved for network identifier and one is for broadcast.
    - so, **total hosts per subnet** = 16,384-2 = 16,382

<br>

**Total subnets, Valid subnets & Block size**

- No. of subnets depends on no. of borrowed bits. If n bits, are borrowed then total subnets would be **2^n**
- From total no. of subnets, we may know valid subnets only if we know network idenfiers for example start and end of subnets.
-  All subnets will be in same increments which would be 

**256-subnet mask (interesting octet) = increment or block size**

- Block size or increment tells us the interval between next subnet.

So, for the last time what we can tell from the ip and subnetmask we have,

```
IP - 172.18.0.0  
Subnet Mask - 255.255.192.0  
Binary of subnet mask - 11111111.11111111.11000000.00000000
```

**<u> How many subnets does the chosen subnet mask produce?</u>**  
- 2 bits borrowed
- **2^2 = 4** 

**<u> How many valid hosts per subnet are available? </u>**  
- we are left with 14 bits for hosts
- **2^14 - 2 = 16,382 hosts per subnet**  

**<u> What are the valid subnets? </u>**
- **(256 - 192) =  64**, is the increment or block size. so valid subnets will be **0, 64, 128 and 192**
- Subnets would be: 172.18.0.0, 172.18.64.0, 172.18.128.0, and 172.18.192.0  

**<u> What’s the broadcast address of each subnet? </u>**  

Broadcast is the last address of network. See table below

**<u> What are the valid first and last hosts in each subnet? </u>**

| Subnet     | First Host  | Last Host   | Broadcast   |
|------------|-------------|-------------|-------------|
| 172.18.0.0   | 172.18.0.1   | 172.18.63.254 | 172.18.63.255 |
| 172.18.64.0  | 172.18.64.1  | 172.18.127.254| 172.18.127.255|
| 172.18.128.0 | 172.18.128.1 | 172.18.191.254| 172.18.191.255|
| 172.18.192.0 | 172.18.192.1 | 172.18.255.254| 172.18.255.255|


**Formulas:**   
<u>Total subnets = 2^bits borrowed</u>   
<u>Block size or increment (for network identifier)</u>  = 256 - (interesting octet number)    
<u>Network /identifier or subnet id</u>  = first address of network    
<u>Broadcast address</u>  = last address of network  
<u>Total number of hosts</u>  = (2^bits left for hosts - 2)    
<u>First valid address of a network</u>  = 2nd address (because first is network idenfier)  
<u>Last valid address of a network</u>  = last address - 1  
{: .notice--success}


## Case

- Divide this Network Address 192.168.10.0/27 into two subnets.
- This question could be asked in another way. How many subnets does 192.168.10.0/27 have?

Write this for reference on paper  

**<u> Power of 2s </u>**

| 2^7 | 2^6 | 2^5 | 2^4 | 2^3 | 2^2 | 2^1 | 2^0 |
|-----|-----|-----|-----|-----|-----|-----|-----|
| 128 | 64  | 32  | 16  | 8   | 4   | 2   | 1   |

<br>
- For 2nd question
  - address is class C, last octet is 11100000 and subnet mask is 255.255.255.224
  - no. of subnets, 2^3 = 8
  - block size 256 - 224 = 32
  - valid subnets --> 192.168.10.0,192.168.10.32.......,192.168.10.192, 192.168.10.224
  - no. of valid hosts in each subnet, (2^5) - 2 = 30

But original question is too further divide /27 in two subnets, let's do this.

- to create to subnet we need to borrow one more bit from host portion.
- last octect would look like this 11110000
- prefix would be 27+1 = /28 and subnet mask would be 255.255.255.240 ( 128+64+32+16 see reference table)
- no. of subnets possible with /28 irrespective how many we need, 2^4 = 16
- block size, 256 - 240 = 16
- valid subnets, 192.168.10.0, 192.168.10.16, 192.168.10.32,........,192.168.10.240
- no. of valid hosts in each subnet, (2^4) - 2 = 14
- for the question, we'll only use two
- **subnet 1**
  - network identifier or subnet id = 192.168.10.0
  - broadcast address = 192.168.10.15
  - first usable address = 192.168.10.1
  - first usable address = 192.168.10.14
- **subnet 2**
  - network identifier or subnet id = 192.168.10.16
  - broadcast address = 192.168.10.31
  - first usable address = 192.168.10.17
  - first usable address = 192.168.10.30 

This was for IP4 -->   
IP6 subnetting is easy if you understand IP4 subnetting.



## Subnetting - IP6

- Before we begin, we should know about the ip6 address

![image-center](/assets/images/bca/s3-cn/images/ip6.png){: .align-center}{: width="500" }

- Ip6 consists of 128 bits divided in 8 hextets (like octets in ip4), 4 hexa digits in each block and each hexa digit represents 4 bits.
- this means we have 16 bit of 1 hextet.
- the right most 64 bit is interface identifier, which is auto-derived from device MAC address. This are your host addresses.
- left most 64 bit is network portion
- we can further divide left most 64 network into 48 bit & 16 bit, where 48 bit is reserved for ISP + site subnets (organizations) and rest 16 bit is for subnetting.
- so we've network id (48 bit), subnet id (16 bit), interface id (64 bit)
- Without subnetting, an ip6 address would have 64 bits for hosts = 2^64 - 2 in a single subnet- 

Please follow these links for examples: 

[Real life example](https://community.cisco.com/t5/networking-knowledge-base/ipv6-subnetting-overview-and-case-study/ta-p/3125702){:target="_blank"}

[Further reading in Ip4](https://ipcisco.com/lesson/subnetting-in-ipv4/){:target="_blank"}













