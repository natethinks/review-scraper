from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from urllib.request import urlopen
from scrape import Scraper

import requests
import re

if __name__ == "__main__":
    scraper = Scraper()
    if scraper.check_network() == False:
        print("network error")
    pages = scraper.get_pages()
    reviews = scraper.process_reviews(pages)
    scraper.print_fakes(reviews)
    

