import random

class Quote:
    """
    A class that stores a dictionary of quotes and print 1 of them randomly

    Attributes:
        quotes (list): A list of quotes

    Methods:
        get_random_quote: Returns a random quote from the list
    """

    def __init__(self, quotes):
        """
        Initializes the class with a list of quotes
        
        Args:
            quotes (list): A list of quotes
        """
        self.quotes = quotes

    def get_random_quote(self):
        """Returns a random quote from the list"""
        return random.choice(self.quotes)