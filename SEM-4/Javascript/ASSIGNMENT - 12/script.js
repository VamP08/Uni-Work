// Q1. Creating an array and copying its items to another array, and displaying the copied items.
function copyArray() {
    const originalArray = [1, 2, 3, 4, 5];
    const copiedArray = [...originalArray];
    document.getElementById("output1").innerText = "Copied Array: " + copiedArray;
}

// Q2. Removing duplicates from an array of objects using JavaScript
function removeDuplicates() {
    const arrayWithDuplicates = [{ id: 1, name: 'John' }, { id: 2, name: 'Jane' }, { id: 1, name: 'John' }];
    const uniqueArray = arrayWithDuplicates.filter((obj, index, self) =>
        index === self.findIndex((t) => (t.id === obj.id && t.name === obj.name))
    );
    document.getElementById("output2").innerText = "Array with Duplicates Removed: " + JSON.stringify(uniqueArray);
}

// Q3. Comparing Arrays of Objects in JavaScript
function compareArrays() {
    const array1 = [{ id: 1, name: 'John' }, { id: 2, name: 'Jane' }];
    const array2 = [{ id: 1, name: 'John' }, { id: 2, name: 'Jane' }];
    const isEqual = JSON.stringify(array1) === JSON.stringify(array2);
    document.getElementById("output3").innerText = "Are Arrays Equal? " + isEqual;
}

// Q4. Taking student details and calculating total and percentage based on subject marks
function calculateMarks() {
    const studentName = document.getElementById("studentName").value;
    const subject1 = parseInt(document.getElementById("subject1").value);
    const subject2 = parseInt(document.getElementById("subject2").value);
    const subject3 = parseInt(document.getElementById("subject3").value);
    const totalMarks = subject1 + subject2 + subject3;
    const percentage = (totalMarks / 300) * 100;
    document.getElementById("output4").innerText = `Student Name: ${studentName}\nTotal Marks: ${totalMarks}\nPercentage: ${percentage.toFixed(2)}%`;
}
