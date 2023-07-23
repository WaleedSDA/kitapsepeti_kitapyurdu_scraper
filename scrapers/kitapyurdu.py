from lxml import html
from core.data_classes.scraped_data import ScrapedData
from core.scraper_abstract import ScraperAbstract


class KitapyurduScraper(ScraperAbstract):
    """
    Implements the abstract scraper for the website 'Kitapyurdu'.
    """

    @property
    def _scraper_name(self):
        """Name of the scraper"""
        return "Kitapyurdu"

    def _is_there_next_page(self) -> bool:
        """Determines if there is a next page on the website to scrape"""
        if self._page_tree.xpath('//a[@class="last"]'):
            return True
        return False

    def _category_mapper(self, category) -> str:
        """Maps input category to corresponding category on the website

        Args:
            category (str): Category name to map.

        Returns:
            str: Mapped category name on the website.
        """
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
    def _website_url(self):
        """Generates the website URL for a given category and page number

        Returns:
            str: URL of the website.
        """
        return f"https://www.kitapyurdu.com/index.php?route=product/best_sellers" \
               f"&page={self._page_number}&list_id={self._category_name}&filter_in_stock=1"

    def _scrape_raw_data(self):
        """Scrapes raw data from the website"""
        is_there_next_page = True
        while is_there_next_page:
            self.__go_to_products_page()
            books = self._page_tree.xpath('//*[@class="product-cr"]')
            self._raw_data.extend(books)
            self._page_number += 1
            is_there_next_page = self._is_there_next_page()

    def _get_final_data(self):
        """Returns the scraped data after finishing the scraping process

        Returns:
            List[ScrapedData]: List of the scraped data.
        """
        scraped_data = []
        for idx, book in enumerate(self._raw_data):
            book_name = book.xpath('.//*[@class="name ellipsis"]/a/span')[0].text
            publisher = book.xpath('.//*[@class="publisher"]/span/a/span')[0].text
            try:
                price = float(
                    book.xpath('.//div[@class="price-new "]/span/text()')[1].replace(" ", "").replace(",", "."))
            except IndexError:  # this means that the book was never on sale:)
                price = float(
                    book.xpath('.//span[@class="price-old "]/span[2]/text()')[0].replace(" ", "").replace(",", "."))

            currency = "TRY"
            try:
                authors = [book.xpath('.//*[@class="author"]/span/a/span')[0].text]
            except IndexError:
                authors = []  # means no author

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
        """Navigates to a specific category on the website"""
        pass

    def __go_to_products_page(self):
        """Navigates to the products page on the website"""
        response = self._requests.get(self._website_url)
        self._page_tree = html.fromstring(response.content)

    def _go_to_the_main_page(self):
        """Navigates to the main page of the website"""
        # we do not need to go to the main page.
        pass

    def _use_selenium_driver(self) -> bool:
        """Determines whether the selenium driver is needed for the website

        Returns:
            bool: True if the selenium driver is needed, False otherwise.
        """
        return False
