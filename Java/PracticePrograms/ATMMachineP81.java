// Program: ATM Machine

class ATM {

    double balance;

    ATM(double balance) {
        this.balance = balance;
    }

    void deposit(double amount) {
        balance += amount;
    }

    void withdraw(double amount) {

        if (amount <= balance)
            balance -= amount;
        else
            System.out.println("Insufficient balance");
    }

    void checkBalance() {
        System.out.println("Balance: ₹" + balance);
    }
}

public class ATMMachineP81 {

    public static void main(String[] args) {

        ATM atm = new ATM(10000);

        atm.deposit(2000);
        atm.withdraw(3000);
        atm.checkBalance();
    }
}