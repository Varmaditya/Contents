// Program: Shapes information.

import java.util.Scanner;

// Abstract class
abstract class Shape {

    public abstract double calculateArea();

    public abstract double calculatePerimeter();
}


// Rectangle
class Rectangle extends Shape {

    private double length, width;

    Rectangle(double length, double width) {
        this.length = length;
        this.width = width;
    }

    public double calculateArea() {
        return length * width;
    }

    public double calculatePerimeter() {
        return 2 * (length + width);
    }
}


// Circle
class Circle extends Shape {

    private double radius;

    Circle(double radius) {
        this.radius = radius;
    }

    public double calculateArea() {
        return Math.PI * radius * radius;
    }

    public double calculatePerimeter() {
        return 2 * Math.PI * radius;
    }
}


// Square
class Square extends Shape {

    private double side;

    Square(double side) {
        this.side = side;
    }

    public double calculateArea() {
        return side * side;
    }

    public double calculatePerimeter() {
        return 4 * side;
    }
}


// Triangle
class Triangle extends Shape {

    private double a, b, c;

    Triangle(double a, double b, double c) {
        this.a = a;
        this.b = b;
        this.c = c;
    }

    public double calculatePerimeter() {
        return a + b + c;
    }

    public double calculateArea() {

        double s = calculatePerimeter() / 2;

        return Math.sqrt(s * (s - a) * (s - b) * (s - c));
    }
}


// Main class
public class ShapesP90 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        while (true) {

            System.out.println("\n==== Shape Calculator ====");
            System.out.println("1. Rectangle");
            System.out.println("2. Circle");
            System.out.println("3. Square");
            System.out.println("4. Triangle");
            System.out.println("5. Exit");
            System.out.print("Choose shape: ");

            int choice = sc.nextInt();

            Shape shape = null;

            switch (choice) {

                case 1:
                    System.out.print("Enter length: ");
                    double length = sc.nextDouble();

                    System.out.print("Enter width: ");
                    double width = sc.nextDouble();

                    shape = new Rectangle(length, width);
                    break;

                case 2:
                    System.out.print("Enter radius: ");
                    double radius = sc.nextDouble();

                    shape = new Circle(radius);
                    break;

                case 3:
                    System.out.print("Enter side: ");
                    double side = sc.nextDouble();

                    shape = new Square(side);
                    break;

                case 4:
                    System.out.print("Enter side A: ");
                    double a = sc.nextDouble();

                    System.out.print("Enter side B: ");
                    double b = sc.nextDouble();

                    System.out.print("Enter side C: ");
                    double c = sc.nextDouble();

                    shape = new Triangle(a, b, c);
                    break;

                case 5:
                    System.out.println("Exiting...");
                    sc.close();
                    return;

                default:
                    System.out.println("Invalid choice");
                    continue;
            }

            System.out.println("\nArea: " + shape.calculateArea());
            System.out.println("Perimeter: " + shape.calculatePerimeter());
        }
    }
}