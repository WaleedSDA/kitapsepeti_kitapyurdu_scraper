from datetime import datetime
from dataclasses import dataclass, field
from typing import List

from core.data_classes.historical_price import HistoricalPrice
from core.validators import validate_string, validate_price, validate_currency, validate_scrape_time


@dataclass
class ScrapedData:
    """
    A class used to represent the Scraped Data of a book.

    ...

    Attributes
    ----------
    book_name : str
        The name of the book (required).
    book_current_price : float
        The current price of the book (required).
    currency : str
        The currency in which the book's price is stated (required).
    seller : str
        The seller of the book (required).
    authors : List[str]
        The list of authors of the book (required).
    publisher : str
        The publisher of the book (required).
    historical_prices : List[HistoricalPrice]
        The list of historical prices of the book (optional).
    last_scrape_time : datetime
        The date and time of the last scraping (optional, default is the current utc time).

    Methods
    -------
    validate_list_of_historical_prices():
        Validates the list of historical prices.
    __post_init__():
        Validates the attributes right after the instance has been initialized.
    """

    book_name: str
    book_current_price: float
    currency: str
    seller: str
    authors: List[str]
    publisher: str
    historical_prices: List[HistoricalPrice] = field(default_factory=list)
    last_scrape_time: datetime = field(default_factory=datetime.utcnow)

    def validate_list_of_historical_prices(self):
        """
        Validates that each element in `historical_prices` is an instance of `HistoricalPrice`.

        Raises
        ------
        ValueError
            If any element in `historical_prices` is not an instance of `HistoricalPrice`.
        """
        if self.historical_prices:
            if not all(isinstance(hp, HistoricalPrice) for hp in self.historical_prices):
                raise ValueError('All elements in historical_prices must be of type HistoricalPrice')

    def __post_init__(self):
        """
        The initializer function that runs right after the instance has been initialized.

        This function will validate the attributes using the functions provided in core.validators
        and the function `validate_list_of_historical_prices`.

        Raises
        ------
        ValueError
            If any of `book_name`, `book_current_price`, `currency`, `seller`, `publisher`,
            `historical_prices`, or `last_scrape_time` are not valid.
        """
        validate_string(self.book_name, 'Book name')
        validate_price(self.book_current_price)
        validate_currency(self.currency)
        validate_string(self.seller, 'Seller')
        validate_string(self.publisher, 'Publisher')
        self.validate_list_of_historical_prices()
        validate_scrape_time(self.last_scrape_time)
