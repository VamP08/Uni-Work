import java.util.Scanner;

public class NestedTryExample {
    public static void main(String[] args) {
        try {
            try {
                int arr[] = {62, 52, 37, 13, 9};
                System.out.println(arr[5]);
            } catch (ArrayIndexOutOfBoundsException e) {
                System.out.println("Array Index Out Of Bounds Exception");
            }
            try {
                int a = 0;
                int b = 50 / a;
            } catch (ArithmeticException e) {
                System.out.println("Arithmetic Exception");
            }
            String s = null;
            s.length();
        } catch (Exception e) {
            System.out.println("Exception caught");
        }
    }
}