# recommender.py

import random

def recommend(movies, genre):
    filtered = []

    for movie in movies:
        if movie.genre.lower() == genre.lower():
            filtered.append(movie)

    if filtered:
        return random.choice(filtered)

    return None