/**
 *Project: Simple Bank Management System.
 *      It allows users to create accounts, deposit or withdraw money,
 * transfer funds, and view their transactions.
 * Access is protected using a PIN, and an admin panel can view all accounts.
 * This project demonstrates basic OOP concepts, arrays, methods, and console-based menus.
**/

import java.util.*;

/* Account class stores all account information and transactions */
class Account {

    int accountNumber;
    String name;
    String phone;
    int pin;
    double balance;

    ArrayList<String> transactions = new ArrayList<>();

    /* Constructor creates a new bank account */
    Account(int accountNumber, String name, String phone, int pin, double balance) {
        this.accountNumber = accountNumber;
        this.name = name;
        this.phone = phone;
        this.pin = pin;
        this.balance = balance;

        transactions.add("Account created with balance: " + balance);
    }

    /* Deposit money into account */
    void deposit(double amount) {
        balance += amount;
        transactions.add("Deposited: " + amount);
    }

    /* Withdraw money if sufficient balance */
    boolean withdraw(double amount) {
        if (amount > balance) {
            return false;
        }

        balance -= amount;
        transactions.add("Withdrawn: " + amount);
        return true;
    }

    /* Add transfer transaction record */
    void addTransaction(String message) {
        transactions.add(message);
    }

    /* Print account details */
    void showDetails() {
        System.out.println("\n===== ACCOUNT DETAILS =====");
        System.out.println("Account Number : " + accountNumber);
        System.out.println("Name           : " + name);
        System.out.println("Phone          : " + phone);
        System.out.println("Balance        : " + balance);
    }

    /* Print account statement */
    void showStatement() {
        System.out.println("\n===== MINI STATEMENT =====");

        for (String t : transactions) {
            System.out.println(t);
        }
    }
}


/* Main banking system class which controls all operations */
class BankSystem {

    static Scanner sc = new Scanner(System.in);

    /* Array storing all bank accounts */
    static Account accounts[] = new Account[100];
    static int accountCount = 0;

    /* Admin credentials */
    static String adminUser = "admin";
    static String adminPass = "bank123";

    static int nextAccountNumber = 1001;

    /* Method to create a new account */
    static void createAccount() {

        System.out.println("\n===== CREATE ACCOUNT =====");

        System.out.print("Enter Name: ");
        String name = sc.next();

        System.out.print("Enter Phone: ");
        String phone = sc.next();

        System.out.print("Set 4 digit PIN: ");
        int pin = sc.nextInt();

        System.out.print("Initial Deposit: ");
        double balance = sc.nextDouble();

        Account acc = new Account(nextAccountNumber, name, phone, pin, balance);

        accounts[accountCount] = acc;
        accountCount++;

        System.out.println("\nAccount Created Successfully!");
        System.out.println("Your Account Number: " + nextAccountNumber);

        nextAccountNumber++;
    }

    /* Method to search account using account number */
    static Account findAccount(int accNo) {

        for (int i = 0; i < accountCount; i++) {
            if (accounts[i].accountNumber == accNo)
                return accounts[i];
        }

        return null;
    }

    /* User login using account number and pin */
    static Account login() {

        System.out.print("Enter Account Number: ");
        int accNo = sc.nextInt();

        Account acc = findAccount(accNo);

        if (acc == null) {
            System.out.println("Account not found");
            return null;
        }

        System.out.print("Enter PIN: ");
        int pin = sc.nextInt();

        if (acc.pin != pin) {
            System.out.println("Incorrect PIN");
            return null;
        }

        return acc;
    }

    /* Deposit money to account */
    static void depositMoney(Account acc) {

        System.out.print("Enter amount to deposit: ");
        double amt = sc.nextDouble();

        acc.deposit(amt);

        System.out.println("Deposit successful");
    }

    /* Withdraw money using ATM */
    static void withdrawMoney(Account acc) {

        System.out.print("Enter withdrawal amount: ");
        double amt = sc.nextDouble();

        if (acc.withdraw(amt)) {
            System.out.println("Withdrawal successful");
        } else {
            System.out.println("Insufficient balance");
        }
    }

    /* Transfer money between two accounts */
    static void transferMoney(Account sender) {

        System.out.print("Enter receiver account number: ");
        int receiverNo = sc.nextInt();

        Account receiver = findAccount(receiverNo);

        if (receiver == null) {
            System.out.println("Receiver account not found");
            return;
        }

        System.out.print("Enter transfer amount: ");
        double amount = sc.nextDouble();

        if (sender.withdraw(amount)) {

            receiver.deposit(amount);

            sender.addTransaction("Transferred " + amount + " to " + receiver.accountNumber);
            receiver.addTransaction("Received " + amount + " from " + sender.accountNumber);

            System.out.println("Transfer successful");
        } else {
            System.out.println("Insufficient balance");
        }
    }

    /* Update user details */
    static void updateAccount(Account acc) {

        System.out.println("\n===== UPDATE ACCOUNT =====");

        System.out.print("Enter new phone number: ");
        acc.phone = sc.next();

        System.out.println("Phone updated successfully");
    }

    /* ATM menu for user */
    static void atmMenu(Account acc) {

        int choice;

        do {
            System.out.println("\n===== ATM MENU =====");

            System.out.println("1 Withdraw");
            System.out.println("2 Check Balance");
            System.out.println("3 Mini Statement");
            System.out.println("4 Exit ATM");

            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    withdrawMoney(acc);
                    break;
                case 2:
                    System.out.println("Balance: " + acc.balance);
                    break;
                case 3:
                    acc.showStatement();
                    break;
            }

        } while (choice != 4);

    }

    /* Admin login to see all accounts */
    static void adminPanel() {

        System.out.print("Admin Username: ");
        String user = sc.next();

        System.out.print("Admin Password: ");
        String pass = sc.next();

        if (user.equals(adminUser) && pass.equals(adminPass)) {
            System.out.println("\n===== ALL ACCOUNTS =====");

            for (int i = 0; i < accountCount; i++) {
                accounts[i].showDetails();
            }
        } else {
            System.out.println("Invalid admin login");
        }
    }
}


/* Main class containing main menu */
public class BankingApplication {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);
        int choice;

        while (true) {

            System.out.println("\n====== BANK MANAGEMENT SYSTEM ======");

            System.out.println("1 Create Account");
            System.out.println("2 View My Account");
            System.out.println("3 ATM System");
            System.out.println("4 Deposit Money");
            System.out.println("5 Transfer Money");
            System.out.println("6 Update Account");
            System.out.println("7 View Statement");
            System.out.println("8 Admin Panel");
            System.out.println("9 Exit");

            System.out.print("Enter choice: ");
            choice = sc.nextInt();

            switch (choice) {
                case 1:
                    BankSystem.createAccount();
                    break;
                case 2: {
                    Account acc = BankSystem.login();
                    if (acc != null)
                        acc.showDetails();
                    break;
                }
                case 3: {
                    Account acc = BankSystem.login();
                    if (acc != null)
                        BankSystem.atmMenu(acc);
                    break;
                }
                case 4: {
                    Account acc = BankSystem.login();
                    if (acc != null)
                        BankSystem.depositMoney(acc);
                    break;
                }
                case 5: {
                    Account acc = BankSystem.login();
                    if (acc != null)
                        BankSystem.transferMoney(acc);
                    break;
                }
                case 6: {
                    Account acc = BankSystem.login();
                    if (acc != null)
                        BankSystem.updateAccount(acc);
                    break;
                }
                case 7: {
                    Account acc = BankSystem.login();
                    if (acc != null)
                        acc.showStatement();
                    break;
                }
                case 8:
                    BankSystem.adminPanel();
                    break;
                case 9:
                    System.out.println("Thank you for using the bank system");
                    System.exit(0);
                default:
                    System.out.println(("Invalid choice! Please choose between 1-9."));
                    break;
            }
        }
    }
}
