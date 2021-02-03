import os
import requests

def get_quotes():
    url = 'http://quotes.stormconsultancy.co.uk/quotes.json'
    r = requests.get(url)
    quotes = r.json()
    quotes_list = []
    for i in range(len(quotes['quotes'])):
        quotes_list.append(quotes['quotes'][i])
    return quotes_list