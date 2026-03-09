// Program: Quiz Game

import java.util.Scanner;

class Question {

    String question;
    String answer;

    Question(String q, String a) {
        question = q;
        answer = a;
    }

    boolean check(String input) {
        return answer.equalsIgnoreCase(input);
    }
}

public class QuizP85 {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        Question[] quiz = {
                new Question("Capital of France?", "Paris"),
                new Question("5 + 7 ?", "12"),
                new Question("Java creator?", "Gosling")
        };

        int score = 0;

        for (Question q : quiz) {

            System.out.println(q.question);
            String ans = sc.nextLine();

            if (q.check(ans))
                score++;
        }

        System.out.println("Score: " + score);

        sc.close();
    }
}