from scrapers.kitapsepeti import KitapsepetiScraper

if __name__ == "__main__":
    x = KitapsepetiScraper("non-literary")
    x.start_scraping()
