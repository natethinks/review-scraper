import unittest
from scrape import Scraper

class ScraperTest(unittest.TestCase):

    def setUp(self):
        self.scraper = Scraper()
        self.pages = self.scraper.get_pages()

    def test_get_pages(self):
        self.assertEqual(len(self.pages), 5)

    def test_process_reviews(self):
        reviews = self.scraper.process_reviews(self.pages)
        self.assertEqual(len(reviews), 50)
        review = reviews[0]
        self.assertTrue('review_text' in review.keys())
        self.assertTrue('perfect_score' in review.keys())
        self.assertTrue('ratings_count' in review.keys())
        self.assertTrue('positive_score' in review.keys())

    def test_remove_imperfect_score(self):
        reviews = self.scraper.process_reviews(self.pages)
        perfect_scores = self.scraper.remove_imperfect_scored_reviews(reviews)
        for review in perfect_scores:
            self.assertTrue(review['perfect_score'])

    def test_process_sentiment(self):
        posText = "This sentence is pretty good!"
        posExpected  = {'neg': 0.0, 'neu': 0.206, 'pos': 0.794, 'compound': 0.7712}
        negText = "Everything is terrible and horrible at the same time"
        negExpected = {'neg': 0.485, 'neu': 0.515, 'pos': 0.0, 'compound': -0.765}
        posRes = self.scraper.process_sentiment(posText)
        self.assertEqual(posRes, posExpected)
        negRes = self.scraper.process_sentiment(negText)
        self.assertEqual(negRes, negExpected)

    def test_get_fakes(self):
        reviews = self.scraper.process_reviews(self.pages)
        fakes = self.scraper.get_fakes(reviews)
        self.assertEqual(len(fakes), 3)

if __name__ == '__main__':
    unittest.main()
