from core.data_classes.scraped_data import ScrapedData
from core.driver_utils import get_element_by_xpath, get_all_elements_by_xpath
from core.scraper_abstract import ScraperAbstract


class KitapsepetiScraper(ScraperAbstract):

    @property
    def _scraper_name(self):
        return "Kitapsepeti"

    __page_number = 1
    __page_tree = None
    __scraped_data = []

    def _is_there_next_page(self) -> bool:
        pass

    def __get_number_of_available_pages(self):
        element = get_element_by_xpath(self._driver, '(//div[@id="pager-wrapper"]/div/div/a)[last()-1]')
        return int(element.text)

    def _category_mapper(self, category) -> str:
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
        return f"https://www.kitapsepeti.com/{self._category_name}?pg={self.__page_number}"

    def _scrape_raw_data(self):
        number_of_pages = self.__get_number_of_available_pages()
        number_of_pages = 5
        for page_number in range(2, number_of_pages + 1):
            books = get_all_elements_by_xpath(self._driver,
                                              '(//div[contains(@class, "catalogWrapper")])[2]//div[contains(@class, "productDetails")]')
            for book in books:
                self.__scraped_data.append(self.__get_transformed_book(book))

            self.__page_number = page_number
            self._go_to_specific_category()

    def __get_transformed_book(self, book):
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
        return self.__scraped_data

    def _go_to_specific_category(self):
        # blocking extra networks will differently help speeding thing up
        self._driver.get(self._website_url)

    def _go_to_the_main_page(self):
        # we do not need to go to the main page.
        pass

    def _use_selenium_driver(self) -> bool:
        return True
