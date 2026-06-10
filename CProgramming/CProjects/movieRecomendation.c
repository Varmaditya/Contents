/*---------------------------------------------------------
    Project Title : Movie Recommendation System
    Description : A console based movie and series recommendation system
                  that allows users to:
        1. View all content
        2. Search by title
        3. Search by genre
        4. Show top rated content
        5. Recommend content
        6. Sort by rating
        7. Exit
    Concepts Used : Structures, Arrays, Strings, Functions,
                    Loops, Conditionals, Searching, Sorting
---------------------------------------------------------*/

#include <stdio.h>
#include <string.h>

struct Movie {
    int id;
    char title[50];
    char genre[20];
    char language[20];
    char type[20];
    float rating;
};

struct Movie m[] = {
    {101, "3 Idiots", "Comedy", "Hindi", "Movie", 8.4},
    {102, "Dangal", "Drama", "Hindi", "Movie", 8.5},
    {103, "Drishyam", "Thriller", "Hindi", "Movie", 8.3},
    {104, "Chhichhore", "Comedy", "Hindi", "Movie", 8.2},
    {201, "Panchayat", "Drama", "Hindi", "Series", 9.0},
    {202, "Mirzapur", "Crime", "Hindi", "Series", 8.6},
    {203, "Aspirants", "Drama", "Hindi", "Series", 9.1},
    {301, "Interstellar", "SciFi", "English", "Movie", 8.7},
    {302, "Inception", "SciFi", "English", "Movie", 8.8},
    {303, "Dark Knight", "Action", "English", "Movie", 9.0},
    {401, "Breaking Bad", "Crime", "English", "Series", 9.5},
    {402, "Dark", "SciFi", "English", "Series", 8.8}
};

int n = sizeof(m) / sizeof(m[0]);

/*---------------------------------------------------
    Function : displayAll
    Purpose  : Display all movies and series
---------------------------------------------------*/
void displayAll() {
    int i;

    printf("\n------------------------------------------------------------\n");
    printf("ID\tTITLE\t\tLANGUAGE\tTYPE\tRATING\n");
    printf("------------------------------------------------------------\n");

    for(i = 0; i < n; i++) {
        printf("%d\t%-15s\t%-10s\t%-8s %.1f\n", m[i].id, m[i].title,
               m[i].language, m[i].type, m[i].rating);
    }
}

/*---------------------------------------------------
    Function : searchTitle
    Purpose  : Search content by title
---------------------------------------------------*/
void searchTitle() {
    char name[50];
    int i, found = 0;

    printf("Enter Title : ");
    scanf(" %[^\n]", name);

    for(i = 0; i < n; i++) {
        if(strcmp(name, m[i].title) == 0) {
            printf("\nFound!\n");
            printf("Title    : %s\n", m[i].title);
            printf("Genre    : %s\n", m[i].genre);
            printf("Language : %s\n", m[i].language);
            printf("Type     : %s\n", m[i].type);
            printf("Rating   : %.1f\n", m[i].rating);

            found = 1;
            break;
        }
    }

    if(found == 0)
        printf("Content Not Found!\n");
}

/*---------------------------------------------------
    Function : searchGenre
    Purpose  : Search by genre
---------------------------------------------------*/
void searchGenre() {
    char genre[20];
    int i;

    printf("Enter Genre : ");
    scanf("%s", genre);

    printf("\nRecommendations:\n");

    for(i = 0; i < n; i++) {
        if(strcmp(genre, m[i].genre) == 0) {
            printf("- %s\n", m[i].title);
        }
    }
}

/*---------------------------------------------------
    Function : topRated
    Purpose  : Show top rated content
---------------------------------------------------*/
void topRated() {
    int i;

    printf("\nTop Rated Content\n");

    for(i = 0; i < n; i++) {
        if(m[i].rating >= 8.8) {
            printf("%s (%.1f)\n", m[i].title, m[i].rating);
        }
    }
}

/*---------------------------------------------------
    Function : recommendMovie
    Purpose  : Recommend based on language
---------------------------------------------------*/
void recommendMovie() {
    int choice,i;

    printf("\n1. Hindi\n");
    printf("2. English\n");

    printf("Choose Language : ");
    scanf("%d", &choice);

    printf("\nRecommended For You\n");

    for(i = 0; i < n; i++) {
        if(choice == 1 && strcmp(m[i].language, "Hindi") == 0 && m[i].rating >= 8.5) {
            printf("%s\n",m[i].title);
        }

        if(choice==2 && strcmp(m[i].language, "English") == 0 && m[i].rating >= 8.5) {
            printf("%s\n", m[i].title);
        }
    }
}

/*---------------------------------------------------
    Function : sortRating
    Purpose  : Sort content by rating
---------------------------------------------------*/
void sortRating() {
    int i, j;
    struct Movie temp;

    for(i = 0; i < n-1; i++) {
        for(j = 0; j < n-i-1; j++) {
            if(m[j].rating < m[j+1].rating) {
                temp = m[j];
                m[j] = m[j+1];
                m[j+1] = temp;
            }
        }
    }

    printf("\nSorted By Rating (High to Low)\n");

    for(i = 0; i < n; i++) {
        printf("%s (%.1f)\n", m[i].title, m[i].rating);
    }
}

/*---------------------------------------------------
    Function : rateMovie
    Purpose  : Update movie rating
---------------------------------------------------*/
void rateMovie() {
    int id, i;
    float rating;

    printf("Enter Content ID : ");
    scanf("%d", &id);

    for(i = 0; i < n; i++) {
        if(m[i].id==id) {
            printf("Enter New Rating : ");
            scanf("%f", &rating);

            m[i].rating = rating;

            printf("Rating Updated Successfully!\n");
            return;
        }
    }

    printf("Content Not Found!\n");
}

/*---------------------------------------------------
    Main Function
---------------------------------------------------*/
int main() {
    int choice;

    do {
        printf("\n\n");
        printf("========================================\n");
        printf("      MOVIE RECOMMENDATION SYSTEM\n");
        printf("========================================\n");

        printf("1. View All Content\n");
        printf("2. Search By Title\n");
        printf("3. Search By Genre\n");
        printf("4. Top Rated Content\n");
        printf("5. Recommend For Me\n");
        printf("6. Sort By Rating\n");
        printf("7. Rate Content\n");
        printf("8. Exit\n\n");

        printf("Enter Choice : ");
        scanf("%d",&choice);

        switch(choice) {
            case 1:
                displayAll();
                break;
            case 2:
                searchTitle();
                break;
            case 3:
                searchGenre();
                break;
            case 4:
                topRated();
                break;
            case 5:
                recommendMovie();
                break;
            case 6:
                sortRating();
                break;
            case 7:
                rateMovie();
                break;
            case 8:
                printf("Thank You!\n");
                break;
            default:
                printf("Invalid Choice!\n");
        }

    } while(choice != 8);

    return 0;
}
