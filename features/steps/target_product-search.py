from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@given('I am on the Target homepage')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get("https://www.target.com")
    context.wait = WebDriverWait(context.driver, 10)  # Explicit wait with a 10-second timeout

@when('I search for "{product}"')
def step_impl(context, product):
    # Wait until the search box is present
    search_box = context.wait.until(EC.presence_of_element_located((By.ID, "search")))
    search_box.send_keys(product)
    search_box.submit()

@then('I should see the results for "{product}"')
def step_impl(context, product):
    # Wait until the page source contains the search results
    context.wait.until(EC.presence_of_element_located(
    (By.CLASS_NAME, "search-result")))  # Example: adjust locator based on your page structure
    assert product in context.driver.page_source
    context.driver.quit()
