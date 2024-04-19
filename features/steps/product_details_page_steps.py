from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

COLOR_OPTIONS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
SELECTED_COLOR = (By.CSS_SELECTOR, "[class*='StyledVariationSelectorImage'] [class*='StyledHeaderWrapperDiv']")

@given("Open Target product '{product}' Page")
def open_target(context, product):
    context.driver.get(f'https://www.target.com/p/{product}')
    sleep(6)

@then("Verify Multiple Colors Can be Clicked")
def verify_multiple_colors(context):
    colors_expected = ['vapor grey microfiber', 'court green', 'oxide blue microfiber', 'heritage red microfiber', 'white smooth']
    actual_colors = []

    colors = context.driver.find_elements(*COLOR_OPTIONS)

    for color in colors:
        color.click()

        selected_color = context.driver.find_element(*SELECTED_COLOR).text
        selected_color = selected_color.split('\n')[1]
        actual_colors.append(selected_color)
        print(actual_colors)

    assert colors_expected == actual_colors, f'Expected {colors_expected} did not match actual {actual_colors}'