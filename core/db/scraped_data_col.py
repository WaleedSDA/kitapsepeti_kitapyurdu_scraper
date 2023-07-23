from typing import List
from dataclasses_serialization.bson import BSONSerializer

from core.data_classes.historical_price import HistoricalPrice
from core.data_classes.scraped_data import ScrapedData
from core.db.db_connection import DbWrapper


class ScrapedDataCol(DbWrapper):
    """
    A subclass of DbWrapper to interact with the 'scraped_data' MongoDB collection.

    ...

    Methods
    -------
    add_scraped_data_to_db(scraped_data):
        Adds a list of ScrapedData objects to the collection. If a record with the same
        book_name, seller, and authors already exists, it updates the historical prices of the record.
    """

    def __init__(self):
        """
        Initializes the ScrapedDataCol with the 'scraped_data' collection.
        """
        super().__init__("scraped_data")

    def add_scraped_data_to_db(self, scraped_data: List[ScrapedData]):
        """
        Adds a list of ScrapedData objects to the collection. If a record with the same
        book_name, seller, and authors already exists, it updates the historical prices of the record.

        Parameters
        ----------
        scraped_data : List[ScrapedData]
            The list of ScrapedData objects to be added to the collection.
        """
        for scraped_obj in scraped_data:
            searching_filter = {
                "book_name": scraped_obj.book_name,
                "seller": scraped_obj.seller,
                "authors": scraped_obj.authors
            }
            existing_rec = self.find_one(searching_filter)
            if not existing_rec:
                self.insert_one(scraped_obj)
            else:
                del existing_rec["_id"]
                existing_rec: ScrapedData = BSONSerializer.deserialize(ScrapedData, existing_rec)
                historical_prices: List[HistoricalPrice] = existing_rec.historical_prices
                historical_prices.append(HistoricalPrice(
                    price=existing_rec.book_current_price,
                    currency=existing_rec.currency,
                    scrape_time=existing_rec.last_scrape_time
                ))
                scraped_obj.historical_prices = historical_prices
                self.replace_one(searching_filter, scraped_obj)
