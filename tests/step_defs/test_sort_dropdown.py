from pytest_bdd import scenarios, when, then, parsers
from tests.step_defs.locators import Locator

scenarios('../features/dropdown.feature')


@when('Click on the sort dropdown')
def on_sort(browser):
    Locator(browser).sort_dropdown().click()


@then(parsers.parse('check that it has "{num:d}" list items'))
def check_items(browser, num):
    ul_element = Locator(browser).ul_element()
    li_element = Locator(ul_element).li_tag()
    assert len(li_element) == num


@when('Select “Newest Arrivals” in the list')
def select_newest_arrivals(browser):
    Locator(browser).newest_arrivals().click()
    Locator(browser).result_list()


@when('Select “Featured” in the list')
def select_newest_arrivals(browser):
    Locator(browser).featured().click()
    Locator(browser).result_list()


@then('check if there are search results appearing')
def check_search_results(browser):
    one_result = Locator(browser).one_result()
    assert one_result.is_displayed()
