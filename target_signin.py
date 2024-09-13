from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

@given('I open the Target homepage')
def step_open_target_homepage(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://www.target.com")

@when('I click on the Sign In button')
def step_click_sign_in_button(context):
    sign_in_button = context.driver.find_element(By.XPATH, "//a[@id='account']")
    sign_in_button.click()

@when('I click on the Sign In link in the right side navigation menu')
def step_click_sign_in_link(context):
    sign_in_link = context.driver.find_element(By.XPATH, "//a[contains(text(),'Sign in')]")
    sign_in_link.click()

@then('I should see the Sign In form')
def step_verify_sign_in_form(context):
    sign_in_form = context.driver.find_element(By.ID, "signin-form")
    assert sign_in_form.is_displayed()
    context.driver.quit()
