import unittest
from datetime import datetime

from core.data_classes.scraped_data import ScrapedData


class TestScrapedData(unittest.TestCase):
    def test_valid_data(self):
        valid_data = ScrapedData('Book1', 10.0, 'USD', 'Seller1', 'Author1', 'Publisher1')
        self.assertEqual(valid_data.book_name, 'Book1')
        self.assertEqual(valid_data.book_current_price, 10.0)
        self.assertEqual(valid_data.currency, 'USD')
        self.assertEqual(valid_data.seller, 'Seller1')
        self.assertEqual(valid_data.author, 'Author1')
        self.assertEqual(valid_data.publisher, 'Publisher1')
        self.assertTrue(isinstance(valid_data.last_scrape_time, datetime))

    def test_invalid_book_name(self):
        with self.assertRaises(ValueError):
            ScrapedData('', 10.0, 'USD', 'Seller1', 'Author1', 'Publisher1')

    def test_invalid_price(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', -10.0, 'USD', 'Seller1', 'Author1', 'Publisher1')

    def test_invalid_currency(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', 10.0, 'usd', 'Seller1', 'Author1', 'Publisher1')

    def test_invalid_seller(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', 10.0, 'USD', '', 'Author1', 'Publisher1')

    def test_invalid_author(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', 10.0, 'USD', 'Seller1', '', 'Publisher1')

    def test_invalid_publisher(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', 10.0, 'USD', 'Seller1', 'Author1', '')

    def test_invalid_historical_prices(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', 10.0, 'USD', 'Seller1', 'Author1', 'Publisher1', historical_prices=[10.0])

    def test_invalid_scrape_time(self):
        with self.assertRaises(ValueError):
            ScrapedData('Book1', 10.0, 'USD', 'Seller1', 'Author1', 'Publisher1', last_scrape_time='2023-07-21')

    if __name__ == '__main__':
        unittest.main()
