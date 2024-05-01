from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class TCPage(BasePage):

    def click_tc_link(self):
        self.driver.find_element(By.XPATH, "//a[contains(text(), 'Target terms and conditions')]").click()

    def verify_tc_opened(self):
        self.verify_partial_url('terms-conditions/')