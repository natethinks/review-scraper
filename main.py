from scrape import Scraper
import pprint

if __name__ == "__main__":
    scraper = Scraper()
    if scraper.check_network() == False:
        print("network error")
    pages = scraper.get_pages()
    reviews = scraper.process_reviews(pages)
    fakes = scraper.get_fakes(reviews)
    pprint.pprint(fakes[:3])
