public class ThrowDemo {
    public static void main(String[] args) {
      try {
        int num = 10 / 0;
      } catch (ArithmeticException e) {
        throw new ArithmeticException("Cannot divide by zero.");
      }
    }
  }