from selenium.webdriver.common.by import By
from typing import Tuple, Dict

locators: Dict[str, Tuple[str, str]] = {
    "item_image": (By.CLASS_NAME, 's-image'),
    "li_tag": (By.TAG_NAME, 'li'),
    "cart_qty": (By.ID, 'a-autoid-0'),
    "empty_cart": (By.ID, 'quantity_0'),
    "nav_cart_icon": (By.ID, 'nav-cart'),
    "featured": (By.ID, "s-result-sort-select_0"),
    "search_input": (By.ID, "twotabsearchtextbox"),
    "sort_dropdown": (By.ID, "a-autoid-0-announce"),
    "add_cart_button": (By.ID, 'add-to-cart-button'),
    "newest_arrivals": (By.ID, "s-result-sort-select_4"),
    "ul_element": (By.CSS_SELECTOR, 'ul[role="listbox"]'),
    "third_result": (By.CSS_SELECTOR, "[data-index='3']"),
    "one_result": (By.CSS_SELECTOR, 'div[data-index]:nth-child(6)'),
    "header": (By.CSS_SELECTOR, "#sc-active-cart > div > div > div > h1"),
    "sidesheet": (By.XPATH, '//*[@id="attach-sidesheet-view-cart-button"]/span/input'),
    "result_list": (By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row"),
    "active_cart_form": (By.CSS_SELECTOR, '#activeCartViewForm [data-name="Active Items"] :nth-child(3)')
}
