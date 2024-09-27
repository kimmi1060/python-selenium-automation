from behave import given, when, then
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# @given('I am on the Target product page "{url}"')
# def step_impl(context, url):
#     # Open the browser and navigate to the product page
#     context.driver.get(url)


# @when('I select each available product color')
# def step_impl(context):
#     # Wait until color options are present and interact with them
#     wait = WebDriverWait(context.driver, 10)
#     context.color_options = wait.until(
#         EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="colorSwatch"]')))
#
#     context.selected_colors = []
#
#     for color in context.color_options:
#         color.click()  # Click each color option
#
#         # Wait for the color to be selected (is-active class should be applied)
#         selected_color = wait.until(
#             EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="colorSwatch"].is-active')))
#
#         # Store the selected color for validation
#         context.selected_colors.append(selected_color)


# @then('the selected color should be visibly highlighted')
# def step_impl(context):
#     # Check that all clicked colors have the "is-active" class, verifying they are selected
#     assert len(context.selected_colors) > 0, "No colors were selected!"
#     for color in context.selected_colors:
#         assert 'is-active' in color.get_attribute('class'), "Color is not properly highlighted or selected!"


@given('I am on the Target product page "{url}"')
def step_impl(context, url):
    # Open the browser and navigate to the product page
    context.driver.get(url)


@when('I select each available product color')
def step_impl(context):
    # Wait until color options are present and interact with them
    wait = WebDriverWait(context.driver, 10)
    context.color_options = wait.until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, '[data-test="colorSwatch"]')))

    context.selected_colors = []

    for color in context.color_options:
        color.click()  # Click each color option

        # Wait for the color to be selected (is-active class should be applied)
        selected_color = wait.until(
            EC.presence_of_element_located((By.CSS_SELECTOR, '[data-test="colorSwatch"].is-active')))

        # Store the selected color for validation
        context.selected_colors.append(selected_color)


@then('the selected color should be visibly highlighted')
def step_impl(context):
    # Check that all clicked colors have the "is-active" class, verifying they are selected
    assert len(context.selected_colors) > 0, "No colors were selected!"
    for color in context.selected_colors:
        assert 'is-active' in color.get_attribute('class'), "Color is not properly highlighted or selected!"
