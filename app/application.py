from pages.base_page import BasePage
from pages.main_page import MainPage
from pages.header import Header
from pages.cart_page import CartPage
from pages.sign_in_page import SignIn
from pages.search_results_page import SearchResultsPage
from pages.target_app_page import TargetAppPage
from pages.privacy_policy_page import PrivacyPolicyPage
from pages.tc_page import TCPage
from pages.help_page import HelpPage
class Application:

    def __init__(self, driver):
        self.base_page = BasePage(driver)
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
        self.sign_in_page = SignIn(driver)
        self.target_app_page = TargetAppPage(driver)
        self.privacy_policy_page = PrivacyPolicyPage(driver)
        self.tc_page = TCPage(driver)
        self.help_page = HelpPage(driver)


