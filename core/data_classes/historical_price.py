from dataclasses import dataclass
from datetime import datetime

from core.validators import validate_currency, validate_price, validate_scrape_time


@dataclass
class HistoricalPrice:
    """
    A class used to represent the Historical Price of an item.

    ...

    Attributes
    ----------
    price : float
        The price of the item at the time it was scraped
    currency : str
        The currency in which the price of the item is stated
    scrape_time : datetime
        The exact date and time the price was scraped

    Methods
    -------
    __post_init__():
        Validates the attributes right after the instance has been initialized.
    """

    price: float
    currency: str
    scrape_time: datetime

    def __post_init__(self):
        """
        The initializer function that runs right after the instance has been initialized.

        This function will validate the attributes using the functions provided in core.validators.

        Raises
        ------
        ValueError
            If `price`, `currency`, or `scrape_time` are not valid.
        """
        validate_currency(self.currency)
        validate_price(self.price)
        validate_scrape_time(self.scrape_time)
