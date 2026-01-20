// Program: Daily Temperature Tracker

public class TemperatureTrackerP53 {
    public static void main(String[] args) {

        int[] temps = {32, 35, 30, 28, 36, 34, 31};

        int max = temps[0], min = temps[0];

        for (int t : temps) {
            if (t > max) max = t;
            if (t < min) min = t;
        }

        System.out.println("Highest Temperature: " + max);
        System.out.println("Lowest Temperature: " + min);
    }
}
