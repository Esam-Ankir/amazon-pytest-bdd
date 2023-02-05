from webbrowser import Chrome
import pytest
from pytest_bdd import given, when, parsers
from selenium import webdriver
from decouple import config
from test_models.utilities import get_element, type_and_enter
from tests.step_defs.locators import locators


def pytest_bdd_step_error(step):
    print(f'Step failed: {step}')


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()


@given('the Amazon home page is displayed')
def amazon_home(browser: Chrome) -> None:
    browser.get(config('URL'))


@when(parsers.parse('Type in a search term "{text}" in the search box and search'))
def search_phrase(browser: Chrome, text) -> None:
    search_input = get_element(browser, locators["search_input"])
    type_and_enter(search_input, text)
