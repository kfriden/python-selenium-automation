from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')

@when("Click cart icon")
def search_product(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='@web/CartLink']").click()
    sleep(6)

@then('Verify cart is empty message shows')
def verify_cart_empty(context):
    actual_text = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert 'cart is empty' in actual_text, f'Error: Text cart is empty not in {actual_text}'