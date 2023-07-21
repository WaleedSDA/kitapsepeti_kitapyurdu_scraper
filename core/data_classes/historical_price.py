from dataclasses import dataclass
from datetime import datetime

from core.validators import validate_currency, validate_price, validate_scrape_time


@dataclass
class HistoricalPrice:
    price: float
    currency: str
    scrape_time: datetime

    def __post_init__(self):
        validate_currency(self.currency)
        validate_price(self.price)
        validate_scrape_time(self.scrape_time)
