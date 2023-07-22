from datetime import datetime
from dataclasses import dataclass, field
from typing import List

from core.data_classes.historical_price import HistoricalPrice
from core.validators import validate_string, validate_price, validate_currency, validate_scrape_time


@dataclass
class ScrapedData:
    book_name: str  # required
    book_current_price: float  # required
    currency: str  # required
    seller: str  # required
    authors: List[str]  # required
    publisher: str  # required
    historical_prices: List[HistoricalPrice] = field(default_factory=list)
    last_scrape_time: datetime = field(default_factory=datetime.utcnow)

    def validate_list_of_historical_prices(self):
        if self.historical_prices:
            if not all(isinstance(hp, HistoricalPrice) for hp in self.historical_prices):
                raise ValueError('All elements in historical_prices must be of type HistoricalPrice')

    def __post_init__(self):
        validate_string(self.book_name, 'Book name')
        validate_price(self.book_current_price)
        validate_currency(self.currency)
        validate_string(self.seller, 'Seller')
        validate_string(self.publisher, 'Publisher')
        self.validate_list_of_historical_prices()
        validate_scrape_time(self.last_scrape_time)
