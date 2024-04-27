from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import then

SEARCH_RESULT_HEADER = (By.XPATH, "//div[@data-test='resultsHeading']")

@then('Verify search results are shown for {expected_item}')
def verify_search_results(context, expected_item):
    context.app.search_results_page.verify_search_results(expected_item)

@then('Verify that URL has {product}')
def verify_search_page_url(context, product):
    # context.driver.wait.until(EC.url_contains(product), message= f'URL does not contain {product}')
    context.app.search_results_page.verify_partial_url(product)