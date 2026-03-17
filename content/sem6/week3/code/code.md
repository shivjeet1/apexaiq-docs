---
layout: default
title: "JavaScript Practical Programs"
---

# JavaScript Practical Program

This document contains simple and practical examples for core JavaScript concepts.

## 1. Variables

```js
var name = "shivjeet";      // function scoped
let age = 21;           // block scoped
const country = "India"; // cannot be reassigned

console.log(name, age, country);
````

---

## 2. Datatypes

```js
let str = "Hello";          // String
let num = 10;              // Number
let isTrue = true;         // Boolean
let arr = [1, 2, 3];       // Array (Object)
let obj = { key: "value" };// Object
let und;                   // Undefined
let empty = null;          // Null

console.log(typeof str, typeof num, typeof isTrue);
```

---

## 3. Loops

```js
// for loop
for (let i = 0; i < 3; i++) {
  console.log("for:", i);
}

// while loop
let i = 0;
while (i < 3) {
  console.log("while:", i);
  i++;
}

// do...while
let j = 0;
do {
  console.log("do-while:", j);
  j++;
} while (j < 3);

// for...of (arrays)
let nums = [10, 20, 30];
for (let n of nums) {
  console.log("for-of:", n);
}

// for...in (objects)
let obj = { a: 1, b: 2 };
for (let key in obj) {
  console.log("for-in:", key, obj[key]);
}
```

---

## 4. Functions

```js
// normal function
function add(a, b) {
  return a + b;
}

// function expression
const sub = function(a, b) {
  return a - b;
};

// arrow function
const mul = (a, b) => a * b;

// default params
function greet(name = "User") {
  return "Hello " + name;
}

// callback function
function process(num, callback) {
  return callback(num);
}

console.log(add(2,3));
console.log(sub(5,2));
console.log(mul(3,4));
console.log(greet());
console.log(process(5, (n) => n * 2));
```

---

## 5. Arrays (Methods & Properties)

```js
let arr = [1, 2, 3];

// properties
console.log(arr.length);

// add/remove
arr.push(4);
arr.pop();
arr.unshift(0);
arr.shift();

// methods
console.log(arr.includes(2));
console.log(arr.indexOf(3));
console.log(arr.join("-"));

// map
let doubled = arr.map(x => x * 2);

// filter
let filtered = arr.filter(x => x > 1);

// reduce
let sum = arr.reduce((acc, val) => acc + val, 0);

// find
let found = arr.find(x => x === 2);

// slice & splice
let sliced = arr.slice(1, 2);
arr.splice(1, 1);

console.log(doubled, filtered, sum, found, sliced);
```

---

## 6. Object (Methods & Properties)

```js
let user = {
  name: "shivjeet",
  age: 21,
  greet() {
    return "Hello " + this.name;
  }
};

// access
console.log(user.name);
console.log(user["age"]);

// add/update
user.city = "Shegaon";
user.age = 22;

// delete
delete user.city;

// methods
console.log(Object.keys(user));
console.log(Object.values(user));
console.log(Object.entries(user));

// assign
let newUser = Object.assign({}, user);

// freeze
Object.freeze(user);

console.log(user.greet());
```

---

## 7. DOM & Event Handling (Callback)

```html
<button id="btn">Click Me</button>

<script>
  const btn = document.getElementById("btn");

  btn.addEventListener("click", function() {
    console.log("Button clicked");
  });
</script>
```

---

## 8. Promises

```js
let promise = new Promise((resolve, reject) => {
  let success = true;

  if (success) {
    resolve("Success");
  } else {
    reject("Error");
  }
});

promise
  .then(res => console.log(res))
  .catch(err => console.log(err));
```

---

## 9. Async & Await

```js
function fetchData() {
  return new Promise(resolve => {
    setTimeout(() => resolve("Data received"), 1000);
  });
}

async function getData() {
  let data = await fetchData();
  console.log(data);
}

getData();
```

---

## 10. Event Loop (Research Only)

Simple explanation:

* JavaScript is single-threaded.
* It uses **Call Stack**, **Web APIs**, and **Callback Queue**.
* Tasks like `setTimeout` go to Web APIs.
* After execution, they go to queue.
* Event loop checks stack and pushes tasks.

Example:

```js
console.log("Start");

setTimeout(() => {
  console.log("Timeout");
}, 0);

console.log("End");
```

Output:

```
Start
End
Timeout
```

Reason: Event loop handles async tasks after main execution.

---




