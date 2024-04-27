from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class Header(BasePage):
    SEARCH_INPUT = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
    CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

    def search_product(self, product):
        self.click(*self.SEARCH_INPUT)
        self.input_text(product, *self.SEARCH_INPUT)
        self.click(*self.SEARCH_BTN)
        sleep(6)

    def click_cart_icon(self):
        self.wait_until_clickable(*self.CART_ICON)
        self.save_screenshot('clicked_cart')
