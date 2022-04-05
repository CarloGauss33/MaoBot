import requests
import bs4
import json


class MaoScrapper:
    def __init__(self):
        self.file_name = 'quotes.html'
        self.quotes = []
        self.parsed_file = None
        self.__get_parsed_file()
        self.quotes = self.__get_quotes()

    def dump_quotes_in_json(self, json_filepath):
        with open(json_filepath, 'w') as file:
            json.dump(self.quotes, file, indent=2)

    def __get_parsed_file(self):
        with open(self.file_name, 'r') as file:
            self.parsed_file = bs4.BeautifulSoup(file.read(), 'html.parser')

    def __get_quotes(self):
        quotes = []
        for paragraph in self.parsed_file.find_all('p'):
            quote = paragraph.find('quote').text
            context = paragraph.find('context').text
            context = context.replace('\ufffd', '')
            quotes.append({'quote': quote, 'context': context})
        return quotes

maoScrapper = MaoScrapper()
print(maoScrapper.quotes)
maoScrapper.dump_quotes_in_json('quotes.json')