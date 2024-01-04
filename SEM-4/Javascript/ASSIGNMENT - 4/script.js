function DayToday(){
    let today = new Date();
    let day = today.getDay();
    let dayName;

    switch (day) {
    case 0:
        dayName = 'Sunday';
        break;
    case 1:
        dayName = 'Monday';
        break;
    case 2:
        dayName = 'Tuesday';
        break;
    case 3:
        dayName = 'Wednesday';
        break;
    case 4:
        dayName = 'Thursday';
        break;
    case 5:
        dayName = 'Friday';
        break;
    case 6:
        dayName = 'Saturday';
        break;
    default:
        dayName = 'Invalid day';
        break;
    }
    document.getElementById("output1").textContent = `Today is ${dayName}`;
}

function SimpleCalci(){
    let num1 = parseFloat(document.getElementById("num1").value);
    let num2 = parseFloat(document.getElementById("num2").value);
    let op = document.getElementById("op").value;
    let output;

    switch (op) {
        case '+':
            output = num1 + num2;
            break;
        case '-':
            output = num1 - num2;
            break;
        case '*':
            output = num1 * num2;    
            break;
        case '/':
            output = num1 / num2;
            break;
        case '%':
            output = num1 % num2;
            break;
        default:
            output = 'Invalid Operator';
            break;
    }
    document.getElementById("output2").textContent = `${output}`;
}

function CheckChar(){
    let Char = document.getElementById("Char").value;
    let output;
    
    switch (Char) {
        case 'a':
        case 'e':
        case 'i':
        case 'o':
        case 'u':
            output = 'Vowel';
            break;
        default:
            output = 'Consonant';
            break;
    } 
    document.getElementById("output3").textContent = 'Your Alphabet is a '+`${output}`;
    
}

function DaysCount(){
    let month = document.getElementById("month").value;
    let year = parseInt(document.getElementById("year").value);
    let output;

    switch (month) {
        case 'January':
        case 'March':
        case 'May':
        case 'July':
        case 'August':
        case 'October':
        case 'December':
            output=31;
            break;
        
        case 'April':
        case 'June':
        case 'September':
        case 'November':
            output=30;
            break;
        
        case 'February':
            if ((year % 400 == 0) ||
            (year % 100 != 0) && 
            (year % 4 == 0)){
                output = 29;
            }    
            else {
                output = 28;
            }
            break;

        default:
            output = 'Invalid Month';
            break;
    }
    document.getElementById("output4").innerHTML = `Number of days in ${month} in year ${year} - `+"<br>"+`${output}`;
}

function calculateGrade() {
    let subject1 = parseInt(document.getElementById('subject1').value);
    let subject2 = parseInt(document.getElementById('subject2').value);
    let subject3 = parseInt(document.getElementById('subject3').value);
    let subject4 = parseInt(document.getElementById('subject4').value);

    let total = subject1 + subject2 + subject3 + subject4;

    document.getElementById('total').value = total;

    let grade;
    switch (true) {
      case total >= 80:
        grade = 'A';
        break;
      case total >= 60:
        grade = 'B';
        break;
      case total >= 40:
        grade = 'C';
        break;
      case total >= 20:
        grade = 'D';
        break;
      default:
        grade = 'E';
        break;
    }

    document.getElementById('grade').value = grade;

    let remark;
    switch (grade) {
      case 'A':
        remark = 'Excellent';
        break;
      case 'B':
        remark = 'Good';
        break;
      case 'C':
        remark = 'Average';
        break;
      case 'D':
        remark = 'Below Average';
        break;
      default:
        remark = 'Poor';
        break;
    }
    document.getElementById('remark').value = remark;
  }