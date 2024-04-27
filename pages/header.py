from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

    def search_product(self, product):
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart_icon(self):
        self.click(*self.CART_ICON)
