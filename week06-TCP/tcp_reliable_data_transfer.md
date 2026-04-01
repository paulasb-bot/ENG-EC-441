# TCP Reliable Data Transfer – Analysis and Mechanisms

## 1. Introduction

The Transport layer is responsible for providing reliable communication between processes running on different hosts.

TCP (Transmission Control Protocol) ensures reliability through mechanisms such as acknowledgments (ACKs), retransmissions, sequence numbers, and timers.

---

## 2. Objective

The goal of this assignment is to:

1. Understand how TCP achieves reliable data transfer.
2. Analyze the role of sequence numbers and acknowledgments.
3. Study retransmission behavior.
4. Explain how errors and losses are handled.

---

## 3. Basic Concepts

TCP ensures reliability using:

- Sequence numbers → identify each byte of data
- ACKs → confirm received data
- Retransmission → resend lost segments
- Timers → detect packet loss
- Sliding window → control flow

---

## 4. Problem Scenario

Host A sends 4 segments to Host B:

- Segment 1 → Seq = 0  
- Segment 2 → Seq = 100  
- Segment 3 → Seq = 200  
- Segment 4 → Seq = 300  

Assume each segment carries 100 bytes.

During transmission:

- Segment 2 is lost
- All others arrive correctly

---

## 5. Receiver Behavior

Host B receives:

- Segment 1 → OK → sends ACK = 100  
- Segment 3 → out of order → discards → sends ACK = 100  
- Segment 4 → out of order → discards → sends ACK = 100  

Explanation:

TCP uses cumulative ACKs.  
It only acknowledges the next expected byte.

---

## 6. Sender Behavior

Host A receives duplicate ACKs:

- ACK = 100 (multiple times)

This indicates that segment 2 is missing.

TCP triggers retransmission:

- Segment 2 is retransmitted

---

## 7. After Retransmission

Once Segment 2 arrives:

Host B now has:

- Segment 1  
- Segment 2  
- Segment 3  
- Segment 4  

It sends:

ACK = 400

This acknowledges all data up to byte 399.

---

## 8. Timeline Representation

A → B:

Seg1 → Seg2 (lost) → Seg3 → Seg4  

B → A:

ACK100 → ACK100 → ACK100  

A → B:

(retransmit Seg2)

B → A:

ACK400  

---

## 9. Analysis

This example demonstrates key TCP mechanisms:

- **Cumulative ACKs** reduce overhead
- **Duplicate ACKs** signal packet loss
- **Retransmission** ensures reliability
- **Out-of-order segments** are discarded (simplified model)

This mechanism allows TCP to recover from packet loss without restarting the entire transmission.

---

## 10. Real-World Behavior

In real TCP implementations:

- Fast retransmit occurs after 3 duplicate ACKs
- Out-of-order segments may be buffered (not discarded)
- Congestion control also affects transmission rate

---

## 11. Reflection

This exercise shows how TCP provides reliable communication over an unreliable network.

Instead of preventing errors, TCP detects and corrects them through acknowledgments and retransmissions.

The combination of sequence numbers, ACKs, and timers makes TCP robust and efficient, enabling reliable data transfer in the Internet.