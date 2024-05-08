from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep


class SignIn(BasePage):
    USERNAME_INPUT = (By.ID, 'username')
    PASSWORD_INPUT = (By.ID, 'password')
    LOGIN_BTN = (By.ID, 'login')
    LOGIN_ERROR_MSG = (By.ID, "password--ErrorMessage")

    def open_signin(self):
        self.driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')


    def verify_signin_opens(self):
        actual_text = self.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
        assert 'Sign into your Target account' in actual_text, f'Error: Text sign into your account not in {actual_text}'

    def input_username(self, username):
        self.click(*self.USERNAME_INPUT)
        self.input_text(username, *self.USERNAME_INPUT)
        sleep(4)

    def input_password(self, password):
        self.click(*self.PASSWORD_INPUT)
        self.input_text(password, *self.PASSWORD_INPUT)
        sleep(4)

    def click_login(self):
        self.click(*self.LOGIN_BTN)
        sleep(2)

    def verify_signin_error_message(self):
        self.verify_text('Please enter a valid password', *self.LOGIN_ERROR_MSG)
        sleep(2)
