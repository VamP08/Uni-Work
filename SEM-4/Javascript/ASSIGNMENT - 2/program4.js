// Different Types of Functions
// Function Declaration
function add(a, b) {
    return a + b;
  }
  
  // Function Expression
  let multiply = function(a, b) {
    return a * b;
  };
  
  // Arrow Function
  let subtract = (a, b) => {
    return a - b;
  };
  
console.log(add(5, 3)); // Output: 8
console.log(multiply(5, 3)); // Output: 15
console.log(subtract(5, 3)); // Output: 2
  