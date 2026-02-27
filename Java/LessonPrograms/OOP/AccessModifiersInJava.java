// Program: Access Modifiers, Static & Final in Java (Detailed)

class Demo {

    // ---------------- Access Modifiers ----------------
    public String publicVar = "Public Variable";
    private String privateVar = "Private Variable";
    protected String protectedVar = "Protected Variable";
    String defaultVar = "Default Variable";

    // ---------------- Static Variable ----------------
    static int staticCounter = 0;

    // ---------------- Final Variable ----------------
    final double PI = 3.14159;

    // ---------------- Static Block ----------------
    static {
        System.out.println("Static Block Executed (Class Loaded)");
        staticCounter = 100;
    }

    // ---------------- Constructor ----------------
    Demo() {
        staticCounter++;
    }

    // ---------------- Static Method ----------------
    static void showStaticInfo() {
        System.out.println("Static Method Called");
        System.out.println("Static Counter = " + staticCounter);
    }

    // ---------------- Non-Static Method ----------------
    void showDetails() {
        System.out.println("Public: " + publicVar);
        System.out.println("Private: " + privateVar);
        System.out.println("Protected: " + protectedVar);
        System.out.println("Default: " + defaultVar);
        System.out.println("Final PI value: " + PI);
    }
}

public class AccessModifiersInJava {

    public static void main(String[] args) {

        // ---------------- Introduction ----------------
        System.out.println("\n==================== ACCESS MODIFIERS ====================");
        System.out.println("""
Access Modifiers control visibility of:
✔ Variables
✔ Methods
✔ Classes

Types:
✔ public      → Accessible everywhere
✔ private     → Accessible only inside class
✔ protected   → Accessible within package + subclass
✔ default     → Accessible within package
""");


        // ---------------- Creating Object ----------------
        Demo obj1 = new Demo();
        Demo obj2 = new Demo();

        System.out.println("\n==================== ACCESSING VARIABLES ====================");
        obj1.showDetails();


        // ---------------- Static Keyword ----------------
        System.out.println("\n==================== STATIC KEYWORD ====================");
        System.out.println("""
static means:
✔ Belongs to class
✔ Shared by all objects
✔ Only one copy exists

Accessed using:
ClassName.variableName
""");

        Demo.showStaticInfo();


        // ---------------- Static Variable ----------------
        System.out.println("\n==================== STATIC VARIABLE ====================");
        System.out.println("""
Static variable:
✔ Shared across all objects
✔ Changes reflect everywhere
✔ Loaded once when class loads
""");

        System.out.println("Static Counter from obj1: " + Demo.staticCounter);
        System.out.println("Static Counter from obj2: " + Demo.staticCounter);


        // ---------------- Static Method ----------------
        System.out.println("\n==================== STATIC METHOD ====================");
        System.out.println("""
Static method:
✔ Belongs to class
✔ Cannot access non-static members directly
✔ Can be called without creating object
""");

        Demo.showStaticInfo();


        // ---------------- Static Block ----------------
        System.out.println("\n==================== STATIC BLOCK ====================");
        System.out.println("""
Static block:
✔ Executes only once
✔ Runs when class loads
✔ Used for initialization
✔ Runs before main()
""");


        // ---------------- Final Keyword ----------------
        System.out.println("\n==================== FINAL KEYWORD ====================");
        System.out.println("""
final means:
✔ Constant variable (cannot change)
✔ Final method (cannot override)
✔ Final class (cannot inherit)

Example:
final double PI = 3.14159;
""");


        // ---------------- Why Use Static & Final ----------------
        System.out.println("\n==================== WHY USE STATIC & FINAL ====================");
        System.out.println("""
Use static:
✔ For common shared data
✔ Utility methods
✔ Counters

Use final:
✔ To create constants
✔ To prevent modification
✔ To increase security
""");


        // ---------------- Real-World Mapping ----------------
        System.out.println("\n==================== REAL-WORLD EXAMPLE ====================");
        System.out.println("""
Static:
✔ Bank interest rate (same for all)

Final:
✔ ATM PIN (constant)
✔ Mathematical constants

Access modifiers:
✔ Locker system (restricted access)
""");


        // ---------------- Summary ----------------
        System.out.println("\n==================== SUMMARY ====================");
        System.out.println("""
→ Access modifiers control visibility.
→ static belongs to class.
→ Static variables are shared.
→ Static methods belong to class.
→ Static block runs once at class loading.
→ final prevents modification or inheritance.

These features improve structure and control in Java.
""");
    }
}