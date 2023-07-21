from datetime import datetime


def validate_currency(currency):
    if not isinstance(currency, str):
        raise ValueError(f'Currency must be a string, not {type(currency).__name__}')
    if len(currency) != 3 or not currency.isupper():
        raise ValueError('Currency must be three uppercase letters')


def validate_price(price):
    if not isinstance(price, (int, float)):
        raise ValueError(f'Price must be a number, not {type(price).__name__}')
    if price <= 0:
        raise ValueError('Price must be greater than 0')


def validate_scrape_time(scrape_time):
    if not isinstance(scrape_time, datetime):
        raise ValueError(f'Scrape_time must be a datetime instance, not {type(scrape_time).__name__}')
