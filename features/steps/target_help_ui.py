from behave import given, then
from selenium.webdriver.common.by import By

@given('I am on the Target Help page')
def step_impl(context):
    context.driver.get("https://help.target.com/help")

@then('I should see the following UI elements:')
def step_impl(context):
    for row in context.table:
        element_id = row['element']
        assert context.driver.find_element(By.ID, element_id) is not None
    context.driver.quit()
