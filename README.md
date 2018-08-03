# review-scraper
Python microservice for web scraping reviews and determining the likelihood that a review is fake.

Scraping is done using beautiful soup, fake likelihood calculation is done using proprietary website information and nltk sentiment processing on the review text.

### Installation
Clone the repo
``` 
git clone https://github.com/natethinks/review-scraper.git
```

Download data required for NLP (natural language processing)
```
python3
import nltk
nltk.download()
```

### Run
Build the image and tag it as scraper, name can be changed to anything
```
docker build -t scraper .
```
Mount the volume with the nltk_data for NLP
```
docker run -v /Users/$USER/nltk_data/:/root/nltk_data/ scraper
```

### Testing
```
pip3 install -r requirements.txt
python3 scrape_test.py
```

### To-do
- In app health reporting (prometheus)
- Support retrieving addresses to be scraped from kafka or rabbitmq
- Multiple stratgies for determining fake reviews
- Custom NLP model for reviews
- More error catches and handling
