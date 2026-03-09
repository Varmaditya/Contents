// Program: Elevator Simulator

class Elevator {

    int floor = 0;

    void moveUp() {
        floor++;
    }

    void moveDown() {
        if (floor > 0)
            floor--;
    }

    void display() {
        System.out.println("Current Floor: " + floor);
    }
}

public class ElevatorSimulatorP82 {

    public static void main(String[] args) {

        Elevator e = new Elevator();

        e.moveUp();
        e.moveUp();
        e.moveDown();
        e.display();
    }
}