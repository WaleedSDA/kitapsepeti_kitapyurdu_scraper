import unittest
from datetime import datetime, timedelta

from core.data_classes.historical_price import HistoricalPrice


class TestScrapedData(unittest.TestCase):
    def test_valid_data(self):
        valid_data = HistoricalPrice(10.0, 'USD', datetime.now())
        self.assertEqual(valid_data.currency, 'USD')
        self.assertEqual(valid_data.price, 10.0)
        self.assertTrue(isinstance(valid_data.scrape_time, datetime))

    def test_invalid_currency_type(self):
        with self.assertRaises(ValueError):
            HistoricalPrice(10.0, 123, datetime.now())

    def test_invalid_currency_length(self):
        with self.assertRaises(ValueError):
            HistoricalPrice(10.0, 'US', datetime.now())

    def test_invalid_currency_case(self):
        with self.assertRaises(ValueError):
            HistoricalPrice(10.0, 'usd', datetime.now())

    def test_invalid_price_type(self):
        with self.assertRaises(ValueError):
            HistoricalPrice('10.0', 'USD', datetime.now())

    def test_invalid_price_value(self):
        with self.assertRaises(ValueError):
            HistoricalPrice(0.0, 'USD', datetime.now())

    def test_invalid_scrape_time_type(self):
        with self.assertRaises(ValueError):
            HistoricalPrice(10.0, 'USD', '2023-07-21')


if __name__ == '__main__':
    unittest.main()
