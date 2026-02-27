// Program: Constructors in Java

class Student2 {

    // ---------------- Instance Variables ----------------
    String name;
    int age;

    // ---------------- Default Constructor ----------------
    Student2() {
        System.out.println("Default Constructor Called");
        name = "Unknown";
        age = 0;
    }

    // ---------------- Parameterized Constructor ----------------
    Student2(String name, int age) {

        // Using this keyword to refer current object
        this.name = name;
        this.age = age;

        System.out.println("Parameterized Constructor Called");
    }

    // ---------------- Constructor Overloading ----------------
    Student2(String name) {
        this.name = name;
        this.age = 18;   // default age
        System.out.println("Overloaded Constructor (Name only)");
    }

    // ---------------- Method ----------------
    void display() {
        System.out.println("Name: " + name + ", Age: " + age);
    }
}

public class ConstructorsInJava {

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== CONSTRUCTORS IN JAVA ====================");
        System.out.println("""
A Constructor is a special method
used to initialize objects.

✔ Same name as class
✔ No return type (not even void)
✔ Automatically called when object is created
""");


        // ---------------- Why Constructors ----------------
        System.out.println("\n==================== WHY CONSTRUCTORS? ====================");
        System.out.println("""
Constructors are used to:
✔ Initialize instance variables
✔ Ensure object starts in valid state
✔ Assign default or user-defined values
""");


        // ---------------- Default Constructor ----------------
        System.out.println("\n==================== DEFAULT CONSTRUCTOR ====================");
        System.out.println("""
A Default Constructor:
✔ Has no parameters
✔ Assigns default values
✔ Called automatically

Syntax:
ClassName() { }
""");

        Student2 s1 = new Student2();
        s1.display();


        // ---------------- Parameterized Constructor ----------------
        System.out.println("\n==================== PARAMETERIZED CONSTRUCTOR ====================");
        System.out.println("""
A Parameterized Constructor:
✔ Accepts arguments
✔ Assigns values during object creation
✔ Allows dynamic initialization
""");

        Student2 s2 = new Student2("Amit", 21);
        s2.display();


        // ---------------- Constructor Overloading ----------------
        System.out.println("\n==================== CONSTRUCTOR OVERLOADING ====================");
        System.out.println("""
Constructor Overloading means:
✔ Multiple constructors
✔ Same class name
✔ Different parameter lists

Allows multiple ways to create object.
""");

        Student2 s3 = new Student2("Neha");
        s3.display();


        // ---------------- this Keyword ----------------
        System.out.println("\n==================== THIS KEYWORD ====================");
        System.out.println("""
this keyword refers to:
✔ Current object

Used when:
✔ Instance variable and parameter have same name
✔ To avoid confusion
""");

        System.out.println("""
Example:
Student(String name, int age) {
    this.name = name;
    this.age = age;
}
""");


        // ---------------- Referring to Current Object ----------------
        System.out.println("\n==================== REFERRING TO CURRENT OBJECT ====================");
        System.out.println("""
Without 'this':
    name = name;

This causes ambiguity.

With 'this':
    this.name = name;

Now:
✔ Left side → instance variable
✔ Right side → parameter
""");


        // ---------------- Constructor vs Method ----------------
        System.out.println("\n==================== CONSTRUCTOR vs METHOD ====================");
        System.out.println("""
CONSTRUCTOR:
✔ Same name as class
✔ No return type
✔ Called automatically
✔ Used to initialize object

METHOD:
✔ Can have any name
✔ Has return type
✔ Called explicitly
✔ Used to perform actions
""");


        // ---------------- Memory Concept ----------------
        System.out.println("\n==================== MEMORY CONCEPT ====================");
        System.out.println("""
When object is created:
Student s = new Student();

✔ Memory allocated in Heap
✔ Constructor initializes variables
✔ Object becomes ready to use
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Giving return type to constructor
✘ Forgetting to initialize variables
✘ Confusing constructor with method
✘ Not using this when needed
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Constructor initializes object.
→ Default constructor has no parameters.
→ Parameterized constructor accepts values.
→ Constructors can be overloaded.
→ this keyword refers to current object.
→ Constructor runs automatically when object is created.

Constructors are the ENTRY POINT of object life cycle.
""");
    }
}