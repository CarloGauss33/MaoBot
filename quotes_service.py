import json
import random

class QuotesService:
    def __init__(self, quotes_path):
        self.quotes_path = quotes_path
        self.__load_quotes()

    def __load_quotes(self):
        with open(self.quotes_path, 'r') as file:
            self.quotes = json.load(file)

    def random_quote(self):
        return self.quotes[random.randint(0, len(self.quotes) - 1)]