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
