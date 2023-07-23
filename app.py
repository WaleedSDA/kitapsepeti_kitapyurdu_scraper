from scrapers.kitapyurdu import KitapyurduScraper
from multiprocessing import Process


def scrape(category, scraper):
    s = scraper(category)
    s.start_scraping()


kitapyurdu_cat = ["Kids", "General", "Literature", "Exams", "English", "non-literary"]
for cat in kitapyurdu_cat:
    p = Process(target=scrape, args=(cat, KitapyurduScraper))
    p.start()

kitapyurdu_cat = ["Kids", "General", "Literature", "Exams", "Turkish_Literature", "sci-fi", "Anime"]
for cat in kitapyurdu_cat:
    p = Process(target=scrape, args=(cat, KitapyurduScraper))
    p.start()
