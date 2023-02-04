from selenium.webdriver.common.by import By

class Locator():
    def __init__(self,browser):
        self.browser = browser

    NEWEST_ARRIVALS = (By.ID, 's-result-sort-select_4')
    SEARCH_INPUT = (By.ID, 'twotabsearchtextbox')
    SORT_DROPDOWN = (By.ID, 'a-autoid-0-announce')
    FEATURED = (By.ID, 's-result-sort-select_0')
    ADD_CART_BUTTON = (By.ID, 'add-to-cart-button')
    NAV_CART_ICON = (By.ID, 'nav-cart')
    NAV_CART_COUNT = (By.ID, 'nav-cart-count')
    CART_QTY = (By.ID, 'a-autoid-0')
    EMPTY_CART = (By.ID, 'quantity_0')
    UL_ELEMENT = (By.CSS_SELECTOR, 'ul[role="listbox"]')
    RESULT_LIST = (By.CSS_SELECTOR, "div.s-main-slot.s-result-list.s-search-results.sg-row")
    ONE_RESULT = (By.CSS_SELECTOR, 'div[data-index]:nth-child(6)')
    ACTIVE_CART_DIV = (By.CSS_SELECTOR, 'div[data-name="Active Cart"]')
    ACTIVE_CART_FORM = (By.CSS_SELECTOR, '#activeCartViewForm [data-name="Active Items"] :nth-child(3)')
    THIRD_RESULT = (By.CSS_SELECTOR, "[data-index='3']")
    HEADER = (By.CSS_SELECTOR, '#sc-active-cart > div > div > div > h1')
    SIDESHEET = (By.XPATH, '//*[@id="attach-sidesheet-view-cart-button"]/span/input')
    ITEM_IMAGE = (By.CLASS_NAME, 's-image' )
    LI_TAG=(By.TAG_NAME, 'li')

    def newest_arrivals(self):
        return self.browser.find_element(*self.NEWEST_ARRIVALS)
    def search_input(self):
        return self.browser.find_element(*self.SEARCH_INPUT)
    def sort_dropdown(self):
        return self.browser.find_element(*self.SORT_DROPDOWN)
    def featured(self):
        return self.browser.find_element(*self.FEATURED)
    def add_cart_button(self):
        return self.browser.find_element(*self.ADD_CART_BUTTON)
    def nav_cart_icon(self):
        return self.browser.find_element(*self.NAV_CART_ICON)
    def nav_cart_count(self):
        return self.browser.find_element(*self.NAV_CART_COUNT)
    def cart_qty(self):
        return self.browser.find_element(*self.CART_QTY)
    def empty_cart(self):
        return self.browser.find_element(*self.EMPTY_CART)
    def ul_element(self):
        return self.browser.find_element(*self.UL_ELEMENT)
    def result_list(self):
        return self.browser.find_element(*self.RESULT_LIST)
    def one_result(self):
        return self.browser.find_element(*self.ONE_RESULT)
    def active_cart_div(self):
        return self.browser.find_element(*self.ACTIVE_CART_DIV)
    def active_cart_form(self):
        return self.browser.find_element(*self.ACTIVE_CART_FORM)
    def third_result(self):
        return self.browser.find_element(*self.THIRD_RESULT)
    def header(self):
        return self.browser.find_element(*self.HEADER)
    def sidesheet(self):
        return self.browser.find_element(*self.SIDESHEET)
    def all_sidesheets(self):
        return self.browser.find_elements(*self.SIDESHEET)
    def item_image(self):
        return self.browser.find_element(*self.ITEM_IMAGE)
    def li_tag(self):
        return self.browser.find_elements(*self.LI_TAG)
    

