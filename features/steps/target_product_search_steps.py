from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@then("Add any '{product}' item to cart")
def add_first_product(context, product):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='chooseOptionsButton']").click()
    # sleep(4)
    context.driver.implicitly_wait(4)

@then("Click Add to Cart on side menu")
def add_cart_side_menu(context):
    context.driver.find_element(By.CSS_SELECTOR, "button[data-test='orderPickupButton']").click()
    # UNABLE TO USE IMPLICIT OR EXPLICIT WAIT IT FAILS EVERY TIME
    sleep(6)



# @then("Click decline coverage button")
# def decline_coverage(context):
#     context.driver.find_element(By.CSS_SELECTOR, "button[data-test='espDrawerContent-declineCoverageButton']").click()
#     sleep(2)

@then("Open Target Cart Page")
def open_target_cart_page(context):
    context.driver.get("https://www.target.com/cart")
    # context.wait.until(EC)   THIS STEP FAILS
    sleep(4)

@then("Verify '{product}' has been added to cart")
def decline_coverage(context, product):
    actual_text = context.driver.find_element(By.XPATH,"//span[contains(text(), '1 item')]").text
    assert '1 item' in actual_text, f'Error: There are no {actual_text} in your cart'


