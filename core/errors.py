class NoProductsFound(Exception):
    """
    Exception raised when no products are found during a web scraping operation.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    """
    pass


class ErrorWhileScrapping(Exception):
    """
    Exception raised when an error occurs during a web scraping operation.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    """
    pass


class NoSuchCategory(Exception):
    """
    Exception raised when a specified category does not exist during a web scraping operation.

    ...

    Attributes
    ----------
    None

    Methods
    -------
    None
    """
    pass
