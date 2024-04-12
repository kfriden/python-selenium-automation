from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Click sign in")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    sleep(6)

@when("Search for 'coffee'")
def search_product(context):
    context.driver.find_element(*SEARCH_INPUT).send_keys('coffee')
    context.driver.find_element(*SEARCH_BTN).click()
    sleep(6)

@when("Click cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(6)