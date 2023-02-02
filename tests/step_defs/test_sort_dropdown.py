from pytest_bdd import scenarios, when, then, parsers
from tests.step_defs.locators import Locator, obj

scenarios('../features/dropdown.feature')


@when('Click on the sort dropdown')
def on_sort(browser):
    Locator(obj['sort_dropdown']).get_id(browser).click()


@then(parsers.parse('check that it has "{num:d}" list items'))
def check_items(browser, num):
    ul_element = Locator(obj['ul_element']).get_selector(browser)
    li_element = Locator(obj['li_tag']).get_tag(ul_element)
    assert len(li_element) == num


@when('Select “Newest Arrivals” in the list')
def select_newest_arrivals(browser):
    Locator(obj['newest_arrivals']).get_id(browser).click()
    Locator(obj['result_list']).get_selector(browser)


@when('Select “Featured” in the list')
def select_newest_arrivals(browser):
    Locator(obj['featured']).get_id(browser).click()
    Locator(obj['result_list']).get_selector(browser)


@then('check if there are search results appearing')
def check_search_results(browser):
    one_result = Locator(obj['one_result']).get_selector(browser)

    assert one_result.is_displayed()
