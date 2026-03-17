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
