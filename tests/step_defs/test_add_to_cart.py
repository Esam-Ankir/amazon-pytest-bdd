from pytest_bdd import scenarios, when, then
from tests.step_defs.locators import Locator, obj
import time

scenarios('../features/add_to_cart.feature')


@when('Click any of the results to open the product page')
def open_product_page(browser):
    third_result = Locator(obj['third_result']).get_selector(browser)
    global third_result_data_asin
    third_result_data_asin = third_result.get_dom_attribute('data-asin')
    Locator(obj['item_image']).get_class(third_result).click()


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
def check_same_product_added(browser):
    active_form = Locator(
        obj['active_cart_form']).get_selector(browser)
    active_form_data_asin = active_form.get_dom_attribute('data-asin')
    assert active_form_data_asin == third_result_data_asin


@when('Click on Qty list and choose 0')
def remove_from_cart(browser):
    Locator(obj['cart_qty']).get_id(browser).click()
    Locator(obj['empty_cart']).get_id(browser).click()


@then('Check that the header contains "Your Amazon Cart is empty."')
def check_empty_header(browser):
    time.sleep(10)
    header = Locator(obj['header']).get_selector(browser).text
    assert "Your Amazon Cart is empty." == header
