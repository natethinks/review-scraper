from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk
from urllib.request import urlopen

import requests
import re

sid = SentimentIntensityAnalyzer()

def check_network():
    try:
        urllib2.urlopen('http://216.58.192.142', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def scrape_pages():
    for i in range(1, 6):
        page = requests.get(('https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page{}/?filter=ALL_REVIEWS#link').format(i))
        parse_content(page)


    reviews = []

    for review in soup.find_all(class_="review-entry"):
        # just a bunch of find commands? or maybe keep a list of things i'm interested in so it can be another loop
        review_text = review.find(class_="review-content").get_text()
        perfect_score = True

        ratings = review.find_all(class_="rating-static")
        ratings_count = len(ratings)

        # use a tuple to store ratings, tuples don't have duplicates, if the length is 1 and the only element is 50 then it gets a perfect score
        for rating in ratings:
            rating_num = re.search(r'rating-(\d+)', str(rating))
            if rating_num.group(1) != 50:
                perfect_score = False
    
        review_dict = {'review_text': review_text, 'perfect_score': perfect_score, 'ratings_count': ratings_count}
        reviews.append(review_dict)
        print(reviews)
#print(soup.find(id="reviews").prettify())

def parse_content(page):
    soup = BeautifulSoup(page.content, 'lxml')
    print(page)

def process_sentiment(text):
     print(text)
     ss = sid.polarity_scores(text)
     for k in ss:
         print('{0}: {1}, '.format(k, ss[k]))
     print()


if __name__ == "__main__":
    nltk.download('vader_lexicon')
    process_sentiment("this book is great at being terrible")
    #check_network()
    #scrape_pages()
    

