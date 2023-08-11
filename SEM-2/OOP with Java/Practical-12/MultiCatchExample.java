import java.util.Scanner;
public class MultiCatchExample {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        try {   
            System.out.print("Enter a number: ");
            int a = sc.nextInt();
            int b = 10 / a;
            String s = null;
            s.length();
        } catch (ArithmeticException | NullPointerException e) {
            System.out.println("Exception caught: " + e);
        }
    }
}