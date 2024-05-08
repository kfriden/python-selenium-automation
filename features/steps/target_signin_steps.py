from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep

@given('Open sign in page')
def open_signin_page(context):
    context.app.sign_in_page.open_signin()

@when("Click sign in on side nav bar")
def sign_in_sidenav(context):
    context.app.main_page.sign_in_sidenav_bar()

@then('Verify sign in form opens')
def verify_signin_form(context):
    context.app.sign_in_page.verify_signin_opens()

@when('Store original window')
def store_original_window(context):
    context.original_window = context.app.base_page.get_current_window()

@then('Input incorrect username {username}')
def input_username(context, username):
    context.app.sign_in_page.input_username(username)

@then('Input incorrect password {password}')
def input_password(context, password):
    context.app.sign_in_page.input_password(password)

@when('Click login')
def click_login(context):
    context.app.sign_in_page.click_login()

@then('Verify We cannot find your account message shows')
def verify_signin_error_message(context):
    context.app.sign_in_page.verify_signin_error_message()

