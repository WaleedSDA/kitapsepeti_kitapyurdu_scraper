import requests
from lxml import html

from scrapers.kitapsepeti import KitapsepetiScraper

# def scrape_quotes(url):
#     response = requests.get(url)
#     tree = html.fromstring(response.content)
#
#     books = tree.xpath('//*[@class="product-cr"]')
#
#     for book in books:
#         book_name = book.xpath('.//*[@class="name ellipsis"]/a/span')[0].text
#         author = book.xpath('.//small[@class="author"]/text()')[0]
#         tags = book.xpath('.//a[@class="tag"]/text()')
#         print(f'Quote: {quote}\nAuthor: {author}\nTags: {tags}\n---')


if __name__ == "__main__":
    x = KitapsepetiScraper("non-literary")
    x.start_scraping()
