---
layout: default
title: Parallel Fraud Detection Simulator
---

## Parallel Fraud Detection Simulator

### Description

- Transaction batches arrive simultaneously from payment gateways.
- Detect suspicious transactions, avoid duplicates, maintain per-user risk scores, and process
batches concurrently.
- Expected Output:
    ```bash
    
    Fraud Detection Report
    Users Flagged: 3
    Suspicious Transactions: 11
    Highest Risk User: user_27
    ```

### Implementation

- Clone the repository

  ```bash
  git clone https://github.com/shivjeet1/apexaiq-docs.git
  ```

- Navigate to the project directory

  ```bash
  cd apexaiq-docs/content/sem6/week2/code
  ```
  
- Run the program

  ```bash
  python fraud.py
  ```

---

##        OR

---

- Edit the transactions.json :
  ```bash
  nano transactions.json
  ```
    
- Run the program

  ```bash
  python detect.py
  ```

> This program is a modified version of the [Parallel Fraud Detection Simulator](https://github.com/shivjeet1/apexaiq-docs/blob/master/content/sem6/week2/code/detect.py).
> This is used to detect fraud in a parallel environment.
> This program implements the following :
  - OOPs
  - Multithreading
  - Locks
  - Conditions

