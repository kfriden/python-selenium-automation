from selenium.webdriver.common.by import By
from time import sleep
from pages.base_page import BasePage


class CartPage(BasePage):
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "h1[class*='StyledHeading']")

    def open_cart_page(self):
        self.driver.get('https://www.target.com/cart')

    def verify_cart_empty_message(self):
        self.verify_text('Your cart is empty', *self.CART_EMPTY_MSG)

    def verify_item_in_cart(self):
        actual_text = self.driver.find_element(By.XPATH, "//span[contains(text(), '1 item')]").text
        assert '1 item' in actual_text, f'Error: There are no {actual_text} in your cart'
        sleep(5)