
// Program 1: Person Class
class Person {
    constructor(name, age, country) {
      this.name = name;
      this.age = age;
      this.country = country;
    }

    displayDetails() {
      return `Name: ${this.name}, Age: ${this.age}, Country: ${this.country}`;
    }
  }

function createPerson() {
    const name = document.getElementById("name").value;
    const age = document.getElementById("age").value;
    const country = document.getElementById("country").value;
    const person = new Person(name, age, country);
    document.getElementById("personOutput").innerHTML = person.displayDetails();
  }

// Program 2: Rectangle Class
class Rectangle {
    constructor(width, height) {
      this.width = width;
      this.height = height;
    }

    calculateArea() {
      return this.width * this.height;
    }

    calculatePerimeter() {
      return 2 * (this.width + this.height);
    }
  }

function calculateRectangle() {
    const width = document.getElementById("width").value;
    const height = document.getElementById("height").value;
    const rectangle = new Rectangle(width, height);
    const area = rectangle.calculateArea();
    const perimeter = rectangle.calculatePerimeter();
    const rectangleDetails = `Area: ${area}, Perimeter: ${perimeter}`;
    document.getElementById("rectangleOutput").innerHTML = rectangleDetails;
  }

// Program 3: Vehicle and Car Classes
class Vehicle {
    constructor(make, model, year) {
      this.make = make;
      this.model = model;
      this.year = year;
    }

    displayDetails() {
      return `Make: ${this.make}, Model: ${this.model}, Year: ${this.year}`;
    }
  }

class Car extends Vehicle {
    constructor(make, model, year, doors) {
      super(make, model, year);
      this.doors = doors;
    }

    displayDetails() {
      return `${super.displayDetails()}, Doors: ${this.doors}`;
    }
  }

function createCar() {
    const make = document.getElementById("make").value;
    const model = document.getElementById("model").value;
    const year = document.getElementById("year").value;
    const doors = document.getElementById("doors").value;
    const car = new Car(make, model, year, doors);
    document.getElementById("carOutput").innerHTML = car.displayDetails();
  }

// Program 4: BankAccount Class
class BankAccount {
    constructor(accountNumber, balance) {
      this.accountNumber = accountNumber;
      this.balance = balance;
    }

    deposit(amount) {
      this.balance += amount;
    }

    withdraw(amount) {
      if (amount <= this.balance) {
        this.balance -= amount;
        return `Withdrawal of ${amount} successful. New balance: ${this.balance}`;
      } else {
        return "Insufficient funds.";
      }
    }
  }

function manageBankAccount() {
    const accountNumber = document.getElementById("accountNumber").value;
    const balance = document.getElementById("balance").value;
    const depositAmount = document.getElementById("depositAmount").value;
    const withdrawAmount = document.getElementById("withdrawAmount").value;

    const bankAccount = new BankAccount(accountNumber, parseFloat(balance));
    bankAccount.deposit(parseFloat(depositAmount));
    const withdrawalMessage = bankAccount.withdraw(parseFloat(withdrawAmount));
    document.getElementById("bankAccountOutput").innerHTML = withdrawalMessage;
  }

// Program 5: Shape, Circle, and Triangle Classes
class Shape {
    calculateArea() {
      return "Area calculation not implemented.";
    }
  }

class Circle extends Shape {
    constructor(radius) {
      super();
      this.radius = radius;
    }

    calculateArea() {
      return Math.PI * Math.pow(this.radius, 2);
    }
  }

class Triangle extends Shape {
    constructor(base, height) {
      super();
      this.base = base;
      this.height = height;
    }

    calculateArea() {
      return (this.base * this.height) / 2;
    }
  }

function calculateCircle() {
    const radius = document.getElementById("circleRadius").value;
    const circle = new Circle(parseFloat(radius));
    const area = circle.calculateArea();
    document.getElementById("circleOutput").innerHTML = `Circle Area: ${area}`;
  }

function calculateTriangle() {
    const base = document.getElementById("triangleBase").value;
    const height = document.getElementById("triangleHeight").value;
    const triangle = new Triangle(parseFloat(base), parseFloat(height));
    const area = triangle.calculateArea();
    document.getElementById("triangleOutput").innerHTML = `Triangle Area: ${area}`;
  }