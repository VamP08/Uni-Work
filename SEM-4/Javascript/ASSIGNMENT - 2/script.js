let displayValue = "";

function appendToDisplay(value) {
  displayValue += value;
  document.getElementById("display").value = displayValue;
}

function clearDisplay() {
  displayValue = "";
  document.getElementById("display").value = displayValue;
}

function calculate() {
  try {
    if (displayValue.includes('radius = ')) {
      const radius = parseFloat(displayValue.replace('radius = ', ''));
      const result = Math.PI * radius * radius;
      displayValue = parseFloat(result.toFixed(10)).toString();
      document.getElementById("display").value = displayValue;
    }else if(displayValue.includes('$')){
      const dollars = parseFloat(displayValue.replace('$', ''));
      const rupees = 83 * dollars;
      displayValue = parseFloat(rupees.toFixed(10)).toString();
      document.getElementById("display").value =  "₹"+displayValue;
    } 
    else {
      result = new Function('return ' + displayValue)();
      document.getElementById("display").value = displayValue;
    }
    document.getElementById("display").value = displayValue;
  } catch (error) {
    displayValue = "";
    document.getElementById("display").value = "Error";
    alert("Error")
  }
}
