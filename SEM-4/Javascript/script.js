function checkOddEven() {
    let number = parseInt(document.getElementById("numberInput").value);
    let output = number % 2 === 0 ? 'Even' : 'Odd';
    document.getElementById("oddEvenOutput").textContent = `The number is ${output}`;
  }

  function checkNumber() {
    let input = document.getElementById("inputCheck").value;
    let output = typeof +input === 'number' && !isNaN(+input) ? 'Number' : 'Not a number';
    document.getElementById("numberCheckOutput").textContent = `The input is ${output}`;
  }

  function findLargest() {
    let a = parseFloat(document.getElementById("num1").value);
    let b = parseFloat(document.getElementById("num2").value);
    let c = parseFloat(document.getElementById("num3").value);

    if (a >= b && a >= c) {
      document.getElementById("largestOutput").textContent = `The largest number is ${a}`;
    } else if (b >= a && b >= c) {
      document.getElementById("largestOutput").textContent = `The largest number is ${b}`;
    } else {
      document.getElementById("largestOutput").textContent = `The largest number is ${c}`;
    }
  }

  function checkTriangle() {
    let side1 = parseFloat(document.getElementById("side1").value);
    let side2 = parseFloat(document.getElementById("side2").value);
    let side3 = parseFloat(document.getElementById("side3").value);

    if (side1 === side2 && side2 === side3) {
      document.getElementById("triangleOutput").textContent = `It is an Equilateral triangle`;
    } else if (side1 === side2 || side1 === side3 || side2 === side3) {
      document.getElementById("triangleOutput").textContent = `It is an Isosceles triangle`;
    } else {
      document.getElementById("triangleOutput").textContent = `It is a Scalene triangle`;
    }
  }

  function checkLeapYear() {
    let year = parseInt(document.getElementById("yearInput").value);
    let output = (year % 4 === 0 && year % 100 !== 0) || year % 400 === 0 ? 'Leap Year' : 'Not a Leap Year';
    document.getElementById("leapYearOutput").textContent = `The year is ${output}`;
  }

  function findLargestTernary() {
    let a = parseFloat(document.getElementById("a").value);
    let b = parseFloat(document.getElementById("b").value);
    let c = parseFloat(document.getElementById("c").value);

    let largest = (a >= b && a >= c) ? a : (b >= a && b >= c) ? b : c;
    document.getElementById("largestTernaryOutput").textContent = `The largest number is ${largest}`;
  }

  function findGrade() {
    let marks = parseInt(document.getElementById("marksInput").value);
    let grade = '';

    if (marks >= 90) {
      grade = 'A';
    } else if (marks >= 80) {
      grade = 'B';
    } else if (marks >= 70) {
      grade = 'C';
    } else if (marks >= 60) {
      grade = 'D';
    } else {
      grade = 'F';
    }

    document.getElementById("gradeOutput").textContent = `The grade is ${grade}`;
  }

  function calculateTicketPrice() {
    let age = parseInt(document.getElementById("ageInput").value);
    let price = '';

    if (age < 12) {
      price = 5;
    } else if (age < 18) {
      price = 10;
    } else if (age < 60) {
      price = 20;
    } else {
      price = 15;
    }

    document.getElementById("ticketPriceOutput").textContent = `The ticket price is ₹${price}`;
  }

  function calculateDiscount() {
    let amount = parseInt(document.getElementById("amountInput").value);
    let discount = '';

    if (amount >= 100) {
      discount = amount * 0.2;
    } else if (amount >= 50) {
      discount = amount * 0.1;
    } else {
      discount = 0;
    }

    document.getElementById("discountOutput").textContent = `The discount is ₹${discount}`;
  }
