import json

class Movie:
    """A class to represent a movie in a movies library."""

    def __init__(self, title, author, year, characters):
        """Initialize the movie."""
        self.title = title
        self.author = author
        self.year = year
        self.characters = characters

    def to_json(self):
        """Return a JSON representation of the movie."""
        return json.dumps(self.__dict__)