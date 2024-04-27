from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from time import sleep

class MainPage(BasePage):
    def open_main(self):
        self.driver.get('https://www.target.com/')

    def sign_in(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
        # sleep(6)
        self.driver.implicitly_wait(4)

    def sign_in_sidenav_bar(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
        sleep(3)