    // Q1: Button click event listener
    document.getElementById("myButton").addEventListener("click", function () {
      console.log("Button clicked!");
    });

    // Q2: Change background color on mouse enter
    function changeBackgroundColor() {
      document.getElementById("changeColor").style.backgroundColor = "lightblue";
    }

    // Q3: Form validation
    function validateForm() {
      const name = document.getElementById("name").value;
      const email = document.getElementById("email").value;

      if (!name || !email) {
        alert("Please fill in all required fields");
      } else {
        alert("Form submitted successfully!");
      }
    }

    // Q4: Dropdown menu
    function toggleDropdown() {
      const dropdownOptions = document.getElementById("dropdownOptions");
      dropdownOptions.style.display =
        dropdownOptions.style.display === "none" ? "block" : "none";
    }