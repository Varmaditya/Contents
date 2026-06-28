/*
Program: Movie Recommendation System
Description: A simple Netflix-like recommendation system using
Class, Objects, Arrays, Strings, Loops and Conditionals.
*/

#include <iostream>
using namespace std;

class MovieSystem {
private:

    string title[10] = {
        "Interstellar", "Avengers", "Breaking Bad", "Dark", "Jawan",
        "3 Idiots", "Animal", "Panchayat", "Mirzapur", "Scam 1992"
    };

    string genre[10] = {
        "Sci-Fi", "Action", "Crime", "Sci-Fi", "Action",
        "Comedy", "Action", "Comedy", "Crime","Drama"
    };

    string language[10] = {
        "Hollywood", "Hollywood", "Hollywood","Hollywood", "Bollywood",
        "Bollywood", "Bollywood", "Bollywood", "Bollywood", "Bollywood"
    };

    string type[10] = {
        "Movie", "Movie", "Series", "Series", "Movie",
        "Movie", "Movie", "Series", "Series", "Series"
    };

    float rating[10] = {9.3,8.8,9.5,9.1,8.2,9.4,7.5,9.0,8.7,9.6};

public:

    void menu() {
        cout << "\n\n========== MOVIE HUB ==========\n";
        cout << "1. View All Titles\n";
        cout << "2. Search Title\n";
        cout << "3. Browse Genre\n";
        cout << "4. Top Rated\n";
        cout << "5. Recommend Me\n";
        cout << "6. Exit\n";
    }

    void viewAll() {
        cout << "\n------ Library ------\n";

        for(int i=0;i<10;i++) {
            cout << i+1 << ". " << title[i] << " (" << type[i] << ")\n";
        }
    }

    void searchTitle() {
        string search;

        cout << "Enter Title: ";
        cin.ignore();
        getline(cin,search);

        for(int i=0;i<10;i++) {
            if(search==title[i]) {
                cout<<"\nFound!\n";
                cout<<"Title : "<<title[i]<<endl;
                cout<<"Type : "<<type[i]<<endl;
                cout<<"Genre : "<<genre[i]<<endl;
                cout<<"Language : "<<language[i]<<endl;
                cout<<"Rating : "<<rating[i]<<"/10\n";
                return;
            }
        }

        cout<<"\nTitle Not Found!\n";
    }

    void browseGenre() {
        string searchGenre;

        cout<<"Enter Genre: ";
        cin>>searchGenre;

        cout<<"\nRecommendations\n";

        for(int i=0;i<10;i++) {
            if(searchGenre==genre[i]) {
                cout<<title[i] <<" ("<<rating[i]<<")\n";
            }
        }
    }

    void topRated() {
        cout<<"\n⭐⭐ Top Rated ⭐⭐\n";

        for(int i=0;i<10;i++) {
            if(rating[i]>=9.0) {
                cout<<title[i] <<" - " <<rating[i] <<endl;
            }
        }
    }

    void recommend() {
        string lang;
        string searchGenre;

        cout<<"Preferred Language: ";
        cin>>lang;

        cout<<"Preferred Genre: ";
        cin>>searchGenre;

        cout<<"\nRecommended For You\n";

        for(int i=0;i<10;i++) {
            if(language[i]==lang && genre[i]==searchGenre) {
                cout<<"\n🎬 "<<title[i]<<endl;
                cout<<"Type : "<<type[i]<<endl;
                cout<<"Rating : "<<rating[i]<<"/10\n";
                return;
            }
        }

        cout<<"\nNo Recommendation Available.\n";
    }

};

int main() {
    system("chcp 65001");
    MovieSystem netflix;

    int choice;

    do {
        netflix.menu();

        cout<<"\nEnter Choice: ";
        cin>>choice;

        switch(choice) {
            case 1:
                netflix.viewAll();
                break;
            case 2:
                netflix.searchTitle();
                break;
            case 3:
                netflix.browseGenre();
                break;
            case 4:
                netflix.topRated();
                break;
            case 5:
                netflix.recommend();
                break;
            case 6:
                cout<<"\nEnjoy Your Show! 🍿\n";
                break;
            default:
                cout<<"\nInvalid Choice!\n";
        }
    } while(choice!=6);

    return 0;
}
