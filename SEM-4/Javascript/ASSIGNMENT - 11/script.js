// Program 1: Creating and initializing an array with different methods
function createArray() {
    // Method 1: Using Array literal
    const array1 = [1, 2, 3, 4, 5];

    // Method 2: Using new keyword
    const array2 = new Array(1, 2, 3, 4, 5);

    // Method 3: Using Array.from() method
    const array3 = Array.from([1, 2, 3, 4, 5]);

    document.getElementById("output1").innerHTML = `
        Array 1: ${array1}<br>
        Array 2: ${array2}<br>
        Array 3: ${array3}
    `;
}

// Program 2: Differentiating between const and var when declaring the array
function declareArray() {
    // Using const
    const array1 = [1, 2, 3, 4, 5];

    // Using var
    var array2 = [1, 2, 3, 4, 5];

    document.getElementById("output2").innerHTML = `
        Array 1 (const): ${array1}<br>
        Array 2 (var): ${array2}
    `;
}

// Program 3: Adding an element to the end of an array
function addElement() {
    const element = document.getElementById("array3").value;
    const array = [1, 2, 3, 4, 5];
    array.push(element);
    document.getElementById("output3").innerText = "Array with added element: " + array;
}

// Program 4: Adding an element to the beginning of an array
function addElementToBeginning() {
    const element = document.getElementById("array4").value;
    const array = [1, 2, 3, 4, 5];
    array.unshift(element);
    document.getElementById("output4").innerText = "Array with added element at the beginning: " + array;
}

// Program 5: Removing an element from the end of an array
function removeElement() {
    const array = [1, 2, 3, 4, 5];
    array.pop();
    document.getElementById("output5").innerText = "Array with element removed from the end: " + array;
}

// Program 6: Removing an element from the beginning of an array
function removeElementFromBeginning() {
    const array = [1, 2, 3, 4, 5];
    array.shift();
    document.getElementById("output6").innerText = "Array with element removed from the beginning: " + array;
}

// Program 7: Finding the index of an element in the array
function findIndex() {
    const element = document.getElementById("elementIndex").value;
    const array = document.getElementById("array7").value.split(" ");
    const index = array.indexOf(element);
    document.getElementById("output7").innerText = `Index of ${element} in the array: ${index}`;
}

// Program 8: Checking if a value is an array
function checkArray() {
    const value = document.getElementById("valueToCheck").value;
    const isArray = Array.isArray(value);
    document.getElementById("output8").innerText = `Is ${value} an array? ${isArray}`;
}

// Program 9: Display array data in ordered and unordered lists
function displayLists() {
    const array = document.getElementById("array9").value.split(" ");
    const orderedList = document.getElementById("orderedList");
    const unorderedList = document.getElementById("unorderedList");
    
    // Clear existing lists
    orderedList.innerHTML = "";
    unorderedList.innerHTML = "";
    
    // Add elements to lists
    array.forEach(element => {
        const li = document.createElement("li");
        li.textContent = element;
        orderedList.appendChild(li);

        const li2 = document.createElement("li");
        li2.textContent = element;
        unorderedList.appendChild(li2);
    });
}
