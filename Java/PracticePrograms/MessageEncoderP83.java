// Program: Secret Message Encoder

class Encoder {

    String encode(String msg) {

        String result = "";

        for (char c : msg.toCharArray())
            result += (char)(c + 1);

        return result;
    }
}

public class MessageEncoderP83 {

    public static void main(String[] args) {

        Encoder e = new Encoder();

        System.out.println(e.encode("JAVA"));
    }
}