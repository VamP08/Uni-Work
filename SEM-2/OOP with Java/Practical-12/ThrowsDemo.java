import java.io.IOException;
public class ThrowsDemo {
  public static void main(String[] args) {
    try {
      ThrowsDemo obj = new ThrowsDemo();
      obj.testMethod();
    } catch (IOException e) {
      System.out.println("Error: " + e.getMessage());
    }
  }

  public void testMethod() throws IOException, ArithmeticException {
    int num = 10 / 0;
    throw new IOException("IOException occurred.");
  }
}