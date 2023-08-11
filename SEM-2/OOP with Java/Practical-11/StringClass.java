public class StringClass {
    public static void main(String[] args) {
        String str1 = "Hello World";
        String str2 = "hello world";
        String str3 = "Hello World";
        String str4 = "Java Programming";
        String str5 = "Java Programming";

        // charAt() method
        System.out.println("charAt() method:");
        System.out.println("The character at index 0 in str1 is " + str1.charAt(0));
        System.out.println();

        // equals() method
        System.out.println("equals() method:");
        System.out.println("str1 equals str2? " + str1.equals(str2));
        System.out.println("str1 equals str3? " + str1.equals(str3));
        System.out.println();

        // equalsIgnoreCase() method
        System.out.println("equalsIgnoreCase() method:");
        System.out.println("str1 equalsIgnoreCase str2? " + str1.equalsIgnoreCase(str2));
        System.out.println();

        // compareTo() method
        System.out.println("compareTo() method:");
        System.out.println("str4 compareTo str5? " + str4.compareTo(str5));
        System.out.println();

        // indexOf() method
        System.out.println("indexOf() method:");
        System.out.println("The index of 'World' in str1 is " + str1.indexOf("World"));
        System.out.println();

        // lastIndexOf() method
        System.out.println("lastIndexOf() method:");
        System.out.println("The last index of 'o' in str1 is " + str1.lastIndexOf('o'));
        System.out.println();

        // substring() method
        System.out.println("substring() method:");
        System.out.println("The substring of 'World' in str1 is " + str1.substring(6, 11));
    }
}