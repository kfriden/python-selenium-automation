from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
from pages.base_page import BasePage


class HelpPage(BasePage):
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER = (By.XPATH, "//h1[text()=' {HEADER_TEXT}']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "select[id*='ViewHelpTopics']")

    # DYNAMIC LOCATORS
    def _get_locator(self, text):
        return [self.HEADER[0], self.HEADER[1].replace('{HEADER_TEXT}', text)]


    def open_help_returns(self):
        self.open_url('https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges')

    def select_topic(self, option):
        topic_dropdown = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_dropdown)
        sleep(4)
        select.select_by_value(option)

    # def verify_returns_header(self):
    #     self.wait_until_visible(*self.HEADER_RETURNS)
    #
    # def verify_promotions_header(self):
    #     self.wait_until_visible(*self.HEADER_PROMOTIONS)

    def verify_header(self, header):
        locator = self._get_locator(header)
        self.wait_until_visible(*locator)
