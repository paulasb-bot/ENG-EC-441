# IP Addressing, CIDR and Subnetting – Worked Problem

## 1. Introduction

IP addressing is fundamental to the Network layer. It allows devices to be uniquely identified and enables routing across networks.

CIDR (Classless Inter-Domain Routing) improves address allocation by allowing flexible subnet sizes instead of fixed classes. Subnetting allows a network to be divided into smaller sub-networks for efficiency and organization.

---

## 2. Problem Statement

Given the network:

192.168.10.0/24

Design subnets for the following requirements:

- Subnet A: at least 50 hosts  
- Subnet B: at least 20 hosts  
- Subnet C: at least 10 hosts  
- Subnet D: at least 5 hosts  

Tasks:

1. Determine the appropriate subnet mask for each subnet.
2. Assign IP ranges using VLSM (Variable Length Subnet Masking).
3. Specify network address, first usable IP, last usable IP, and broadcast address for each subnet.

---

## 3. Step 1 – Sort Requirements

We allocate subnets from largest to smallest:

- 50 hosts  
- 20 hosts  
- 10 hosts  
- 5 hosts  

---

## 4. Step 2 – Determine Subnet Sizes

We use the formula:

2^n - 2 ≥ required hosts

### Subnet A (50 hosts)

2^6 - 2 = 62 → need 6 host bits  
Prefix: /26  

### Subnet B (20 hosts)

2^5 - 2 = 30 → need 5 host bits  
Prefix: /27  

### Subnet C (10 hosts)

2^4 - 2 = 14 → need 4 host bits  
Prefix: /28  

### Subnet D (5 hosts)

2^3 - 2 = 6 → need 3 host bits  
Prefix: /29  

---

## 5. Step 3 – Assign Subnets (VLSM)

Start from 192.168.10.0

---

### Subnet A (/26)

- Network: 192.168.10.0/26  
- Range: 192.168.10.1 – 192.168.10.62  
- Broadcast: 192.168.10.63  

---

### Subnet B (/27)

Next available block starts at 192.168.10.64

- Network: 192.168.10.64/27  
- Range: 192.168.10.65 – 192.168.10.94  
- Broadcast: 192.168.10.95  

---

### Subnet C (/28)

Next block starts at 192.168.10.96

- Network: 192.168.10.96/28  
- Range: 192.168.10.97 – 192.168.10.110  
- Broadcast: 192.168.10.111  

---

### Subnet D (/29)

Next block starts at 192.168.10.112

- Network: 192.168.10.112/29  
- Range: 192.168.10.113 – 192.168.10.118  
- Broadcast: 192.168.10.119  

---

## 6. Summary Table

| Subnet | Network Address       | First IP        | Last IP         | Broadcast        | Prefix |
|--------|----------------------|-----------------|-----------------|------------------|--------|
| A      | 192.168.10.0         | 192.168.10.1    | 192.168.10.62   | 192.168.10.63    | /26    |
| B      | 192.168.10.64        | 192.168.10.65   | 192.168.10.94   | 192.168.10.95    | /27    |
| C      | 192.168.10.96        | 192.168.10.97   | 192.168.10.110  | 192.168.10.111   | /28    |
| D      | 192.168.10.112       | 192.168.10.113  | 192.168.10.118  | 192.168.10.119   | /29    |

---

## 7. Analysis

VLSM allows efficient use of IP address space by allocating subnet sizes based on actual requirements.

Instead of wasting addresses with fixed subnet sizes, each subnet is tailored to its number of hosts.

This approach is widely used in modern network design.

---

## 8. Reflection

This exercise demonstrates how CIDR and subnetting improve scalability and efficiency in IP networks.

Understanding how to calculate subnet sizes and allocate address ranges is essential for designing real-world networks.

The use of VLSM shows how flexibility in addressing leads to better resource utilization compared to traditional class-based addressing.