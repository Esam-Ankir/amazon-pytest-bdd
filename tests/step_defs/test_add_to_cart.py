import time
from webbrowser import Chrome
from pytest_bdd import scenario, when, then, parsers
from tests.step_defs.locators import locators
from test_models.utilities import click_the_element, get_element, get_elements


@scenario('../features/add_to_cart.feature', 'Add And Remove From Cart')
def test_add_to_cart() -> None:
    pass


@when('Click any of the results to open the product page', target_fixture="open_product_page")
def open_product_page(browser: Chrome) -> str:
    third_result = get_element(browser, locators["third_result"])
    data_asin = third_result.get_dom_attribute('data-asin')
    click_the_element(get_element(third_result, locators["item_image"]))
    return data_asin


@when(parsers.parse('Click on "{locator}"'))
def remove_from_cart(browser: Chrome, locator: str) -> None:
    click_the_element(get_element(browser, locators[locator]))


@when('Click on the cart button')
def click_cart_button(browser: Chrome) -> None:
    if len(get_elements(browser, locators["sidesheet"])) > 0:
        click_the_element(get_element(browser, locators["sidesheet"]))
    else:
        click_the_element(get_element(browser, locators["nav_cart_icon"]))


@then('Check that the product added to the cart is the same product selected initially')
def check_same_product_added(browser: Chrome, open_product_page: str) -> None:
    active_form = get_element(browser, locators["active_cart_form"])
    active_form_data_asin = active_form.get_dom_attribute('data-asin')
    assert active_form_data_asin == open_product_page


@then('Check that the header contains "Your Amazon Cart is empty."')
def check_empty_header(browser: Chrome) -> None:
    time.sleep(5)
    header = get_element(browser, locators["header"]).text
    assert "Your Amazon Cart is empty." == header
