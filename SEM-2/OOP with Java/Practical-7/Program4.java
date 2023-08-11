// Define an interface for playing musical instruments
interface Instrument {
    void play();
}

// Define an interface for tuning musical instruments
interface Tunable {
    void tune();
}

// Define a class for a guitar that implements both interfaces
class Guitar implements Instrument, Tunable {
    public void play() {
        System.out.println("Playing guitar");
    }

    public void tune() {
        System.out.println("Tuning guitar");
    }
}

// Define a class for a piano that implements only the Instrument interface
class Piano implements Instrument {
    public void play() {
        System.out.println("Playing piano");
    }
}

public class Program4 {
    public static void main(String[] args) {
        // create a guitar and call its play and tune methods
        Guitar guitar = new Guitar();
        guitar.play();
        guitar.tune(); 

        // create a piano and call its play method
        Piano piano = new Piano();
        piano.play();
    }
}