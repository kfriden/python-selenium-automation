from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



@then("Add any '{product}' item to cart")
def add_first_product(context, product):
    context.app.search_results_page.add_item_to_cart()

@then("Click Add to Cart on side menu")
def add_cart_side_menu(context):
    context.app.search_results_page.click_add_to_cart_side_menu()



# @then("Click decline coverage button")
# def decline_coverage(context):
#     context.driver.find_element(By.CSS_SELECTOR, "button[data-test='espDrawerContent-declineCoverageButton']").click()
#     sleep(2)






