// Program: Attendance Counter

public class AttendanceCounterP35 {
    public static void main(String[] args) {

        boolean[] attendance = {true, true, false, true, false};
        int present = 0;

        for (boolean status : attendance) {
            if (status) {
                present++;
            }
        }

        System.out.println("Students present: " + present);
    }
}
