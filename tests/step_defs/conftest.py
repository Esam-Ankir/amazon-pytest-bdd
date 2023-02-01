import pytest
from pytest_bdd import given, when, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from tests.step_defs.locators import Locator, obj

# Constants

AMAZON_URL = 'https://www.amazon.com/'


# Hooks

def pytest_bdd_step_error(request, feature, scenario, step, step_func, step_func_args, exception):
    print(f'Step failed: {step}')
    print(f'exception: {exception}')

# Fixtures


@pytest.fixture
def browser():
    b = webdriver.Chrome()
    b.maximize_window()
    b.implicitly_wait(10)
    yield b
    b.quit()

# Shared Given, Then Steps


@given('the Amazon home page is displayed', target_fixture='amazon_home')
def amazon_home(browser):
    browser.get(AMAZON_URL)


@when(parsers.parse('Type in a search term "{text}" in the search box and search'))
def search_phrase(browser, text):
    search_input = Locator(obj['search_input']).get_id(browser)
    search_input.send_keys(text + Keys.ENTER)
