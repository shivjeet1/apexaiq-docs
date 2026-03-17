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
