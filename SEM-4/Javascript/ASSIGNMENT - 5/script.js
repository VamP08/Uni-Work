
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