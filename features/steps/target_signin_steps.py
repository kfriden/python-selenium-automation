from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when("Click sign in on side nav bar")
def sign_in_sidenav(context):
    context.app.main_page.sign_in_sidenav_bar()

@then('Verify sign in form opens')
def verify_signin_form(context):
    context.app.sign_in_page.verify_signin_opens()