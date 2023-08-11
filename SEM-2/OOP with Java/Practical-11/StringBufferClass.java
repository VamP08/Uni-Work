public class StringBufferClass {
    public static void main(String[] args) {
        StringBuffer sb = new StringBuffer("Hello");

        // capacity() method
        System.out.println("capacity() method:");
        System.out.println("The current capacity of sb is " + sb.capacity());
        System.out.println();

        // setCharAt() method
        System.out.println("setCharAt() method:");
        sb.setCharAt(1, 'i');
        System.out.println("After setting character at index 1 to 'i', sb is now " + sb);
        System.out.println();

        // append() method
        System.out.println("append() method:");
        sb.append(" World");
        System.out.println("After appending ' World', sb is now " + sb);
        System.out.println();

        // insert() method
        System.out.println("insert() method:");
        sb.insert(5, " there,");
        System.out.println("After inserting ' there,' at index 5, sb is now " + sb);
        System.out.println();

        // delete() method
        System.out.println("delete() method:");
        sb.delete(5, 12);
        System.out.println("After deleting characters from index 5 to 11, sb is now " + sb);
        System.out.println();

        // deleteCharAt() method
        System.out.println("deleteCharAt() method:");
        sb.deleteCharAt(4);
        System.out.println("After deleting character at index 4, sb is now " + sb);
    }
}
