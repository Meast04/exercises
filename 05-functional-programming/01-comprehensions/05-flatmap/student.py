def genres(movies):
    return {movie.genre for movie in movies}

def actors(movies):
    return {movie.genre for movie in movies}

def repeat_consecutive(xs, n):
    return {x*n for x in xs}