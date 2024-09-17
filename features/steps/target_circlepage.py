from behave import given, then
from selenium.webdriver.common.by import By

@given('I am on the Target Circle page')
def step_impl(context):
    context.driver.get("https://www.target.com/circle")

@then('I should see 10 benefit cells')
def step_impl(context):
    benefit_cells = context.driver.find_elements(By.CLASS_NAME, "circle-benefit-cell")
    assert len(benefit_cells) == 10
    context.driver.quit()
