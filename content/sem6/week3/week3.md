---
title: "Week 3 : JavaScript Theory Notes (ApexaiQ Internship)"
draft: false
layout: default
---

# JavaScript Theory Notes

This document explains all concepts used in the practical programs in simple terms.

---

## 1. Variables

Variables are used to store data.

There are 3 ways to declare variables:

- `var` → old way, function scoped  
- `let` → block scoped (recommended)  
- `const` → block scoped, value cannot change  

### Key Points:
- Use `let` when value can change  
- Use `const` when value should not change  
- Avoid `var` in modern code  

---

## 2. Datatypes

Datatypes define what kind of value a variable holds.

### Primitive Types:
- String → text (`"hello"`)
- Number → numeric values (`10`)
- Boolean → true/false
- Undefined → variable declared but not assigned
- Null → empty value

### Non-Primitive:
- Object → key-value pairs
- Array → list of values

### Key Points:
- `typeof` is used to check datatype  
- Arrays and objects are reference types  

---

## 3. Loops

Loops are used to repeat code.

### Types of Loops:

- `for` → used when count is known  
- `while` → runs while condition is true  
- `do...while` → runs at least once  
- `for...of` → loops through array values  
- `for...in` → loops through object keys  

### Key Points:
- Avoid infinite loops  
- Use `for...of` for arrays  
- Use `for...in` for objects  

---

## 4. Functions

Functions are reusable blocks of code.

### Types:

- Normal Function → basic function  
- Function Expression → stored in variable  
- Arrow Function → shorter syntax  
- Callback Function → passed as argument  
- Default Parameters → fallback values  

### Key Points:
- Functions improve reusability  
- Arrow functions do not have their own `this`  
- Callbacks are used in async operations  

---

## 5. Arrays

Arrays store multiple values in a single variable.

### Common Properties:
- `length` → number of elements  

### Common Methods:
- Add/Remove → `push`, `pop`, `shift`, `unshift`  
- Search → `includes`, `indexOf`, `find`  
- Transform → `map`, `filter`, `reduce`  
- Utility → `join`, `slice`, `splice`  

### Key Points:
- Arrays are zero-indexed  
- `map` returns new array  
- `filter` returns matching elements  
- `reduce` gives single value  

---

## 6. Objects

Objects store data in key-value pairs.

### Features:
- Access using dot (`obj.key`) or bracket (`obj["key"]`)  
- Can store functions (methods)  

### Common Methods:
- `Object.keys()` → returns keys  
- `Object.values()` → returns values  
- `Object.entries()` → key-value pairs  
- `Object.assign()` → copy object  
- `Object.freeze()` → make object immutable  

### Key Points:
- Objects are reference types  
- `this` refers to current object  
- Properties can be added or removed anytime  

---

## 7. DOM & Event Handling

DOM = Document Object Model  
It represents HTML as a tree structure.

### Common Methods:
- `getElementById()`  
- `querySelector()`  

### Events:
- click  
- input  
- submit  

### Event Handling:
- Use `addEventListener()`  
- Takes event type + callback function  

### Key Points:
- DOM allows JS to change HTML  
- Events make pages interactive  
- Callback runs when event happens  

---

## 8. Promises

Promises handle asynchronous operations.

### States:
- Pending → initial state  
- Resolved → success  
- Rejected → error  

### Methods:
- `.then()` → runs on success  
- `.catch()` → runs on error  

### Key Points:
- Avoid callback hell  
- Promises make async code cleaner  

---

## 9. Async & Await

Built on top of promises.

### How it works:
- `async` makes function return a promise  
- `await` pauses execution until promise resolves  

### Key Points:
- Makes async code look like sync  
- Must be used inside async function  
- Use try/catch for error handling  

---

## 10. Event Loop (Research)

JavaScript runs on a single thread.

### Components:
- Call Stack → executes code  
- Web APIs → handles async tasks  
- Callback Queue → stores completed tasks  
- Event Loop → manages execution order  

### Flow:
1. Code goes to call stack  
2. Async tasks go to Web APIs  
3. Completed tasks go to queue  
4. Event loop pushes them back to stack  

### Key Points:
- Explains why async code runs later  
- Even `setTimeout(0)` is not immediate  

---



