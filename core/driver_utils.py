from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def get_element_by_xpath(driver, xpath) -> WebElement:
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, xpath))
    )
    return element


def get_all_elements_by_xpath(driver, xpath) -> List[WebElement]:
    element = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_all_elements_located((By.XPATH, xpath))
    )
    return element
