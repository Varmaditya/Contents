// Program: Employee Salary Filter

class Employee {
    String name;
    double salary;

    Employee(String name, double salary) {
        this.name = name;
        this.salary = salary;
    }
}

public class EmployeeSalaryFilterP51 {
    public static void main(String[] args) {

        Employee[] emp = {
                new Employee("Amit", 45000),
                new Employee("Neha", 60000),
                new Employee("Ravi", 30000)
        };

        for (Employee e : emp) {
            if (e.salary > 40000) {
                System.out.println(e.name + " : ₹" + e.salary);
            }
        }
    }
}
