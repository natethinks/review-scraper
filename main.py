from scrape import Scraper
import pprint

if __name__ == "__main__":
    scraper = Scraper()
    if scraper.check_network() == False:
        print("FATAL: network error")
        return
    pages = scraper.get_pages()
    reviews = scraper.process_reviews(pages)
    fakes = scraper.get_fakes(reviews)
    # print only the first 3 fakes
    pprint.pprint(fakes[:3])
