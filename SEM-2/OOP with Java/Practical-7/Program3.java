interface PaymentStrategy {
    void pay(double amount);
}

// Concrete implementation of payment via credit card
class CreditCardPayment implements PaymentStrategy {
    private String name;
    private String cardNumber;
    private String cvv;
    private String expiryDate;

    public CreditCardPayment(String name, String cardNumber, String cvv, String expiryDate) {
        this.name = name;
        this.cardNumber = cardNumber;
        this.cvv = cvv;
        this.expiryDate = expiryDate;
    }

    public void pay(double amount) {
        System.out.println("Paying " + amount + " via Credit Card.");
    }
}

class PayPalPayment implements PaymentStrategy {
    private String email;
    private String password;

    public PayPalPayment(String email, String password) {
        this.email = email;
        this.password = password;
    }

    public void pay(double amount) {
        System.out.println("Paying " + amount + " via PayPal.");
    }
}

// Concrete implementation of payment via BitCoin
class BitCoinPayment implements PaymentStrategy {
    private String walletAddress;

    public BitCoinPayment(String walletAddress) {
        this.walletAddress = walletAddress;
    }

    public void pay(double amount) {
        System.out.println("Paying " + amount + " via BitCoin.");
    }
}

// Shopping cart class that uses the payment strategy
class ShoppingCart {
    private PaymentStrategy paymentStrategy;

    public ShoppingCart(PaymentStrategy paymentStrategy) {
        this.paymentStrategy = paymentStrategy;
    }

    public void pay(double amount) {
        paymentStrategy.pay(amount);
    }
}

// Example usage of the Shopping Cart class
public class Program3 {
    public static void main(String[] args) {
        // create a shopping cart with a payment strategy of Credit Card
        ShoppingCart cart1 = new ShoppingCart(new CreditCardPayment("John Doe", "1234567890123456", "123", "12/24"));
        cart1.pay(100.0);

        // create a shopping cart with a payment strategy of PayPal
        ShoppingCart cart2 = new ShoppingCart(new PayPalPayment("johndoe@example.com", "password123"));
        cart2.pay(50.0);

        // create a shopping cart with a payment strategy of BitCoin
        ShoppingCart cart3 = new ShoppingCart(new BitCoinPayment("1BvBMSEYstWetqTFn5Au4m4GFg7xJaNVN2"));
        cart3.pay(200.0);
    }
}