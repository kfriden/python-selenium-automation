from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open Target Circle page')
def open_target(context):
    context.driver.get('https://www.target.com/circle')
    sleep(4)

@then('Verify 10 Circle benefits')
def verify_10_circle_benefits(context):
    links = context.driver.find_elements(By.CSS_SELECTOR, "div.cell-item-content")
    print(links)
    assert len(links) == 10, f'Expected 10 links but got {len(links)}'
