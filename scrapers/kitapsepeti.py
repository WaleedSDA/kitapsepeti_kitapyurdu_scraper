from core.data_classes.scraped_data import ScrapedData
from core.driver_utils import get_element_by_xpath, get_all_elements_by_xpath
from core.scraper_abstract import ScraperAbstract


class KitapsepetiScraper(ScraperAbstract):
    """
    Implements the abstract scraper for the website 'Kitapsepeti'.
    """

    @property
    def _scraper_name(self):
        """Name of the scraper"""
        return "Kitapsepeti"

    __scraped_data = []

    def _is_there_next_page(self) -> bool:
        """Determines if there is a next page on the website to scrape"""
        pass

    def __get_number_of_available_pages(self):
        """Gets the number of available pages on the website"""
        element = get_element_by_xpath(self._driver, '(//div[@id="pager-wrapper"]/div/div/a)[last()-1]')
        return int(element.text)

    def _category_mapper(self, category) -> str:
        """Maps input category to corresponding category on the website

        Args:
            category (str): Category name to map.

        Returns:
            str: Mapped category name on the website.
        """
        mapper = {  # adding this to the db and cashing it using redis will be a better choice
            "Kids": "cocuk-kitaplari",
            "General": "cok-satan-kitaplar",
            "Literature": "roman",
            "Exams": "sinavlara-hazirlik-kitaplari",
            "Turkish_Literature": "turk-edebiyati",
            "sci-fi": "bilimkurgu",
            "Anime": "cizgi-roman"
        }
        return mapper[category]

    @property
    def _website_url(self):
        """Generates the website URL for a given category and page number

        Returns:
            str: URL of the website.
        """
        return f"https://www.kitapsepeti.com/{self._category_name}?pg={self._page_number}"

    @property
    def __book_frame_xpath(self):
        if self._category_name in ["cok-satan-kitaplar", "bilimkurgu"]:
            return '//div[contains(@class, "productDetails")]'
        return '(//div[contains(@class, "catalogWrapper")])[2]//div[contains(@class, "productDetails")]'

    def _scrape_raw_data(self):
        """Scrapes raw data from the website"""
        number_of_pages = self.__get_number_of_available_pages()
        number_of_pages = 10
        for page_number in range(2, number_of_pages + 1):

            books = get_all_elements_by_xpath(self._driver, self.__book_frame_xpath)
            for book in books:
                self.__scraped_data.append(self.__get_transformed_book(book))

            self._page_number = page_number
            self._go_to_specific_category()

    def __get_transformed_book(self, book):
        """Transforms the raw book data into ScrapedData format

        Args:
            book: Raw book data.

        Returns:
            ScrapedData: Transformed book data.
        """
        book_name, publisher, auther = get_all_elements_by_xpath(book, './/div[@class="row"]/a')
        price = get_element_by_xpath(book, './/div[contains(@class, "currentPrice")]').text
        price = float(price.replace(" ", "").replace("TL", "").replace(",", "."))
        publisher = publisher.text
        book_name = book_name.text
        auther = auther.text
        return ScrapedData(
            book_name=book_name,
            book_current_price=price,
            currency="TRY",
            seller=self._scraper_name,
            authors=[auther],
            publisher=publisher
        )

    def _get_final_data(self):
        """Returns the scraped data after finishing the scraping process

        Returns:
            List[ScrapedData]: List of the scraped data.
        """
        return self.__scraped_data

    def _go_to_specific_category(self):
        """Navigates to the URL of a specific category on the website"""
        # blocking extra networks will differently help speeding thing up
        self._driver.get(self._website_url)

    def _go_to_the_main_page(self):
        """Navigates to the main page of the website"""
        # we do not need to go to the main page.
        pass

    def _use_selenium_driver(self) -> bool:
        """Determines whether the selenium driver is needed for the website

        Returns:
            bool: True if the selenium driver is needed, False otherwise.
        """
        return True
