# TCP Congestion Control 

## 1. Introduction

TCP congestion control allows the sender to adjust its sending rate based on network conditions.

It uses the congestion window (cwnd) and mechanisms such as Slow Start, Congestion Avoidance, and multiplicative decrease.

---

## 2. Problem Scenario

Initial conditions:

- cwnd = 1 MSS
- ssthresh = 16 MSS

Events:

- RTT 1–4: normal transmission  
- RTT 7: 3 duplicate ACKs  
- RTT 10: timeout  

---

## 3. cwnd Evolution

| RTT | cwnd | Phase                  |
|-----|------|------------------------|
| 1   | 2    | Slow Start             |
| 2   | 4    | Slow Start             |
| 3   | 8    | Slow Start             |
| 4   | 16   | Slow Start → CA        |
| 5   | 17   | Congestion Avoidance   |
| 6   | 18   | Congestion Avoidance   |
| 7   | 9    | Fast Recovery          |
| 8   | 10   | Congestion Avoidance   |
| 9   | 11   | Congestion Avoidance   |
| 10  | 1    | Timeout → Slow Start   |

---

## 4. Graphical Representation

cwnd over time (RTT):

```
cwnd
20 |                         *
18 |                       *   *
16 |                     *
14 |
12 |                   *
10 |                 *
 8 |              *
 6 |
 4 |           *
 2 |        *
 1 |     *
   --------------------------------
     1  2  3  4  5  6  7  8  9  10   RTT
```

### Interpretation:

- Exponential growth (RTT 1–4)
- Linear growth (RTT 5–6)
- Drop due to duplicate ACKs (RTT 7)
- Linear again (RTT 8–9)
- Sharp drop due to timeout (RTT 10)

---

## 5. Key Mechanisms

### Slow Start
- cwnd doubles every RTT
- Fast bandwidth discovery

### Congestion Avoidance
- cwnd increases linearly
- Prevents congestion

### Fast Recovery (3 duplicate ACKs)
- cwnd is reduced by half
- Transmission continues

### Timeout
- cwnd reset to 1
- Indicates severe congestion

---

## 6. Analysis

TCP follows the principle:

**“Increase quickly, decrease aggressively”**

- Efficient use of bandwidth
- Quick reaction to congestion
- Fair sharing between flows

Duplicate ACKs indicate **mild congestion**, while timeouts indicate **severe congestion**.

---

## 7. Python Visualization

For a more advanced version, you can generate a graph:

```python
import matplotlib.pyplot as plt

rtt = list(range(1, 11))
cwnd = [2, 4, 8, 16, 17, 18, 9, 10, 11, 1]

plt.plot(rtt, cwnd, marker='o')
plt.xlabel("RTT")
plt.ylabel("cwnd (MSS)")
plt.title("TCP Congestion Window Evolution")
plt.grid()

plt.show()
```

---

## 8. Reflection

This assignment demonstrates how TCP dynamically adapts to network conditions.

The evolution of cwnd shows the balance between performance and stability. TCP aggressively increases throughput when possible, but quickly reduces it when congestion is detected.

Understanding this behavior is essential for analyzing real-world network performance.