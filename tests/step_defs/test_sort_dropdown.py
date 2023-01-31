from pytest_bdd import scenarios, given, when, then, parsers
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.step_defs import locators

AMAZON_URL = 'https://www.amazon.com/'

scenarios('../features/dropdown.feature')


@when('Click on the sort dropdown')
def on_sort(browser):
    sort_dropdown = browser.find_element(By.ID, locators.sort_dropdown_id)
    sort_dropdown.click()


@then(parsers.parse('check that it has "{num:d}" list items'))
def check_items(browser, num):
    ul_element = browser.find_element(
        By.CSS_SELECTOR, locators.ul_element_selector).find_elements(
        By.TAG_NAME, 'li')
    assert len(ul_element) == num


@when('Select “Newest Arrivals” in the list')
def select_newest_arrivals(browser):
    result_sort = browser.find_element(
        By.ID, locators.newest_arrivals_id).click()
    result_list = browser.find_element(
        By.CSS_SELECTOR, locators.result_list_selector)


@when('Select “Featured” in the list')
def select_newest_arrivals(browser):
    result_sort = browser.find_element(By.ID, locators.featured_id).click()
    result_list = browser.find_element(
        By.CSS_SELECTOR, locators.result_list_selector)


@then('check if there are search results appearing')
def check_search_results(browser):
    one_result = (browser.find_element(
        By.CSS_SELECTOR, locators.one_result_selector))
    assert one_result.is_displayed()
