// Program: Scope of Variables in Java

public class ScopeOfVariablesInJava {

    // ---------------- Instance (Global) Variable ----------------
    int instanceVar = 100;

    // ---------------- Static (Class) Variable ----------------
    static int staticVar = 200;

    // ---------------- Method Demonstrating Local Variable ----------------
    void showLocalScope() {

        // Local variable
        int localVar = 50;

        System.out.println("Inside showLocalScope()");
        System.out.println("Local Variable: " + localVar);
        System.out.println("Instance Variable: " + instanceVar);
        System.out.println("Static Variable: " + staticVar);

        // localVar exists ONLY inside this method
    }

    // ---------------- Another Method ----------------
    void modifyVariables() {

        // Local variable
        int localVar = 10;

        // Modifying instance and static variables
        instanceVar += 10;
        staticVar += 10;

        System.out.println("\nInside modifyVariables()");
        System.out.println("Local Variable: " + localVar);
        System.out.println("Modified Instance Variable: " + instanceVar);
        System.out.println("Modified Static Variable: " + staticVar);
    }

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== SCOPE OF VARIABLES IN JAVA ====================");
        System.out.println("""
The SCOPE of a variable defines:
✔ Where the variable can be accessed
✔ Where it exists in memory
✔ How long it lives

Java variables are mainly classified as:
1. Local variables
2. Instance (Global) variables
3. Static (Class) variables
""");


        // ---------------- Local Variables ----------------
        System.out.println("\n==================== LOCAL VARIABLES ====================");
        System.out.println("""
Local variables are:
✔ Declared inside methods, blocks, or constructors
✔ Accessible ONLY within that block
✔ Created when method is called
✔ Destroyed when method ends

They DO NOT get default values.
They MUST be initialized before use.
""");

        // Creating object to access instance methods
        ScopeOfVariablesInJava obj = new ScopeOfVariablesInJava();

        obj.showLocalScope();


        // ---------------- Instance (Global) Variables ----------------
        System.out.println("\n==================== INSTANCE (GLOBAL) VARIABLES ====================");
        System.out.println("""
Instance variables are:
✔ Declared inside class
✔ Outside all methods
✔ Belong to an object
✔ Each object has its own copy

They get DEFAULT values automatically.
""");

        System.out.println("Accessing instance variable using object:");
        System.out.println("obj.instanceVar = " + obj.instanceVar);


        // ---------------- Static Variables ----------------
        System.out.println("\n==================== STATIC VARIABLES ====================");
        System.out.println("""
Static variables are:
✔ Declared using static keyword
✔ Belong to the class
✔ Shared among all objects
✔ Only ONE copy exists

They are loaded once when class loads.
""");

        System.out.println("Accessing static variable using class name:");
        System.out.println("VariableScope.staticVar = " + ScopeOfVariablesInJava.staticVar);


        // ---------------- Modifying Variables ----------------
        System.out.println("\n==================== VARIABLE MODIFICATION ====================");
        System.out.println("""
Now we modify variables using a method call
to observe scope behavior.
""");

        obj.modifyVariables();


        // ---------------- Object Behavior ----------------
        System.out.println("\n==================== OBJECT BEHAVIOR ====================");
        System.out.println("""
Creating another object to observe instance vs static behavior.
""");

        ScopeOfVariablesInJava obj2 = new ScopeOfVariablesInJava();

        System.out.println("obj2.instanceVar (new object): " + obj2.instanceVar);
        System.out.println("staticVar (shared): " + ScopeOfVariablesInJava.staticVar);


        // ---------------- Scope Summary Table ----------------
        System.out.println("\n==================== SCOPE SUMMARY ====================");
        System.out.println("""
LOCAL VARIABLES:
✔ Scope → Inside method/block
✔ Lifetime → Method execution
✔ Memory → Stack
✔ Default value → NO

INSTANCE VARIABLES:
✔ Scope → Entire class
✔ Lifetime → Object lifetime
✔ Memory → Heap
✔ Default value → YES

STATIC VARIABLES:
✔ Scope → Entire class
✔ Lifetime → Program lifetime
✔ Memory → Method area
✔ Default value → YES
""");


        // ---------------- Common Mistakes ----------------
        System.out.println("\n==================== COMMON MISTAKES ====================");
        System.out.println("""
✘ Using local variable without initialization
✘ Assuming local variable is shared
✘ Confusing instance and static variables
✘ Accessing instance variable without object
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD MAPPING ====================");
        System.out.println("""
Local Variable:
✔ Temporary calculation (bill total)

Instance Variable:
✔ Account balance (per user)

Static Variable:
✔ Bank interest rate (same for all users)
""");


        // ---------------- What Comes Next ----------------
        System.out.println("\n==================== WHAT COMES NEXT ====================");
        System.out.println("""
Next important topics:

✔ Passing variables to methods
✔ Passing arrays to methods
✔ Variable shadowing
✔ Lifetime of variables
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Scope defines where a variable is accessible.
→ Local variables exist only inside methods.
→ Instance variables belong to objects.
→ Static variables are shared across class.
→ Understanding scope prevents bugs.

Variable scope is CRITICAL for clean Java programs.
""");
    }
}
