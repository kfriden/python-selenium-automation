from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then('Verify cart is empty message shows')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty_message()