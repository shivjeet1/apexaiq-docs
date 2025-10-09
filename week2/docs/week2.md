---
layout: default
title: "WEEK2 Documentation"
# Python Documentation
---

## Python Concepts

### Syntax, Variables & Datatypes
-   **Syntax**: The rules of the language. Get it right, or the code won't run.
-   **Variables**: Named containers for storing data. `name = "value"`.
-   **Datatypes**: The type of data you're storing.
    -   `int`: Whole numbers. `10`, `-50`.
    -   `float`: Decimal numbers. `3.14`, `-0.5`.
    -   `string`: Text, wrapped in quotes. `"Hello"`, `'World'`.
    -   `list`: Ordered, changeable collection of items. `[1, "apple", 3.0]`.
    -   `tuple`: Ordered, unchangeable collection. `(1, "apple", 3.0)`.
    -   `dict`: Unordered collection of key-value pairs. `{"key": "value", "id": 123}`.
    -   `set`: Unordered collection of unique items. `{1, 2, 3}`.

### List/Dictionary Comprehension
-   **Purpose**: A short, elegant syntax for creating a list or dictionary from an existing iterable.
-   **Syntax**:
    ```python
    # List comprehension
    squares = [x*x for x in range(10)]
    # Dictionary comprehension
    square_dict = {x: x*x for x in range(10)}
    ```

### Conditional Statements (if-elif-else)
-   **Purpose**: Make decisions in your code. "If this is true, do this; otherwise, do that."
-   **Syntax**:
    ```python
    if condition:
        # run this code
    elif another_condition:
        # run this instead
    else:
        # run if nothing above was true
    ```

### Loops (for, while)
-   **Purpose**: Repeat a block of code.
-   **`for` loop**: Iterates over a sequence (like a list or string).
    ```python
    for item in my_list:
        print(item)
    ```
-   **`while` loop**: Repeats as long as a condition is true.
    ```python
    count = 0
    while count < 5:
        print(count)
        count += 1
    ```
-   **`break`**: Immediately exit the current loop.
-   **`continue`**: Skip the rest of the current iteration and move to the next.

### Iterators & Generators
-   **Iterator**: An object that allows you to traverse a container one element at a time.
-   **Generator**: A simpler way to create iterators using a function with the `yield` keyword. It produces items one by one, saving memory.

### Functions
-   **Purpose**: A named, reusable block of code that performs a specific task.
-   **Syntax**:
    ```python
    def function_name(parameter1, default_param="default"):
        # code to execute
        return "some value"
    ```
-   **`*args`**: Collects extra positional arguments into a tuple.
-   **`**kwargs`**: Collects extra keyword arguments into a dictionary.

### Decorators
-   **Purpose**: A function that takes another function as input, adds functionality to it, and returns the modified function.
-   **Syntax**: The `@` symbol is syntactic sugar for wrapping a function.
    ```python
    @my_decorator
    def say_hello():
        print("Hello!")
    ```

### Object Oriented Programming
   - **Purpose**: A paradigm to structure code around "objects" (data and functions) instead of just functions and logic.
   - **`class`**: A blueprint for creating objects.
   - **`object`**: An instance of a class.
   - **Pillars of OOP**:
     - Abstraction
     - Class
     - Encapsulation
     - Inheritance
     - Object
     - Polymorphism

### Exception Handling
-   **Purpose**: Manage errors without crashing the program.
-   **Syntax**:
    ```python
    try:
        # code that might fail
        risky_operation()
    except ValueError as e:
        # run if a ValueError occurs
        print(f"Error caught: {e}")
    finally:
        # this code always runs, error or not
        cleanup()
    ```

### Packages
   A package is a collection of Python modules organized in directories with an ```__init__.py``` file.
   It helps in code organization, reusability and modularity.
   - **Built-in Packages:** Already available. eg. `os, sys, math, datetime`.
   - **Third Party Packages:** Created by community, installed via `pip`. eg. `requests, numpy, pandas, flask`
   - **User-Defined packages:** Custom packages created for a project. eg. our own folder with `__init__.py` and multiple `.py` files.

---

## Virtual Environment
   1. Create a Virtual Environment:
    ```bash
    python -m venv <NameYourVenv>
    ```
   2. Activate Virtual Environment:
    ```bash
    source <NameYourVenv>/bin/activate 
    ```
   3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Coding Standards

-   **Naming Convention**: Write clean, readable names. `snake_case` for variables and functions, `PascalCase` for classes.
-   **Docstring**: Explain the *purpose* of a function, module, or class. Use `"""Triple quotes"""` right after the definition.
-   **Comments**: Explain the *how* or the *why* for complex or non-obvious lines of code. Use `#`.
-   **Types of Testing**:
    -   **Unit Test**: Tests a single component or function in isolation.
    -   **Integration Test**: Tests how multiple components work together.
    -   **End-to-End Test**: Tests the entire application flow from start to finish.
-   **PEP8**: Python's official style guide. Follow it for consistent, readable code.
-   **SOLID & DRY**:
    -   **DRY (Don't Repeat Yourself)**: Every piece of knowledge must have a single, unambiguous representation within a system. Avoid copy-pasting code.
    -   **SOLID**: Five design principles for creating understandable, flexible, and maintainable software.

---

## API [Application Programming Interface]

-   **API**: A contract that allows two separate software systems to communicate and exchange data.
-   **Types of APIs**: Different architectural styles. Common ones include **REST**, **SOAP**, and **GraphQL**.
-   **HTTP Status Codes**: Server responses indicating the result of a request.
    -   `2xx` (e.g., `200 OK`): Success.
    -   `4xx` (e.g., `404 Not Found`): Client-side error. You did something wrong.
    -   `5xx` (e.g., `500 Internal Server Error`): Server-side error. They did something wrong.
-   **Response Formats**: The data structure of the response. **JSON** is the modern standard.
-   **Types of API Authentication**: Methods to prove identity. Common types are **API Keys**, **OAuth 2.0**, and **JWT (JSON Web Tokens)**.
-   **Versioning**: A way to manage changes to an API without breaking existing client applications (e.g., `/api/v1/...`).
-   **CRUD Operations**: The four fundamental functions of persistent storage.
    -   **C**reate -> `POST`
    -   **R**ead -> `GET`
    -   **U**pdate -> `PUT` / `PATCH`
    -   **D**elete -> `DELETE`
-   **Optimization**: Techniques to improve API performance, like **caching**, **rate limiting**, and **payload compression**.
-   **`requests` Library**: The standard Python library for making HTTP requests to APIs.

---

## Extra Topics

-   **SDLC (Software Development Life Cycle)**: A framework defining the process for building and maintaining software, from initial planning to final decommissioning. Steps include Planning, Design, Development, Testing, Deployment, and Maintenance.
-   **Agile Basics**: An iterative approach to project management and software development that helps teams deliver value faster and with fewer headaches.
-   **Version Control (Git)**: A system that records changes to a file or set of files over time so that you can recall specific versions later. Essential for collaboration and sanity.
-   **Software Architecture**: The high-level structure of a software system and the discipline of creating such structures. It's the blueprint for the system. Types: Monolithic, Microservices, Layered(N-tier), Event Driven and Service Oriented.

