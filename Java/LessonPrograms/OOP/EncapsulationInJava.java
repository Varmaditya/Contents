// Program: OOP Properties - Encapsulation in Java

class BankAccount {

    // ---------------- Private Variables ----------------
    private String accountHolder;
    private double balance;

    // ---------------- Constructor ----------------
    BankAccount(String accountHolder, double balance) {
        this.accountHolder = accountHolder;
        this.balance = balance;
    }

    // ---------------- Getter Methods ----------------
    public String getAccountHolder() {
        return accountHolder;
    }

    public double getBalance() {
        return balance;
    }

    // ---------------- Setter Methods ----------------
    public void setAccountHolder(String accountHolder) {
        this.accountHolder = accountHolder;
    }

    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("Amount Deposited: " + amount);
        } else {
            System.out.println("Invalid Deposit Amount");
        }
    }

    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("Amount Withdrawn: " + amount);
        } else {
            System.out.println("Insufficient Balance");
        }
    }
}

public class EncapsulationInJava {

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== OOP PROPERTY: ENCAPSULATION ====================");
        System.out.println("""
Encapsulation means:
✔ Wrapping data and methods together
✔ Restricting direct access to data
✔ Protecting internal state of object

It is achieved using:
✔ private variables
✔ public getter and setter methods
""");


        // ---------------- What is Encapsulation ----------------
        System.out.println("\n==================== WHAT IS ENCAPSULATION ====================");
        System.out.println("""
Encapsulation ensures:
✔ Data hiding
✔ Controlled access
✔ Security
✔ Better maintainability

Data should not be directly accessible from outside.
""");


        // ---------------- Creating Object ----------------
        System.out.println("\n==================== OBJECT CREATION ====================");
        BankAccount acc = new BankAccount("Amit Sharma", 5000);


        // ---------------- Accessing Data Using Getters ----------------
        System.out.println("\n==================== USING GETTERS ====================");
        System.out.println("Account Holder: " + acc.getAccountHolder());
        System.out.println("Current Balance: " + acc.getBalance());


        // ---------------- Performing Operations ----------------
        System.out.println("\n==================== USING METHODS FOR CONTROLLED ACCESS ====================");
        acc.deposit(2000);
        acc.withdraw(1000);
        System.out.println("Updated Balance: " + acc.getBalance());


        // ---------------- Why Private Variables ----------------
        System.out.println("\n==================== WHY PRIVATE VARIABLES ====================");
        System.out.println("""
If variables were public:
✔ Anyone could change balance directly
✔ No validation
✔ Security issues

Private ensures:
✔ No direct modification
✔ Controlled through methods
""");


        // ---------------- Getters & Setters ----------------
        System.out.println("\n==================== GETTERS & SETTERS ====================");
        System.out.println("""
Getter:
✔ Returns value of private variable

Setter:
✔ Sets value of private variable
✔ Can include validation

Encapsulation = Data Hiding + Controlled Access
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD EXAMPLE ====================");
        System.out.println("""
ATM Machine:
✔ You cannot directly access vault money
✔ You use deposit() and withdraw()
✔ System controls operations

This is Encapsulation in real life.
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Encapsulation wraps data and methods together.
→ Private variables hide data.
→ Getters and setters provide controlled access.
→ Improves security and maintainability.
→ One of the four main OOP principles.
""");
    }
}