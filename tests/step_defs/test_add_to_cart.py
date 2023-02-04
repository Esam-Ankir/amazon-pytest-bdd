import time
from pytest_bdd import scenario, when, then
from tests.step_defs.locators import Locator


@scenario('../features/add_to_cart.feature', 'Add And Remove From Cart')
def test_add_to_cart():
    pass


@when('Click any of the results to open the product page', target_fixture="open_product_page")
def open_product_page(browser):
    third_result = Locator(browser).third_result()
    data_asin = third_result.get_dom_attribute('data-asin')
    Locator(third_result).item_image().click()
    return data_asin


@when('Click on add to cart button on the side')
def click_add_to_cart_button(browser):
    Locator(browser).add_cart_button().click()


@when('Click on the cart button')
def click_cart_button(browser):
    if len(Locator(browser).all_sidesheets()) > 0:
        Locator(browser).sidesheet().click()
    else:
        Locator(browser).nav_cart_icon().click()


@then('Check that the product added to the cart is the same product selected initially')
def check_same_product_added(browser, open_product_page):
    active_form = Locator(browser).active_cart_form()
    active_form_data_asin = active_form.get_dom_attribute('data-asin')
    assert active_form_data_asin == open_product_page


@when('Click on Qty list and choose 0')
def remove_from_cart(browser):
    Locator(browser).cart_qty().click()
    Locator(browser).empty_cart().click()


@then('Check that the header contains "Your Amazon Cart is empty."')
def check_empty_header(browser):
    time.sleep(2)
    header = Locator(browser).header().text
    assert "Your Amazon Cart is empty." == header
