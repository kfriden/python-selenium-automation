from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@then("Open Target Cart Page")
def open_target_cart_page(context):
    context.app.cart_page.open_cart_page()

@then('Verify cart is empty message shows')
def verify_cart_empty(context):
    context.app.cart_page.verify_cart_empty_message()

@then("Verify '{product}' has been added to cart")
def verify_product_in_cart(context, product):
    context.app.cart_page.verify_item_in_cart()
