from dataclasses import dataclass
from datetime import datetime


@dataclass
class ScrapedData:
    price: float
    currency: str
    scrape_time: datetime
