from seleniumwire import undetected_chromedriver as uc


def get_driver(use_headless_mode: bool = True):
    """
    The reason we used selenium-wire is scalability, it does everything selenium does
    plus being able to access the requests coming out/in to the browser.
    """
    options = uc.ChromeOptions()
    if use_headless_mode:
        options.add_argument('--headless')
    options.add_argument('--ignore-certificate-errors')
    driver = uc.Chrome(options=options)
    return driver
