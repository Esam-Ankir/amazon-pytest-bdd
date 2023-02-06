from webbrowser import Chrome
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.keys import Keys
from typing import Tuple


def get_element(browser: Chrome, locator: Tuple[str, str]) -> WebElement:
    (type, selector) = locator
    element = browser.find_element(type, selector)
    return element


def get_elements(browser: Chrome, locator: Tuple[str, str]) -> list[WebElement]:
    (type, selector) = locator
    elements = browser.find_elements(type, selector)
    return elements


def click_the_element(element: WebElement) -> None:
    element.click()


def type_and_enter(element: WebElement, text: str) -> None:
    element.send_keys(text)
    element.send_keys(Keys.ENTER)
