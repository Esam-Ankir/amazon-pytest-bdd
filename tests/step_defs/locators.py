from selenium.webdriver.common.by import By

obj = {
    "newest_arrivals": "s-result-sort-select_4",
    "search_input": "twotabsearchtextbox",
    "sort_dropdown": "a-autoid-0-announce",
    "featured": "s-result-sort-select_0",
    "add_cart_button": 'add-to-cart-button',
    "nav_cart_icon": 'nav-cart',
    "nav_cart_count": 'nav-cart-count',
    "cart_qty": 'a-autoid-0',
    "empty_cart": 'quantity_0',
    "ul_element": 'ul[role="listbox"]',
    "result_list": "div.s-main-slot.s-result-list.s-search-results.sg-row",
    "one_result": 'div[data-index]:nth-child(6)',
    "active_cart_div": 'div[data-name="Active Cart"]',
    "active_cart_form": '#activeCartViewForm [data-name="Active Items"] :nth-child(3)',
    "third_result": "[data-index='3']",
    "header": "#sc-active-cart > div > div > div > h1",
    "sidesheet": '//*[@id="attach-sidesheet-view-cart-button"]/span/input',
    "item_image": 's-image'
}


class Locator():
    def __init__(self, name):
        self.name = name

    def get_id(self, browser):
        return browser.find_element(By.ID, self.name)

    def get_class(self, browser):
        return browser.find_element(By.CLASS_NAME, self.name)

    def get_selector(self, browser):
        return browser.find_element(By.CSS_SELECTOR, self.name)

    def get_tag(self, browser):
        return browser.find_element(By.TAG_NAME, self.name)

    def get_xpath(self, browser):
        return browser.find_element(By.XPATH, self.name)

    def get_all_xpath(self, browser):
        return browser.find_elements(By.XPATH, self.name)
