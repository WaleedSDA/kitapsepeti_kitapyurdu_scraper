from datetime import datetime
from dataclasses import dataclass
from typing import List

from core.db.data_classes.historical_price import ScrapedData


@dataclass
class ScrapedData:
    book_name: str  # required
    book_current_price: float  # required
    currency: str  # required
    seller: str  # required
    auther: str  # required
    publisher: str  # required
    historical_prices: List[ScrapedData] = list
    last_scrape_time: datetime = datetime.utcnow()
