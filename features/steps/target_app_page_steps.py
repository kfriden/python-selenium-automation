from behave import given, when, then
from time import sleep

@given('Open Target App Page')
def open_target_app(context):
    context.app.target_app_page.open_target_app()

@given('Store original window')
def store_original_window(context):
    context.original_window = context.app.target_app_page.get_current_window()

@then('Click Privacy Policy link')
def click_privacy_link(context):
    context.app.target_app_page.click_pp_link()

@then('Switch to new window')
def switch_to_window(context):
    context.app.target_app_page.switch_to_new_window()
    sleep(2)

@then('Verify Privacy Policy page is opened')
def verify_pp_opened(context):
    context.app.privacy_policy_page.verify_pp_opened()

@then('Close current page')
def close(context):
    context.app.target_app_page.close()
    sleep(3)

@then('Return to original window')
def return_to_original_window(context):
    sleep(5)
    context.app.target_app_page.switch_to_window_by_id(context.original_window)
    sleep(2)
