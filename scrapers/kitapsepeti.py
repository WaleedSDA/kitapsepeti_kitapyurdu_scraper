from lxml import html

from core.data_classes.scraped_data import ScrapedData
from core.scraper_abstract import ScraperAbstract


class KitapsepetiScraper(ScraperAbstract):

    @property
    def _scraper_name(self):
        return "Kitapsepeti"

    __page_number = 1
    __page_tree = None

    def is_there_next_page(self) -> bool:
        if self.__page_tree.xpath('//a[@class="last"]'):
            return True
        return False

    def category_mapper(self, category) -> str:
        mapper = {  # adding this to the db and cashing it using redis will be a better choice
            "Kids": "22",
            "General": "1",
            "Literature": "16",
            "Exams": "28",
            "English": "25",
            "non-literary": "19",
        }
        return mapper[category]

    @property
    def website_url(self):
        return f"https://www.kitapyurdu.com/index.php?route=product/best_sellers" \
               f"&page={self.__page_number}&list_id={self.category_name}&filter_in_stock=1"

    def _scrape_raw_data(self):
        is_there_next_page = True
        while is_there_next_page:
            self.__go_to_products_page()
            books = self.__page_tree.xpath('//*[@class="product-cr"]')
            self._raw_data.extend(books)
            self.__page_number += 1
            is_there_next_page = self.is_there_next_page()

    def _get_final_data(self):
        scraped_data = []
        for idx, book in enumerate(self._raw_data):
            book_name = book.xpath('.//*[@class="name ellipsis"]/a/span')[0].text
            # kitapyurdu does not display more than one auther name
            publisher = book.xpath('.//*[@class="publisher"]/span/a/span')[0].text
            try:
                price = float(
                    book.xpath('.//div[@class="price-new "]/span/text()')[1].replace(" ", "").replace(",", "."))
            except IndexError:  # this means that the book was never on sale:)
                price = float(
                    book.xpath('.//span[@class="price-old "]/span[2]/text()')[0].replace(" ", "").replace(",", "."))

            currency = "TRY"

            # in the main page of search they show only one writer, if we need them all,
            # we need to make another request for all books, which will take 3 times the time
            try:
                authors = [book.xpath('.//*[@class="author"]/span/a/span')[0].text]
            except IndexError:
                authors = []  # means no auther
            scraped_data.append(ScrapedData(
                book_name=book_name,
                book_current_price=price,
                currency=currency,
                seller=self._scraper_name,
                authors=authors,
                publisher=publisher,
            ))
        return scraped_data

    def _go_to_specific_category(self):
        pass

    def __go_to_products_page(self):
        response = self.requests.get(self.website_url)
        self.__page_tree = html.fromstring(response.content)

    def _go_to_the_main_page(self):
        # we do not need to go to the main page.
        pass
