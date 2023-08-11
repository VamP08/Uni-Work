// Define an interface for a Shape
interface Shape {
    double getArea();
}

abstract class Quadrilateral {
    protected double width;
    protected double height;

    public Quadrilateral(double width, double height) {
        this.width = width;
        this.height = height;
    }

    abstract double getArea();
}

class Rectangle extends Quadrilateral implements Shape {
    public Rectangle(double width, double height) {
        super(width, height);
    }

    public double getArea() {
        return width * height;
    }
}

public class Program6 {
    public static void main(String[] args) {
        // create a Rectangle object and call its getArea method
        Rectangle rectangle = new Rectangle(5, 10);
        System.out.println("Rectangle area: " + rectangle.getArea());
    }
}