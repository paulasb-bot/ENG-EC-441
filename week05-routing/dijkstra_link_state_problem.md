# Routing with Link State – Dijkstra’s Algorithm

## 1. Introduction

Routing is a fundamental function of the Network layer. It determines the best path for data to travel from a source to a destination across a network.

Link State routing protocols (such as OSPF) use a global view of the network and compute shortest paths using Dijkstra’s algorithm.

---

## 2. Problem Statement

Consider the following network graph:

Nodes: A, B, C, D, E

Edges with costs:

- A–B: 2  
- A–C: 5  
- B–C: 1  
- B–D: 2  
- C–D: 3  
- C–E: 1  
- D–E: 2  

Task:

Use Dijkstra’s algorithm to compute the shortest path from node A to all other nodes.

---

## 3. Step 1 – Initialization

Start from node A.

| Node | Distance | Previous |
|------|----------|----------|
| A    | 0        | —        |
| B    | ∞        | —        |
| C    | ∞        | —        |
| D    | ∞        | —        |
| E    | ∞        | —        |

Visited set: {}

---

## 4. Step 2 – Visit A

From A:

- A → B = 2  
- A → C = 5  

Update:

| Node | Distance | Previous |
|------|----------|----------|
| A    | 0        | —        |
| B    | 2        | A        |
| C    | 5        | A        |
| D    | ∞        | —        |
| E    | ∞        | —        |

Visited: {A}

---

## 5. Step 3 – Visit B (smallest distance = 2)

From B:

- B → C = 2 + 1 = 3 (better than 5 → update)  
- B → D = 2 + 2 = 4  

Update:

| Node | Distance | Previous |
|------|----------|----------|
| A    | 0        | —        |
| B    | 2        | A        |
| C    | 3        | B        |
| D    | 4        | B        |
| E    | ∞        | —        |

Visited: {A, B}

---

## 6. Step 4 – Visit C (distance = 3)

From C:

- C → D = 3 + 3 = 6 (no improvement over 4)  
- C → E = 3 + 1 = 4  

Update:

| Node | Distance | Previous |
|------|----------|----------|
| A    | 0        | —        |
| B    | 2        | A        |
| C    | 3        | B        |
| D    | 4        | B        |
| E    | 4        | C        |

Visited: {A, B, C}

---

## 7. Step 5 – Visit D (distance = 4)

From D:

- D → E = 4 + 2 = 6 (no improvement over 4)

No changes.

Visited: {A, B, C, D}

---

## 8. Step 6 – Visit E

No further updates.

Visited: {A, B, C, D, E}

---

## 9. Final Shortest Paths

| Destination | Cost | Path        |
|------------|------|-------------|
| A          | 0    | A           |
| B          | 2    | A → B       |
| C          | 3    | A → B → C   |
| D          | 4    | A → B → D   |
| E          | 4    | A → B → C → E |

---

## 10. Shortest Path Tree

The resulting shortest path tree from A includes:

- A → B  
- B → C  
- B → D  
- C → E  

---

## 11. Analysis

Dijkstra’s algorithm works by iteratively selecting the node with the smallest tentative distance and updating its neighbors.

This ensures that once a node is visited, its shortest path is finalized.

Link State protocols rely on this algorithm after building a complete map of the network.

---

## 12. Reflection

This exercise demonstrates how routing decisions are computed systematically rather than guessed.

Dijkstra’s algorithm guarantees optimal paths in networks with non-negative edge weights, making it suitable for real-world routing protocols such as OSPF.

Understanding this process is essential for analyzing how routers make forwarding decisions in large-scale networks.