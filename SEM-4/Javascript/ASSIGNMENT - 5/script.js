
function printnumbers(){
    const outputDiv = document.getElementById('output1');

    for (let i = 1; i <= 10; i++) {
    // Create a text node containing the current number
    const textNode = document.createTextNode(i);

    // Create a line break element
    const lineBreak = document.createElement('br');

    // Append the text node (number) and line break to the output div
    outputDiv.appendChild(textNode);
    outputDiv.appendChild(lineBreak);
    }    
}

function FibonacciSeq(){
    const outputDiv = document.getElementById('output2');
    let num = parseFloat(document.getElementById("num").value);
    a=0
    b=1
    textNode = document.createTextNode(a);
    lineBreak = document.createElement('br');
    outputDiv.appendChild(textNode);
    outputDiv.appendChild(lineBreak);
    
    for (let i = 1; i < num; i++){
        c=a+b;
        a=b;
        b=c;
        textNode = document.createTextNode(a);
        lineBreak = document.createElement('br');
        outputDiv.appendChild(textNode);
        outputDiv.appendChild(lineBreak);
    }
}

function CountChar(){
    text = document.getElementById("Charac").value;
    document.getElementById("output3").textContent = text.length;
}

function OddNum(){
    num = parseInt(document.getElementById("OddNum").value);
    const outputDiv = document.getElementById('output4');
    for (let i=0; i<=num; i++){
        if (i%2!=0){
            textNode = document.createTextNode(i);
            lineBreak = document.createElement('br');
            outputDiv.appendChild(textNode);
            outputDiv.appendChild(lineBreak);
        }
    }
}

function SumN(){
    num = parseInt(document.getElementById("SumNum").value);
    outputDiv = 0;
    for (let i=1; i<=num; i++){
        outputDiv+=i;
    }
    document.getElementById("SumAll").textContent = outputDiv;
  }

function generatePascalsTriangle(rows) {
  let triangle = [];

  for (let i = 0; i < rows; i++) {
    triangle[i] = [];
    for (let j = 0; j <= i; j++) {
      if (j === 0 || j === i) {
        triangle[i][j] = 1;
      } else {
        triangle[i][j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
      }
    }
  }

  return triangle;
}

function printPascalsTriangle() {
  let rows = parseInt(document.getElementById("PascalTri").value);
  let pascalsTriangle = generatePascalsTriangle(rows);
  let triangleDiv = document.getElementById("PT");
  triangleDiv.innerHTML = ''; // Clear previous content

  for (let i = 0; i < pascalsTriangle.length; i++) {
    let rowDiv = document.createElement("div");
    for (let j = 0; j < pascalsTriangle[i].length; j++) {
      let cellSpan = document.createElement("span");
      cellSpan.textContent = pascalsTriangle[i][j] + ' ';
      rowDiv.appendChild(cellSpan);
    }
    triangleDiv.appendChild(rowDiv);
  }
}
  
  function PatternA() {
    let patternA = '';
    let word = document.getElementById("P1").value;
    for (let i = 1; i <= word.length; i++) {
      patternA += word.substring(0, i) + '<br>';
    }
    document.getElementById("t1").innerHTML = patternA;
  }

  function PatternB() {
    let patternB = '';
    let num = document.getElementById("P2").value;
    for (let i = num; i >= 1; i--) {
      for (let j = num; j >= i; j--) {
        patternB += j;
      }
      patternB += '<br>';
    }
    document.getElementById("t2").innerHTML = patternB;
  }

  function PatternC() {
    let patternC = '';
    let num = document.getElementById("P3").value;
    for (let i = 1; i <= num; i++) {
      for (let j = 1; j <= num - i + 1; j++) {
        patternC += j;
      }
      for (let k = 1; k < i * 2 - 1; k++) {
        patternC += '&nbsp;&nbsp;';
      }
      for (let l = num - i + 1; l >= 1; l--) {
        patternC += l;
      }
      patternC += '<br>';
    }
    document.getElementById("t3").innerHTML = patternC;
  }

  function MulTable() {
    printTable(11, "Table11");
    printTable(12, "Table12");
    printTable(13, "Table13");
    printTable(14, "Table14");
    printTable(15, "Table15");
  }

  function printTable(number, elementId) {
    let tableContent = 'Multiplication Table of ' + number + '<br>';
    for (let i = 1; i <= 10; i++) {
      tableContent += number + ' x ' + i + ' = ' + (number * i) + '<br>';
    }
    document.getElementById(elementId).innerHTML = tableContent;
  }