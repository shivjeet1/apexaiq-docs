---
layout: default
title: Week 2
---

# Week 2 - Introduction to Python
## Learning Objectives

- Learn the basics of Python
- Learn the basics of the Python REPL
- Learn the basics of Python syntax
- Learn the basics of functions
- Learn the basics of loops

## Introduction to Python

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













