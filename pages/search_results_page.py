from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from pages.base_page import BasePage
from time import sleep

class SearchResultsPage(BasePage):
    SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")
    FAVORITES_BUTTON = (By.CSS_SELECTOR, "[data-test='FavoritesButton']")
    FAVORITES_TOOLTIP_TXT = (By.XPATH, "//*[text()='Click to sign in and save']")

    def verify_search_results(self, expected_item):
        actual_text = self.driver.find_element(*self.SEARCH_RESULT_HEADER).text
        assert expected_item in actual_text, f'Error: Text {expected_item} not in {actual_text}'

    def add_item_to_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']").click()
        sleep(8)

    def click_add_to_cart_side_menu(self):
        self.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/OverlayModal'] button[data-test='orderPickupButton']").click()
        sleep(8)

    def hover_favorites_icon(self):
        fav_button = self.find_element(*self.FAVORITES_BUTTON)

        actions = ActionChains(self.driver)
        actions.move_to_element(fav_button)
        actions.perform()
        sleep(5)


    def verify_tooltip_shown(self):
        self.verify_text('Click to sign in and save', *self.FAVORITES_TOOLTIP_TXT)



