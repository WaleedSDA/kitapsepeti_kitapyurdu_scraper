from abc import ABC, abstractmethod
from typing import List, final

from flask import Response
from seleniumwire.undetected_chromedriver import Chrome

from core.data_classes.scraped_data import ScrapedData
from core.db.scraped_data_col import ScrapedDataCol
from core.errors import NoProductsFound, ErrorWhileScrapping, NoSuchCategory
from core.requests_util import Request
from core.selenium_driver import get_driver


class ScraperAbstract(ABC):

    def __init__(self, category):
        self._requests = Request()
        self._raw_data = []
        self.__col = ScrapedDataCol()
        """
        doing the exception here will make the human error less likely,
        because devs will forget to handle this exception
        """
        try:
            self._category_name = self._category_mapper(category)
        except KeyError:
            raise NoSuchCategory

    @abstractmethod
    def _go_to_the_main_page(self):
        pass

    @abstractmethod
    def _go_to_specific_category(self):
        pass

    @property
    @abstractmethod
    def _scraper_name(self):
        pass

    @abstractmethod
    def _scrape_raw_data(self) -> list:
        pass

    @abstractmethod
    def _is_there_next_page(self) -> bool:
        pass

    @abstractmethod
    def _use_selenium_driver(self) -> bool:
        pass

    @abstractmethod
    def _get_final_data(self) -> List[ScrapedData]:
        pass

    @property
    @abstractmethod
    def _website_url(self):
        pass

    @abstractmethod
    def _category_mapper(self, category) -> str:
        pass

    @final
    def start_scraping(self):
        try:
            if self._use_selenium_driver():
                # the reason it is initialized here is we do not want chrome to open immediately in the constructor
                self._driver: Chrome = get_driver()
            self._go_to_the_main_page()
            self._go_to_specific_category()
            self._scrape_raw_data()
            final_data = self._get_final_data()
            self.__col.add_scraped_data_to_db(final_data)
            response = Response("OK")
            return response

        except(NoProductsFound, ErrorWhileScrapping, Exception) as e:
            response = Response(str(e))
            return response

        finally:
            if self._use_selenium_driver():
                self._driver.quit()
