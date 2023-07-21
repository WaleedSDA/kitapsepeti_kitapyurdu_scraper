from abc import ABC, abstractmethod
from typing import List, final

from flask import Response

from core.data_classes.scraped_data import ScrapedData
from core.errors import NoProductsFound, ErrorWhileScrapping
from core.requests_util import Request
from core.selenium_driver import ChromeDriver


class ScraperAbstract(ABC):

    def __init__(self):
        self.driver = None
        self.requests = Request()

    def initialize_webdriver(self):
        self.driver = ChromeDriver()

    @abstractmethod
    def go_to_the_main_page(self):
        pass

    @abstractmethod
    def go_to_specific_category(self):
        pass

    def get_raw_data(self):
        pass

    def get_final_data(self) -> List[ScrapedData]:
        pass

    @final
    def start_scraping(self):
        try:
            self.go_to_the_main_page()
            self.go_to_specific_category()
            self.get_raw_data()
            final_data = self.get_final_data()
            print(final_data)
            response = Response("OK")
            return response

        except(NoProductsFound, ErrorWhileScrapping, Exception) as e:
            response = Response(str(e))
            return response

        finally:
            pass
