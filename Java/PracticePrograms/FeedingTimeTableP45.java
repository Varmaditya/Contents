// Program: Display Feeding Time Table for Dinosaur Park

public class FeedingTimeTableP45 {

    public static void main(String[] args) {

        // 12 hours schedule
        System.out.println("With 12 hours time schedule:\n");
        int feedAmountAlamo = 120;
        int feedAmountEuropa = 90;

        for( int time = 0; time < 24; time++) {

            if (time == 6 || time == 12 || time == 18 || time == 23) {
                if (time <= 12) {
                    System.out.println("Its " + time + " AM, feeding time for Alamosaurus with " + feedAmountAlamo + " kg of food.");
                } else {
                    System.out.println("Its " + (time - 12) + " PM, feeding time for Alamosaurus with " + feedAmountAlamo + " kg of food.");
                }
            }
            if (time == 8 || time == 15 || time == 20) {
                if (time <= 12){
                    System.out.println("Its " + time + " AM, feeding time for Europasaurus with " + feedAmountEuropa + " kg of food.");
                } else {
                    System.out.println("Its " + (time-12) + " PM, feeding time for Europasaurus with " + feedAmountEuropa + " kg of food.");
                }
            }
        }

        // 24 hours schedule.
        System.out.println("\nWith 24 hours time schedule:\n");

        for (int timer = 0; timer < 24; timer++) {
            if (timer == 6 || timer == 12 || timer == 18 || timer == 23) {
                System.out.println("It's " + timer + ":00 - Feeding time for Alamosaurus with " + feedAmountAlamo + "kg of food");
            }
            if (timer == 8 || timer == 15 || timer == 20) {
                System.out.println("It's " + timer + ":00 - Feeding time for Europasaurus with " + feedAmountEuropa + "kg of food");
            }
        }
    }
}
