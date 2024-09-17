from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By

@given('I am on the Target homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")

@when('I search for "{product}"')
def step_impl(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_box.submit()

@then('I should see the results for "{product}"')
def step_impl(context, product):
    assert product in context.driver.page_source
    context.driver.quit()
