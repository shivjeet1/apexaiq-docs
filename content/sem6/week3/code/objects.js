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
