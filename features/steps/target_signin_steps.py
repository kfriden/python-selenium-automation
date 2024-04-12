from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click sign in on side nav bar")
def sign_in_sidenav(context):
    context.driver.find_element(By.CSS_SELECTOR, "a[data-test='accountNav-signIn']").click()
    sleep(3)

@then('Verify sign in form opens')
def verify_signin_form(context):
    actual_text = context.driver.find_element(By.XPATH, "//span[text()='Sign into your Target account']").text
    assert 'Sign into your Target account' in actual_text, f'Error: Text sign into your account not in {actual_text}'