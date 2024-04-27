from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from time import sleep

class SearchResultsPage(BasePage):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    def verify_search_results(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error: Text {expected_item} not in {actual_text}'

    def add_item_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']").click()
        sleep(8)

    def click_add_to_cart_side_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/OverlayModal'] button[data-test='orderPickupButton']").click()
        sleep(8)


