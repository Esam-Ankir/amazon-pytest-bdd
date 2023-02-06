from webbrowser import Chrome
from pytest_bdd import scenario, when, then, parsers
from test_models.utilities import click_the_element, get_element, get_elements
from tests.step_defs.locators import locators


@scenario('../features/dropdown.feature', 'Sort Dropdown')
def test_sort_dropdown() -> None:
    pass


@when(parsers.parse('Click on "{locator}"'))
def select_newest_arrivals(browser: Chrome, locator: str) -> None:
    click_the_element(get_element(browser, locators[locator]))


@then(parsers.parse('check that it has "{num:d}" list items'))
def check_items(browser: Chrome, num: int) -> None:
    ul_element = get_element(browser, locators["ul_element"])
    li_element = get_elements(ul_element, locators["li_tag"])
    assert len(li_element) == num


@scenario('../features/dropdown.feature', 'Newest Arrivals')
def test_newest_arrivals() -> None:
    pass


@scenario('../features/dropdown.feature', 'Featured')
def test_featured() -> None:
    pass


@then('check if there are search results appearing')
def check_search_results(browser: Chrome) -> None:
    get_element(browser, locators["result_list"])
    one_result = get_element(browser, locators["one_result"])
    assert one_result.is_displayed()
