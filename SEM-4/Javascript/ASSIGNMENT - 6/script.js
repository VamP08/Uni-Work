function submitForm() {
    // Get form data
    var name = document.getElementById("name").value;
    var email = document.getElementById("email").value;
    var gender = document.querySelector('input[name="gender"]:checked') ? document.querySelector('input[name="gender"]:checked').value : "";
    var terms = document.getElementById("terms").checked;

    // Display data in alert
    if (name && email && gender && terms) {
        var message = "Submitted Data:\n\nName: " + name + "\nEmail: " + email + "\nGender: " + gender;
        alert(message);
    } else {
        alert("Please fill in all fields and agree to the terms.");
    }
}

function clearForm() {
    // Clear form fields
    document.getElementById("name").value = "";
    document.getElementById("email").value = "";
    document.getElementById("male").checked = false;
    document.getElementById("female").checked = false;
    document.getElementById("terms").checked = false;
}
