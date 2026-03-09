// Program: Bank Account Manager

public class BankAccountP87 {

    // Data members
    private int acctNo;
    private double balance;
    private String acctType;

    // Constructor to initialize account details
    public BankAccountP87(int acctNo, double balance, String acctType) {
        this.acctNo = acctNo;
        this.balance = balance;
        this.acctType = acctType;
    }

    // Method to deposit an amount
    public void deposit(double amount) {
        balance += amount;
        System.out.println("Deposited: " + amount);
    }

    // Method to withdraw an amount
    public void withdraw(double amount) {
        if (balance >= amount) {
            balance -= amount;
            System.out.println("Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient balance for withdrawal.");
        }
    }

    // Method to display account details
    public void displayAccountDetails() {
        System.out.println("Account Number: " + acctNo);
        System.out.println("Account Type: " + acctType);
        System.out.println("Account Balance: " + balance);
    }

    // Main method to perform operations
    public static void main(String[] args) {

        // Creating a BankAccount object
        BankAccountP87 account = new BankAccountP87(101, 5000.0, "Savings");

        // Display initial account details
        System.out.println("Initial Account Details:");
        account.displayAccountDetails();

        // Deposit 10,000
        account.deposit(10000);

        // Withdraw 5,000
        account.withdraw(5000);

        // Display final account details
        System.out.println("\nFinal Account Details:");
        account.displayAccountDetails();
    }
}