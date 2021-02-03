import os
import requests

def get_quotes():
    url = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    r = requests.get(url)
    quotes = r.json()
    quotes_list = [i for i in quotes]
    return quotes_list