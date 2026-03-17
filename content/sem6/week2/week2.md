---
layout: default
title: Week 2
---

# Week 2 - Session 1 - Introduction to Python

## Learning Objectives

- Learn the basics of Python
- Learn the basics of the Python REPL
- Learn the basics of Python syntax
- Learn the basics of functions
- Learn the basics of loops

### Introduction to Python

Python is a general purpose programming language. It is a high level language that is easy to learn and use. It is also a good language for beginners to learn because it is simple and easy to understand.

### 1. Concurrency vs. Parallelism

In this program, we use **Concurrency** to manage the lifecycle of different transaction batches and **Parallelism** to process them simultaneously.

* **Concurrency:** This is the *art of juggling*. The program schedules multiple batches to be processed. Even if one batch is waiting for a resource, the program moves on to start the next one.
* **Parallelism:** This is the *art of multitasking*. If your computer has 4 CPU cores, the `ThreadPoolExecutor` can theoretically run 4 different batch checks at the exact same millisecond.

### 2. Thread Safety and Mutual Exclusion (The Lock)

When multiple threads work on the same data (like the `user_scores` dictionary), they can cause a **Race Condition**.

* **The Problem:** Two threads read `user_27`'s score as `5` at the same time. Both add `1` and try to write `6`. The score becomes `6` instead of `7`.
* **The Concept (Locking):** We use a `threading.Lock()`. This acts like a "talking stick." Only the thread holding the lock is allowed to update the dictionary. Others must wait in line. This ensures **Data Integrity**.

### 3. Object-Oriented Programming (OOPS)

Even in the simplified version, the logic follows OOP principles to make the code maintainable.

* **Encapsulation:** We wrap the data (transactions) and the logic (risk checking) into distinct units. In the professional version, the `RiskEngine` "hides" its internal mechanics from the rest of the program.
* **Abstraction:** The user only sees the `run()` method. They don't need to know how the threads are being managed or how the lock is being acquired; they just want the report.

### 4. Idempotency and Deduplication

In financial systems, "Idempotency" means that performing an operation multiple times has the same effect as performing it once.

* **Deduplication:** By using a `set()` for `processed_ids`, we ensure that if a payment gateway sends "Transaction_ABC" five times, our simulator only counts it once.
* **Set Lookup Complexity:** We use a `set` instead of a `list` because searching a set is $O(1)$ (instant), whereas searching a list is $O(n)$ (slows down as the list grows). This is vital for high-speed fraud detection.

### 5. The Producer-Consumer Pattern

The "Gateways" act as **Producers** (creating data), and our "RiskEngine" acts as a **Consumer** (processing data).

* In industry, this is often handled by a **Message Queue** (like RabbitMQ or Kafka).
* In our Python code, the `ThreadPoolExecutor` acts as the queue manager, handing tasks to available worker threads as soon as they become free.

### Summary Table for Quick Reference

| Concept | Purpose in this Program |
| --- | --- |
| **ThreadPoolExecutor** | Manages a pool of workers to process batches simultaneously. |
| **threading.Lock** | Prevents "Race Conditions" where two threads overwrite the same data. |
| **Dictionary (Hash Map)** | Stores user risk scores for $O(1)$ access speed. |
| **Set** | Tracks unique transaction IDs to avoid duplicate fraud counts. |
| **Futures** | Objects that represent a result that hasn't happened yet but will soon. |

---



# Week 2 - Session 2 - REST APIs

## Comprehensive Guide to REST APIs and Modern API Architecture

Today we are going to look into a complete guide covering the fundamentals of APIs, architectural paradigms, and best practices. Below is the detailed breakdown of all the key topics.

### 1. REST API Definition

  REST API stands for Representational State Transfer Application Programming Interface. First defined by Dr. Roy Fielding, REST is a widely adopted architectural style used to build lightweight, flexible, and scalable web services that facilitate data exchange between applications over the internet.

### 2. Stateless APIs and Scalability

  One of the core ideas behind REST is Statelessness. Stateless APIs mandate that every single request from the client to the server must contain all the necessary information to understand and process that request. The server does not store any session state or history about the client between requests. This principle makes the API highly scalable, as any server in a cluster can seamlessly handle any request without needing to sync session data.

### 3. The 6 Guiding Principles of REST

  To be considered truly RESTful, an API must adhere to these six guiding principles:

  1. **Uniform Interface:** The architecture standardizes how information is identified and transmitted, keeping the interactions consistent and simple.
  2. **Client-Server Decoupling:** The client application and server application must evolve completely independently. The client only needs to know the resource URIs.
  3. **Stateless:** As discussed, no client context is stored on the server side.
  4. **Cacheable:** Responses must explicitly define whether they can be cached or not. Caching drastically improves performance and reduces server load.
  5. **Layered System:** The API can run on multiple hierarchical servers (e.g., load balancers, proxies, databases) to ensure security and efficiency, without the client ever knowing.
  6. **Code on Demand (Optional):** The server can occasionally extend the client's functionality by sending executable code (like JavaScript).

### 4. HTTP Methods & CRUD Operations

HTTP methods natively map to standard CRUD (Create, Read, Update, Delete) database operations:

* **POST (Create):** Used to submit new data and create a new resource on the server.
* **GET (Read):** Used to retrieve information or fetch a resource.
* **PUT / PATCH (Update):** Used to update existing resources. PUT typically replaces the entire resource, while PATCH modifies it partially.
* **DELETE (Delete):** Used to remove a resource from the server.

### 5. Data Formats (JSON vs XML)

While APIs can return data in various formats like XML or HTML, **JSON (JavaScript Object Notation)** is the industry standard today. JSON is highly preferred because it is lightweight, concise, and natively supported by JavaScript, making parsing 2 to 3 times faster compared to XML. XML is more verbose and tag-heavy, usually reserved for legacy enterprise systems or SOAP integrations.

### 6. Hypermedia Links (HATEOAS)

HATEOAS stands for Hypermedia as the Engine of Application State. It means that an API response should include hypermedia links (usually within a `_links` object) that guide the client on what actions can be taken next. Instead of hardcoding URLs on the frontend, the client traverses these dynamic links returned by the server, making the API self-documenting and highly discoverable.

### 7. RESTful URL Structure

When designing endpoints, it is important to follow specific naming conventions:

* **Nouns over Verbs:** Use nouns to represent resources, not verbs. Let the HTTP method handle the action. For example, use `/users` instead of `/getUsers`.
* **Pluralization:** Always use plural nouns for collection URIs to maintain consistency (e.g., `/items` is correct, `/item` is wrong).
* **Logical Nesting:** Show hierarchical relationships simply (e.g., `/users/{userId}/orders`).

### 8. HTTP Status Codes

Status codes let the client know the result of their request. Below are the main types:

* **1xx (Informational):** The request was received, and the process is continuing (e.g., `100 Continue`).
* **2xx (Successful):** The request was successfully accepted.
* *Example:* `200 OK`, `201 Created`.


* **3xx (Redirection):** Further action is required by the client to complete the request.
* *Example:* `301 Moved Permanently`.


* **4xx (Client Error):** The request contains bad syntax or cannot be fulfilled due to client-side issues.
* *Example:* `400 Bad Request`, `401 Unauthorized`, `403 Forbidden`, `404 Not Found`, `429 Too Many Requests`.


* **5xx (Server Error):** The server failed to process a seemingly valid request.
* *Example:* `500 Internal Server Error`, `502 Bad Gateway`, `503 Service Unavailable`, `504 Gateway Timeout`.



### 9. Error Handling

APIs must handle errors gracefully. Instead of throwing raw stack traces, a standard REST API should return an appropriate 4xx or 5xx status code alongside a structured JSON payload containing a clear, human-readable error message and standard error codes to help developers debug the issue efficiently.

### 10. REST vs GraphQL vs gRPC

Below is a comparison of modern API architectural styles to select an appropriate protocol:

| Criteria | REST | GraphQL | gRPC |
| --- | --- | --- | --- |
| **Data Retrieval** | Can suffer from over-fetching or under-fetching. | Client queries exactly the specific data they need. | Highly structured method calls. |
| **Payload/Format** | Text-based (JSON/XML). | Text-based (JSON). | Binary protocol (Protocol Buffers). |
| **Performance** | Moderate; slightly slower. | Moderate. | Blazing fast; very low latency. |
| **Primary Use Case** | Standard web applications, public interfaces. | Complex UIs and data-heavy applications. | Internal microservices and real-time systems. |

### 11. API Authentication Methods

Authentication is the process of verifying user identity. The most common methods include:

* **Basic Auth:** Sends the username and password in the HTTP headers using Base64 encoding. It is very simple but should strictly be used over HTTPS.
* **API Keys:** A unique string identifier assigned to users, usually passed in the request header. Best for internal services or simple B2B integrations.
* **JWT (JSON Web Token):** A stateless, self-contained token mechanism widely used in modern web apps and microservices.
* **OAuth 2.0:** A highly secure framework used for third-party integrations (like "Sign in with Google"), allowing access to resources without sharing actual passwords.

### 12. API Rate-Limiting Algorithms

Rate limiting restricts the number of API calls a user can make within a specific time window to prevent system overload and DoS attacks. Below are the standard algorithms:

* **Fixed Window Counter:** Counts requests in fixed time blocks (e.g., 1 minute). Simple, but vulnerable to spikes at the window boundaries.
* **Sliding Window Log/Counter:** Tracks precise timestamps or averages out time blocks to avoid the boundary spike issue, offering smoother traffic control.
* **Leaky Bucket:** Places requests in a queue and processes them at a constant, even rate, smoothing out burst traffic.
* **Token Bucket:** One of the most popular algorithms. Tokens are added to a bucket at a set rate. Each incoming request consumes a token, making it ideal for safely handling sudden bursts.

### 13. API Versioning Strategies

Versioning ensures that updates to your backend do not break existing client applications. Takeaway pointers for versioning include:

* **URI Path Versioning:** Adding the version directly in the URL (e.g., `https://api.example.com/v1/users`). This is the easiest to implement and spot.
* **Query Parameter Versioning:** Passing the version as a query parameter (e.g., `/users?version=v1`).
* **Header Versioning:** Sending the version explicitly inside a custom HTTP request header. This keeps the URIs clean but makes caching slightly more complex.
* **Media Type (Content Negotiation):** Passing the version inside the standard `Accept` header.

### 14. API Security Best Practices

Securing your API is a critical step. Following the OWASP (Open Worldwide Application Security Project) API Security guidelines, here are essential best practices:

* **Enforce TLS/HTTPS:** Always encrypt data in transit across all endpoints to prevent eavesdropping.
* **Strict Authorization:** Ensure proper function-level and object-level authorization (BOLA) to prevent unauthorized users from accessing data they shouldn't see.
* **Implement Rate Limiting:** Actively prevent brute-force attacks and abuse of unrestricted resource consumption.
* **Input Validation:** Reject malformed data to protect against SQL and Command Injection attacks.
* **Security Misconfiguration:** Disable default settings, do not expose debug stack traces, and manage your API inventory properly to shut down unmonitored "zombie" APIs.











