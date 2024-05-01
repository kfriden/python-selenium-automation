from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on Target terms and conditions link')
def click_tc_link(context):
    context.app.tc_page.click_tc_link()

@then('Verify Terms and Conditions page is opened')
def verify_tc_page_opens(context):
    context.app.tc_page.verify_tc_opened()