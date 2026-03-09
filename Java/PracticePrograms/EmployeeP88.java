// Program: Empolyee Management

class Employees {

    int empNo;
    String name;
    String department;
    double salary;

    // Constructor to initialize an Employee object
    Employees(int empNo, String name, String department, double salary) {
        this.empNo = empNo;
        this.name = name;
        this.department = department;
        this.salary = salary;
    }

    // Method to display employee details
    void display() {
        System.out.println("Employee No: " + empNo);
        System.out.println("Name: " + name);
        System.out.println("Department: " + department);
        System.out.println("Salary: " + salary);
        System.out.println("-------------------------");
    }
}

public class EmployeeP88 {
    public static void main(String[] args) {

        // Check if there are enough arguments
        if (args.length < 20) {
            System.out.println("Please provide data for 5 employees: empNo, name, department, and salary for each.");
            return;
        }

        // Array to store Employee objects
        Employees[] employees = new Employees[5];

        // Read data for 5 employees from command-line arguments
        for (int i = 0; i < 5; i++) {
            int empNo = Integer.parseInt(args[i * 4]);
            String name = args[i * 4 + 1];
            String department = args[i * 4 + 2];
            double salary = Double.parseDouble(args[i * 4 + 3]);

            employees[i] = new Employees(empNo, name, department, salary);
        }

        // Display employee details
        System.out.println("Employee Details:");
        System.out.println("-------------------------");
        for (Employees employee : employees) {
            employee.display();
        }

        // Find the employee with the highest salary
        Employees highestPaid = employees[0];
        for (Employees employee : employees) {
            if (employee.salary > highestPaid.salary) {
                highestPaid = employee;
            }
        }

        // Display the employee with the highest salary
        System.out.println("Employee with the Highest Salary:");
        System.out.println("-------------------------");
        highestPaid.display();
    }
}