// OBJECT ORIENTED PROGRAMMING (OOP) IN JAVA
// ------------------------------------------

class Student {

    // Class variable (shared by all objects)
    static String schoolName = "Bright Future School";

    // Instance variables
    String name;
    int age;

    // Constructor
    Student(String name, int age) {
        this.name = name;
        this.age = age;
    }

    // Instance method
    void display() {
        System.out.println("School: " + schoolName);
        System.out.println("Name: " + name);
        System.out.println("Age: " + age);
    }

    // Static method
    static void changeSchool(String newSchool) {
        schoolName = newSchool;
    }
}

public class Main {
    public static void main(String[] args) {

        // Creating objects
        Student s1 = new Student("Alice", 20);
        Student s2 = new Student("Bob", 22);

        // Display details
        s1.display();
        System.out.println();
        s2.display();

        // Changing class variable
        System.out.println("\nChanging School Name...\n");
        Student.changeSchool("Global Public School");

        s1.display();
        System.out.println();
        s2.display();
    }
}