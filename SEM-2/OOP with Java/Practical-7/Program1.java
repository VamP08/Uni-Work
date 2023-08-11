import java.util.ArrayList;

interface in1 {
    void display(int k);
}

class Class implements in1 {

    // helper method to check if a number is prime
    private boolean isPrime(int num) {
        if (num < 2) {
            return false;
        }
        for (int i = 2; i <= Math.sqrt(num); i++) {
            if (num % i == 0) {
                return false;
            }
        }
        return true;
    }

    public void display(int k) {
        ArrayList<Integer> primes = new ArrayList<Integer>();
        for (int i = 2; i <= k; i++) {
            if (isPrime(i)) {
                primes.add(i);
            }
        }
        System.out.println("Total number of prime numbers between 2 and " + k + " is: " + primes.size());
    }
}

public class Program1 {
    public static void main(String[] args) {
        Class obj = new Class();
        obj.display(20); // "Total number of prime numbers between 2 and 20 is: 8"
    }
}