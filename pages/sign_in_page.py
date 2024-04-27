from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignIn(BasePage):

    def verify_signin_opens(self):
        actual_text = self.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
        assert 'Sign into your Target account' in actual_text, f'Error: Text sign into your account not in {actual_text}'