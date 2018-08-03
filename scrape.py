from bs4 import BeautifulSoup
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from urllib.request import urlopen
import requests
import re
import nltk

class Scraper():
    """Scrape a webpage for reviews, process the review, and determine which reviews are most likely to be fake."""

    def __init__(self):
        self.url = 'https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page{}/?filter=ALL_REVIEWS#link'
        self.sid = SentimentIntensityAnalyzer()

    def check_network(self):
        """Test for successful outbound network connection."""
        try:
            urlopen('http://216.58.192.142', timeout=1)
            return True
        except urllib2.URLError as err: 
            return False

    def get_pages(self):
        """HTTP request to retrieve pages, uses hardcode range for multiple pages of reviews"""
        pages = []
        for i in range(1, 6):
            page = requests.get((self.url).format(i))
            pages.append(page)
        return pages

    def process_reviews(self, pages):
        """Ties together other class functions to generate list of dictionaries containing all processed review data"""
        reviews = []
        for page in pages:
            soup = BeautifulSoup(page.content, 'lxml')
            for review in soup.find_all(class_="review-entry"):
                review_text = review.find(class_="review-content").get_text()
                perfect_score = True

                ratings = review.find_all(class_="rating-static")
                ratings_count = len(ratings)
                sentiment = self.process_sentiment(review_text)

                for rating in ratings:
                    rating_num = re.search(r'rating-(\d+)', str(rating))
                    if rating_num.group(1) != "50":
                        perfect_score = False
            
                review_dict = {'review_text': review_text, 'perfect_score': perfect_score, 'ratings_count': ratings_count, 'positive_score': sentiment['pos']}
                reviews.append(review_dict)
        return reviews

    def process_sentiment(self, text):
        """Runs sentiment using NLTK vader to determine positive, negative, and neutral score of the review text, currently only positive is used"""
        ss = self.sid.polarity_scores(text)
        return ss

    def remove_imperfect_scored_reviews(self, reviews):
        """List comprehension to remove all reviews without perfect start ratings, if less than 3 such reviews exist, it returns the original review array"""
        perfect_reviews = [x for x in reviews if x['perfect_score'] == True]
        if len(perfect_reviews) > 3:
            return perfect_reviews
        else:
            return reviews

    def get_fakes(self, reviews):
        """Returns the top 3 reviews most likely to be fake as determined by highest sentiment scores and perfect star ratings"""
        newList = self.remove_imperfect_scored_reviews(reviews)
        newlist = sorted(reviews, key=lambda k: k['positive_score'], reverse=True)
        return newlist
