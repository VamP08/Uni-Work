class NoMatchException extends Exception {
  public NoMatchException(String message) {
    super(message);
  }
}
  
public class CustomExceptionDemo {
  public static void main(String[] args) {
    
      try {
        String str = "Hi";
        if (!str.equals("Hello")) {
          throw new NoMatchException("String does not match.");
        }
      } catch (NoMatchException e) {
        System.out.println("Error: " + e.getMessage());
      }
  }
}