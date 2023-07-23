from datetime import datetime

def validate_currency(currency):
    """
    Validates a currency code.

    Args:
        currency (str): The currency code to validate. Must be a three letter uppercase string.

    Raises:
        ValueError: If the currency code is not a string, is not three characters in length,
            or is not in uppercase letters.
    """
    if not isinstance(currency, str):
        raise ValueError(f'Currency must be a string, not {type(currency).__name__}')
    if len(currency) != 3 or not currency.isupper():
        raise ValueError('Currency must be three uppercase letters')


def validate_price(price):
    """
    Validates a price value.

    Args:
        price (int, float): The price to validate. Must be a positive number.

    Raises:
        ValueError: If the price is not a number or is not greater than 0.
    """
    if not isinstance(price, (int, float)):
        raise ValueError(f'Price must be a number, not {type(price).__name__}')
    if price <= 0:
        raise ValueError('Price must be greater than 0')


def validate_scrape_time(scrape_time):
    """
    Validates a scrape_time value.

    Args:
        scrape_time (datetime): The scrape_time to validate. Must be a datetime instance.

    Raises:
        ValueError: If the scrape_time is not a datetime instance.
    """
    if not isinstance(scrape_time, datetime):
        raise ValueError(f'Scrape_time must be a datetime instance, not {type(scrape_time).__name__}')


def validate_string(value, field_name):
    """
    Validates a string value.

    Args:
        value (str): The string to validate. Must be a non-empty string.
        field_name (str): The name of the field. Used in error messages.

    Raises:
        ValueError: If the value is not a string or is an empty string.
    """
    if not isinstance(value, str):
        raise ValueError(f'{field_name} must be a string, not {type(value).__name__}')
    if not value:
        raise ValueError(f'{field_name} cannot be empty')
