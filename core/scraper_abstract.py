from abc import ABC, abstractmethod
from typing import List, final
from webbrowser import Chrome

from core.data_classes.scraped_data import ScrapedData
from core.db.scraped_data_col import ScrapedDataCol
from core.errors import NoProductsFound, ErrorWhileScrapping, NoSuchCategory
from core.requests_util import Request
from core.selenium_driver import get_driver


class ScraperAbstract(ABC):
    """
    The abstract base class that defines the basic structure and methods for all scraper classes.

    Attributes:
        _requests: A Request object for HTTP communication.
        _raw_data: A list to hold the raw data extracted from the website.
        __col: A ScrapedDataCol object to interact with the database.
        _category_name: The name of the category being scraped.

    Note:
        Any new scraper class should inherit from this base class and implement all abstract methods.
    """

    def __init__(self, category: str):
        """
        Initialize ScraperAbstract with a specific category.

        Args:
            category (str): The category name to scrape data from.

        Raises:
            NoSuchCategory: Exception if the given category is not found.
        """
        self._requests = Request()
        self._raw_data = []
        self.__col = ScrapedDataCol()
        self._page_number = 1
        self._page_tree = None

        try:
            self._category_name = self._category_mapper(category)
        except KeyError:
            raise NoSuchCategory

    @abstractmethod
    def _go_to_the_main_page(self):
        """
        An abstract method to navigate to the main page of the website.
        To be implemented by subclasses.
        """
        pass

    @abstractmethod
    def _go_to_specific_category(self):
        """
        An abstract method to navigate to a specific category on the website.
        To be implemented by subclasses.
        """
        pass

    @property
    @abstractmethod
    def _scraper_name(self):
        """
        An abstract method to return the name of the scraper.
        To be implemented by subclasses.
        """
        pass

    @abstractmethod
    def _scrape_raw_data(self) -> list:
        """
        An abstract method to scrape the raw data from the website.
        To be implemented by subclasses.

        Returns:
            list: Raw data scraped from the website.
        """
        pass

    @abstractmethod
    def _is_there_next_page(self) -> bool:
        """
        An abstract method to check if there is a next page in the pagination.
        To be implemented by subclasses.

        Returns:
            bool: True if there is a next page, False otherwise.
        """
        pass

    @abstractmethod
    def _use_selenium_driver(self) -> bool:
        """
        An abstract method to determine if the Selenium WebDriver is used in the scraper.
        To be implemented by subclasses.

        Returns:
            bool: True if the scraper uses Selenium WebDriver, False otherwise.
        """
        pass

    @abstractmethod
    def _get_final_data(self) -> List[ScrapedData]:
        """
        An abstract method to parse the raw data and return it in the final format.
        To be implemented by subclasses.

        Returns:
            List[ScrapedData]: A list of ScrapedData objects.
        """
        pass

    @property
    @abstractmethod
    def _website_url(self):
        """
        An abstract method to return the URL of the website to be scraped.
        To be implemented by subclasses.
        """
        pass

    @abstractmethod
    def _category_mapper(self, category) -> str:
        """
        An abstract method to map the input category to the corresponding category in the website.
        To be implemented by subclasses.

        Args:
            category (str): The input category.

        Returns:
            str: The corresponding category in the website.
        """
        pass

    @final
    def start_scraping(self):
        """
        Start the scraping process.
        It performs the scraping process with error handling and database interaction.

        Returns:
        """
        try:
            if self._use_selenium_driver():
                self._driver: Chrome = get_driver()
            self._go_to_the_main_page()
            self._go_to_specific_category()
            self._scrape_raw_data()
            final_data = self._get_final_data()
            self.__col.add_scraped_data_to_db(final_data)
            print(f"{self._scraper_name}/{self._category_name}: Done")
        except(NoProductsFound, ErrorWhileScrapping) as e:
            print(f"{self._scraper_name}/{self._category_name}: {e}")

        finally:
            if self._use_selenium_driver():
                self._driver.quit()
