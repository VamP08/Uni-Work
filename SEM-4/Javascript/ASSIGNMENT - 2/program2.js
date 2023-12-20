// Arithmetic Operators
let a = 10;
let b = 5;
console.log("Arithmetic Operators:");
console.log("Addition:", a + b);        // Output: 15
console.log("Subtraction:", a - b);     // Output: 5
console.log("Multiplication:", a * b);  // Output: 50
console.log("Division:", a / b);        // Output: 2
console.log("Modulus:", a % b);         // Output: 0
console.log("Increment:", a++);         // Output: 10 (post-increment)
console.log("Decrement:", b--);         // Output: 5 (post-decrement)

// Comparison Operators
let x = 5;
let y = "5";
console.log("Comparison Operators:");
console.log("Equal (==):", x == y);      // Output: true
console.log("Strict Equal (===):", x === y); // Output: false
console.log("Not Equal (!=):", x != y);  // Output: false
console.log("Strict Not Equal (!==):", x !== y); // Output: true
console.log("Greater Than (>):", a > b); // Output: true
console.log("Less Than (<):", a < b);    // Output: false
console.log("Greater Than or Equal (>=):", a >= b); // Output: true
console.log("Less Than or Equal (<=):", a <= b);    // Output: false

// Logical Operators
let p = true;
let q = false;
console.log("Logical Operators:");
console.log("Logical AND (&&):", p && q); // Output: false
console.log("Logical OR (||):", p || q);  // Output: true
console.log("Logical NOT (!):", !p);      // Output: false

// Assignment Operators
let c = 15;
console.log("Assignment Operators:");
console.log("c =", c);           // Output: 15
c += 5;                          // Equivalent to: c = c + 5;
console.log("c += 5:", c);       // Output: 20
c -= 3;                          // Equivalent to: c = c - 3;
console.log("c -= 3:", c);       // Output: 17
c *= 2;                          // Equivalent to: c = c * 2;
console.log("c *= 2:", c);       // Output: 34
c /= 4;                          // Equivalent to: c = c / 4;
console.log("c /= 4:", c);       // Output: 8.5
c %= 3;                          // Equivalent to: c = c % 3;
console.log("c %= 3:", c);       // Output: 2.5
console.log("------------");

// Conditional (Ternary) Operator
let age = 20;
let isAdult = (age >= 18) ? "Adult" : "Not Adult";
console.log("Conditional (Ternary) Operator:");
console.log("Is Adult?", isAdult); // Output: Adult
console.log("------------");

// Typeof Operator
let variable = "Hello";
console.log("Typeof Operator:");
console.log("Type of variable:", typeof variable); // Output: string

// Relational Operators
let num1 = 10;
let num2 = 5;
console.log("Relational Operators:");
console.log("Equal to (==):", num1 == num2);      // Output: false
console.log("Not Equal to (!=):", num1 != num2);  // Output: true
console.log("Greater than (>):", num1 > num2);    // Output: true
console.log("Less than (<):", num1 < num2);       // Output: false
console.log("Greater than or equal (>=):", num1 >= num2); // Output: true
console.log("Less than or equal (<=):", num1 <= num2);    // Output: false

// Bitwise Operators
let operand1 = 5; // Binary: 0101
let operand2 = 3; // Binary: 0011

console.log("Bitwise Operators:");
console.log("Bitwise AND (&):", operand1 & operand2);   // Output: 1 (Binary: 0001)
console.log("Bitwise OR (|):", operand1 | operand2);    // Output: 7 (Binary: 0111)
console.log("Bitwise XOR (^):", operand1 ^ operand2);   // Output: 6 (Binary: 0110)
console.log("Bitwise NOT (~):", ~operand1);             // Output: -6
console.log("Left Shift (<<):", operand1 << 1);         // Output: 10 (Binary: 1010)
console.log("Right Shift (>>):", operand2 >> 1);        // Output: 1 (Binary: 0001)
console.log("Zero-fill Right Shift (>>>):", operand2 >>> 1); // Output: 1 (Binary: 0001)
