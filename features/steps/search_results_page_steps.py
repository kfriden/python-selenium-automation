from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify search results are shown')
def verify_search_results(context):
    actual_text = context.driver.find_element(By.XPATH, "//div[@data-test='resultsHeading']").text
    assert 'coffee' in actual_text, f'Error: Text coffee not in {actual_text}'