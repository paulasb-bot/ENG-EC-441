# Application Layer – Web, HTTP, Streaming and CDNs

## 1. Introduction

The Application Layer provides network services directly to end users. It includes protocols such as HTTP, DNS, SMTP, and others.

Among these, HTTP (HyperText Transfer Protocol) is the foundation of the Web, enabling communication between clients (browsers) and servers.

Modern web systems also rely on content distribution techniques such as CDNs and adaptive video streaming to achieve scalability and performance.

---

## 2. Client-Server Model

Web applications follow a client-server architecture:

- Client (browser) sends requests
- Server responds with resources (HTML, images, video)

Example:

User → Browser → HTTP Request → Server → HTTP Response → Browser → Render page

---

## 3. HTTP Protocol Basics

HTTP is:

- Stateless
- Request-response based
- Runs on top of TCP

### HTTP Request Structure

Example:

```
GET /index.html HTTP/1.1
Host: example.com
User-Agent: Mozilla/5.0
```

### HTTP Response Structure

```
HTTP/1.1 200 OK
Content-Type: text/html

<html>...</html>
```

---

## 4. Persistent vs Non-Persistent HTTP

### Non-Persistent HTTP

- One TCP connection per object
- High overhead (multiple RTTs)

### Persistent HTTP

- Single connection reused
- Lower latency
- Default in HTTP/1.1

---

## 5. Problem – Web Page Download Time

Assume:

- RTT = 100 ms  
- HTML file + 3 images  
- Non-persistent HTTP  

### Step-by-step:

1. TCP handshake → 1 RTT  
2. Request + response → 1 RTT  

Each object = 2 RTT

Total objects = 4

Total time:

4 × 2 RTT = 8 RTT = 800 ms

---

### With Persistent HTTP

- 1 handshake = 1 RTT  
- All objects requested over same connection  

Total:

≈ 1 RTT + 4 RTT = 5 RTT = 500 ms

---

## 6. Web Caching

Caches store copies of resources closer to the client.

Benefits:

- Reduced latency
- Reduced server load
- Reduced bandwidth usage

---

## 7. Content Distribution Networks (CDNs)

CDNs replicate content across geographically distributed servers.

Two main approaches:

### 7.1 Enter Deep

- Servers placed inside ISPs
- Close to users

### 7.2 Bring Home

- Large data centers
- Redirect users to nearest node

Examples:

- Akamai
- Cloudflare
- Amazon CloudFront

---

## 8. Video Streaming

Video traffic dominates Internet usage.

Challenges:

- Large file sizes
- Variable bandwidth
- Buffering issues

---

## 9. Adaptive Streaming (DASH)

DASH = Dynamic Adaptive Streaming over HTTP

Key idea:

- Video divided into chunks
- Each chunk encoded at multiple bitrates
- Client selects quality dynamically

---

### How it works:

1. Client measures available bandwidth  
2. Requests appropriate quality chunk  
3. Adjusts in real time  

---

## 10. Example Scenario

User starts watching a video:

- High bandwidth → HD quality  
- Network congestion → switch to lower quality  

This avoids buffering.

---

## 11. Analysis

Modern web performance depends on:

- RTT (latency)
- Number of objects
- Connection reuse
- CDN placement
- Adaptive streaming

Key insights:

- Persistent connections reduce delay
- CDNs reduce physical distance
- DASH improves user experience under varying conditions

---

## 12. Real-World Impact

Technologies described are used by:

- Netflix → adaptive streaming  
- YouTube → DASH  
- Cloudflare → CDN  
- Google → QUIC + HTTP/3  

---

## 13. Reflection

This topic shows how application-layer protocols must be designed not only for correctness, but also for scalability and performance.

The combination of HTTP, CDNs, and adaptive streaming allows modern applications to deliver large-scale content efficiently across the globe.

Understanding these mechanisms is essential to analyze how real-world Internet services operate.