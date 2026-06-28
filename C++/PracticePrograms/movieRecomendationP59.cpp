/*
Program: Netflix Recommendation Engine
Description: Searches movie and displays rating, genre, and recommendation.
*/

#include <iostream>
using namespace std;

int main() {

    string movieNames[5] = {"Jawan","Dangal","Animal","Interstellar","Drishyam"};
    string movieGenre[5] = {"Action","Sports","Action","SciFi","Thriller"};
    string searchMovie;

    float movieRating[5] = {8.2,9.1,7.5,9.3,8.8};

    cout << "Enter Movie Name: ";
    cin >> searchMovie;

    for(int index = 0; index < 5; index++) {
        if(searchMovie == movieNames[index]) {

            cout << "\nMovie Found\n";
            cout << "Genre : " << movieGenre[index] << endl;
            cout << "Rating : " << movieRating[index] << endl;

            if(movieRating[index] >= 9)
                cout << "⭐⭐ Must Watch\n";
            else if(movieRating[index] >= 8)
                cout << "⭐ Recommended\n";
            else
                cout << "Average Movie\n";
        }
    }

    return 0;
}
