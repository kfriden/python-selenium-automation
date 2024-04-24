from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


SEARCH_INPUT = (By.ID, 'search')
SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")
CART_ICON = (By.CSS_SELECTOR, "a[data-test='@web/CartLink']")

@given('Open Target main page')
def open_target(context):
    context.app.main_page.open_main()

@when("Click sign in")
def sign_in(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/AccountLink']").click()
    # sleep(6)
    context.driver.implicitly_wait(4)

@when("Search for '{product}'")
def search_product(context, product):
    context.app.header.search_product(product)

@when("Click cart icon")
def click_cart_icon(context):
    context.driver.find_element(*CART_ICON).click()
    sleep(6)