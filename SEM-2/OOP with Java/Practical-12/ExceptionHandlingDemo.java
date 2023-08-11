import java.util.Scanner;
public class ExceptionHandlingDemo {
  public static void main(String[] args) {
    Scanner sc = new Scanner(System.in);
    try {
      System.out.print("Enter a number: ");
      int num = sc.nextInt();
      int result = 10 / num;
      System.out.println("Result: " + result);
    } catch (ArithmeticException e) {
      System.out.println("Error: " + e.getMessage());
    } finally {
      System.out.println("Finally block executed.");
    }
    sc.close();
  }
}