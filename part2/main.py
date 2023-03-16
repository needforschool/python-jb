import json
from movie import Movie

# Create a movie
movie = Movie(
    "La reine des neiges",
    "Disney",
    2013,
    [
        "Anna",
        "Elsa",
        "Kristoff",
        "Olaf",
        "Sven"
    ]
)

# Print the movie
print(movie.to_json())