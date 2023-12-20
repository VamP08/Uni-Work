console.log("Operator Precedence:");

//Multiplication (*) and division (/) have higher precedence than addition (+) and subtraction (-).
let result1 = 10 + 5 * 2;
console.log("10 + 5 * 2 =", result1); // Output: 20

//When using parentheses, operations inside the parentheses are computed first:
let result2 = (10 + 5) * 2; 
console.log("(10 + 5) * 2 =", result2); // Output: 30

// Modulus (%) has higher precedence than addition (+)
let result4 = 15 % 4 + 2; 
console.log("15 % 4 + 2 =", result4); // Output: 5

// Operations with the same precedence (like * and /) are computed from left to right
let result5 = 10 * 2 / 4;
console.log("10 * 2 / 4 =",result5); // Output: 5

// Comparison (relational) operators have lower precedence than arithmetic and logical operators
let result6 = 5 + 3 < 8 || 9 >= 10;
console.log("5 + 3 < 8 || 9 >= 10 =", result6); // Output: true

// Logical AND (&&) has higher precedence than Bitwise XOR (^)
let result7 = true && false ^ true; 
console.log("true && false ^ true =", result7); // Output: false
