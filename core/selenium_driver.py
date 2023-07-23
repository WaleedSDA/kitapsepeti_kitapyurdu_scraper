from seleniumwire import undetected_chromedriver as uc


def get_driver(use_headless_mode: bool = True):
    """
    Returns an instance of a Selenium WebDriver with optional settings.

    The function uses Selenium Wire with undetected chromedriver.
    This allows the WebDriver to work with sites that detect and block standard automated browsers.

    Args:
        use_headless_mode (bool): Determines whether the browser runs in headless mode.
            If True, the browser will not display a GUI. Defaults to True.

    Returns:
        driver: A Selenium WebDriver instance.
    """
    # Create a new instance of ChromeOptions, which will allow us to customize the browser session.
    options = uc.ChromeOptions()

    # If use_headless_mode is True, add the 'headless' argument.
    # This runs the browser in headless mode (without a GUI).
    if use_headless_mode:
        options.add_argument('--headless')

    # Add the 'ignore-certificate-errors' argument.
    # This ignores any SSL certificate errors that might occur during the browser session.
    options.add_argument('--ignore-certificate-errors')

    # Create a new instance of the Selenium WebDriver using the specified options.
    driver = uc.Chrome(options=options)


    return driver
