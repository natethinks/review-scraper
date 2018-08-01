from bs4 import BeautifulSoup

import requests
import re

page = requests.get('https://www.dealerrater.com/dealer/McKaig-Chevrolet-Buick-A-Dealer-For-The-People-dealer-reviews-23685/page2/?filter=ALL_REVIEWS#link')
soup = BeautifulSoup(page.content, 'lxml')
print(type((soup)))

# need a dictionary for all of the things that I care about, and then it will be a list of dictionaries to loop through
i = 0

reviews = []

# lets give this a perfect bool in the dict, if they miss a single star point it can't be perfect
for review in soup.find_all(class_="review-entry"):
    # define a new dictionary to hold all the things I care about
    # just a bunch of find commands? or maybe keep a list of things i'm interested in so it can be another loop
    print(type((review)))
    review_text = review.find(class_="review-content").get_text()
    for rating in review.find_all(class_="rating-static"):
        rating_num = re.search(r'rating-(\d+)', str(rating))
        print(rating_num.group(1)) # matches only the number of all involved reviews
    
    i = i+1
    # append the dictionary to a list of dictionaries
    review_dict = {'review_text': review_text}
    #print(review_dict['review_text'])
    reviews.append(review_dict)
    if i == 2:
        break
print(reviews)
#print(soup.find(id="reviews").prettify())
