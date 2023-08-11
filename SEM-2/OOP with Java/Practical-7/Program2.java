interface Vehicle {
    void changeGear(int gear);
    void speedUp(int increment);
    void applyBrakes(int decrement);
}

// Implement the Bicycle class
class Bicycle implements Vehicle {
    int speed;
    int gear;
    
    public void changeGear(int gear) {
        this.gear = gear;
    }
    
    public void speedUp(int increment) {
        speed += increment;
    }
    
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }
    
    public void printState() {
        System.out.println("Bicycle [ speed: " + speed + ", gear: " + gear + " ]");
    }
}

// Implement the Bike class
class Bike implements Vehicle {
    int speed;
    int gear;
    
    public void changeGear(int gear) {
        this.gear = gear;
    }
    
    public void speedUp(int increment) {
        speed += increment;
    }
    
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }
    
    public void printState() {
        System.out.println("Bike [ speed: " + speed + ", gear: " + gear + " ]");
    }
}

// Implement the Car class
class Car implements Vehicle {
    int speed;
    int gear;
    
    public void changeGear(int gear) {
        this.gear = gear;
    }
    
    public void speedUp(int increment) {
        speed += increment;
    }
    
    public void applyBrakes(int decrement) {
        speed -= decrement;
    }
    
    public void printState() {
        System.out.println("Car [ speed: " + speed + ", gear: " + gear + " ]");
    }
}
public class Program2 {
    public static void main(String[] args) {
        // Create instances of each vehicle
        Bicycle bicycle = new Bicycle();
        Bike bike = new Bike();
        Car car = new Car();
        
        // Change gear and speed up for each vehicle
        bicycle.changeGear(2);
        bicycle.speedUp(20);
        bicycle.printState();
        
        bike.changeGear(3);
        bike.speedUp(30);
        bike.printState();
        
        car.changeGear(4);
        car.speedUp(40);
        car.printState();
    }
}
