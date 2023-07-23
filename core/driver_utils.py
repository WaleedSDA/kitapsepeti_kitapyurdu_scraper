from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_element_by_xpath(driver, xpath) -> WebElement:
    """
    Waits until an element is present in the webpage and then returns it.

    This function uses the Selenium WebDriver to wait until an HTML element is present
    in a webpage, as identified by its XPath. If the element is found within 10 seconds,
    it is returned; otherwise, a TimeoutException is raised.

    Parameters
    ----------
    driver : WebDriver
        The WebDriver instance to use.
    xpath : str
        The XPath of the element to find.

    Returns
    -------
    WebElement
        The first matching element.
    """
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )
    return element


def get_all_elements_by_xpath(driver, xpath) -> List[WebElement]:
    """
    Waits until all elements are present in the webpage and then returns them.

    This function uses the Selenium WebDriver to wait until all HTML elements are present
    in a webpage, as identified by their XPath. If all elements are found within 10 seconds,
    they are returned as a list; otherwise, a TimeoutException is raised.

    Parameters
    ----------
    driver : WebDriver
        The WebDriver instance to use.
    xpath : str
        The XPath of the elements to find.

    Returns
    -------
    List[WebElement]
        A list of all matching elements.
    """
    elements = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_all_elements_located((By.XPATH, xpath))
    )
    return elements
