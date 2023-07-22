from seleniumwire import undetected_chromedriver as uc


def get_driver(use_headless_mode: bool = True):
    """
    the reason we used selenium-wire is scalability, it does every thing selenium does
    plus being able to access the requests coming out/in to the browser
    """
    options = uc.ChromeOptions()
    if use_headless_mode:
        options.headless = True
    driver = uc.Chrome(options=options)
    return driver
