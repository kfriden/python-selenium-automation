from selenium.webdriver.common.by import By
from behave import then

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_results_page.verify_search_results(expected_item)