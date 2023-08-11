// Defining an interface
interface Animal {
    void makeSound(); // A method with no implementation
}

// Defining a class that implements the Animal interface
class Dog implements Animal {
    public void makeSound() {
        System.out.println("Woof!");
    }
}

// Another class that uses the Animal interface
class Cat implements Animal {
    public void makeSound() {
        System.out.println("Meow!");
    }
}

public class Program5 {
    public static void main(String[] args) {
        Animal dog = new Dog();
        dog.makeSound(); // Outputs "Woof!"
        
        Animal cat = new Cat();
        cat.makeSound(); // Outputs "Meow!"
    }
}
