import pytest
from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from tests.step_defs import locators
from selenium.webdriver.support import expected_conditions as EC
import time

AMAZON_URL = 'https://www.amazon.com/'

scenarios('../features/add_to_cart.feature')

pytest.fixture()


@when('Click any of the results to open the product page')
def open_product_page(browser):
    third_result = browser.find_element(
        By.CSS_SELECTOR, locators.third_result_selector)
    third_result_data_asin = third_result.get_dom_attribute('data-asin')
    global before_data_asin
    before_data_asin = third_result_data_asin
    third_result.find_element(
        By.CLASS_NAME, locators.item_image_class).click()


@when('Click on add to cart button on the side')
def click_add_to_cart_button(browser):
    browser.find_element(
        By.ID, locators.add_cart_button_id).click()


@when('Click on the cart button')
def click_cart_button(browser):
    if len(browser.find_elements(By.XPATH, locators.sidesheet_xpath)) > 0:
        browser.find_element(By.XPATH, locators.sidesheet_xpath).click()
    else:
        browser.find_element(By.ID, locators.nav_cart_icon_id).click()


@then('Check that the product added to the cart is the same product selected initially')
def check_same_product_added(browser):
    active_form = browser.find_element(
        By.CSS_SELECTOR, locators.active_cart_form_selector)
    active_form_data_asin = active_form.get_dom_attribute('data-asin')
    assert active_form_data_asin == before_data_asin


@when('Click on Qty list and choose 0')
def remove_from_cart(browser):
    browser.find_element(By.ID, locators.cart_qty_id).click()
    browser.find_element(By.ID, locators.empty_cart_id).click()


@then('Check that the header contains "Your Amazon Cart is empty."')
def check_empty_header(browser):
    time.sleep(10)
    header = browser.find_element(
        By.CSS_SELECTOR, locators.header_selector).text
    assert "Your Amazon Cart is empty." == header
