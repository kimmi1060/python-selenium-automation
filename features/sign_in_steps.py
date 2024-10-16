from behave import given, when, then

@given('Open target main page')
def open_main_page(context):
    context.app.main_page.open_main_page()

@when('Click Sign In from header')
def click_sign_in_header(context):
    context.app.header.click_sign_in()

@when('From right-side navigation menu, click Sign In')
def click_sign_in_menu(context):
    context.app.right_nav_menu.click_sign_in_menu()

@then('Verify Sign In form opened')
def verify_sign_in_form(context):
    context.app.sign_in_page.verify_sign_in_form_displayed()
