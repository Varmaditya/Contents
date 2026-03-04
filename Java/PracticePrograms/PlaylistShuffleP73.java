// Program: Playlist Shuffle

public class PlaylistShuffleP73 {

    static void shuffle(String[] songs) {

        for (int i = 0; i < songs.length; i++) {

            int j = (int)(Math.random() * songs.length);

            String temp = songs[i];
            songs[i] = songs[j];
            songs[j] = temp;
        }
    }

    static void printSongs(String[] songs) {

        for (String s : songs)
            System.out.println(s);
    }

    public static void main(String[] args) {

        String[] songs = {"SongA","SongB","SongC","SongD"};

        shuffle(songs);

        System.out.println("Shuffled Playlist:");
        printSongs(songs);
    }
}