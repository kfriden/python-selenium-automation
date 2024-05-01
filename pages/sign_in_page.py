from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignIn(BasePage):

    def open_signin(self):
        self.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')


    def verify_signin_opens(self):
        actual_text = self.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
        assert 'Sign into your Target account' in actual_text, f'Error: Text sign into your account not in {actual_text}'