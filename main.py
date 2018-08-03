from scrape import Scraper

if __name__ == "__main__":
    scraper = Scraper()
    if scraper.check_network() == False:
        print("network error")
    pages = scraper.get_pages()
    reviews = scraper.process_reviews(pages)
    scraper.print_fakes(reviews)
    

