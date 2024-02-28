// Program 1: Print an array
function printArray() {
    const array = document.getElementById("array1").value.split(" ");
    document.getElementById("output1").innerText = "Array: " + array;
  }
  
  // Program 2: Print an array in reverse order
  function printReverseArray() {
    const array = document.getElementById("array2").value.split(" ");
    document.getElementById("output2").innerText = "Reverse Array: " + array.reverse();
  }
  
  // Program 3: Calculate sum of an array
  function calculateSum() {
    const array = document.getElementById("array3").value.split(" ").map(Number);
    const sum = array.reduce((acc, curr) => acc + curr, 0);
    document.getElementById("output3").innerText = "Sum: " + sum;
  }
  
  // Program 4: Calculate average of an array
  function calculateAverage() {
    const array = document.getElementById("array4").value.split(" ").map(Number);
    const sum = array.reduce((acc, curr) => acc + curr, 0);
    const average = sum / array.length;
    document.getElementById("output4").innerText = "Average: " + average.toFixed(2);
  }
  
  // Program 5: Find the largest element of an array
  function findLargest() {
    const array = document.getElementById("array5").value.split(" ").map(Number);
    const largest = Math.max(...array);
    document.getElementById("output5").innerText = "Largest Element: " + largest;
  }
  
  // Program 6: Find the smallest element of an array
  function findSmallest() {
    const array = document.getElementById("array6").value.split(" ").map(Number);
    const smallest = Math.min(...array);
    document.getElementById("output6").innerText = "Smallest Element: " + smallest;
  }
  