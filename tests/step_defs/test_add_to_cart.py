import pytest
import time
from pytest_bdd import scenario, when, then
from tests.step_defs.locators import Locator, obj


@scenario('../features/add_to_cart.feature', 'Add And Remove From Cart')
def test_add_to_cart():
    pass


@when('Click any of the results to open the product page', target_fixture="open_product_page")
def open_product_page(browser):
    third_result = Locator(obj['third_result']).get_selector(browser)
    data_asin = third_result.get_dom_attribute('data-asin')
    Locator(obj['item_image']).get_class(third_result).click()
    return data_asin


@when('Click on add to cart button on the side')
def click_add_to_cart_button(browser):
    Locator(obj['add_cart_button']).get_id(browser).click()


@when('Click on the cart button')
def click_cart_button(browser):
    if len(Locator(obj['sidesheet']).get_all_xpath(browser)) > 0:
        Locator(obj['sidesheet']).get_xpath(browser).click()
    else:
        Locator(obj['nav_cart_icon']).get_id(browser).click()


@then('Check that the product added to the cart is the same product selected initially')
def check_same_product_added(browser, open_product_page):
    active_form = Locator(
        obj['active_cart_form']).get_selector(browser)
    active_form_data_asin = active_form.get_dom_attribute('data-asin')
    assert active_form_data_asin == open_product_page


@when('Click on Qty list and choose 0')
def remove_from_cart(browser):
    Locator(obj['cart_qty']).get_id(browser).click()
    Locator(obj['empty_cart']).get_id(browser).click()


@then('Check that the header contains "Your Amazon Cart is empty."')
def check_empty_header(browser):
    time.sleep(10)
    header = Locator(obj['header']).get_selector(browser).text
    assert "Your Amazon Cart is empty." == header
