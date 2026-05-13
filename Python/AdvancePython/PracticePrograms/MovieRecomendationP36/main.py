# main.py for movie recommendation program

from movie import Movie
from recommender import recommend

movies = [
    Movie("Interstellar", "Sci-Fi"),
    Movie("Batman", "Action"),
    Movie("Frozen", "Animation")
]

genre = input("Enter genre: ")

movie = recommend(movies, genre)

if movie:
    print("Recommended Movie:", movie.name)
else:
    print("No movie found!")