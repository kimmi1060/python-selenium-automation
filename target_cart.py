from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from behave import given, when, then

@given('I open the Target homepage')
def step_open_target_homepage(context):
    context.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    context.driver.get("https://www.target.com")

@when('I click on the Cart icon')
def step_click_cart_icon(context):
    cart_icon = context.driver.find_element(By.XPATH, "//a[@aria-label='Cart']")
    cart_icon.click()

@then('I should see "Your cart is empty" message')
def step_verify_empty_cart_message(context):
    empty_cart_message = context.driver.find_element(By.XPATH, "//span[contains(text(),'Your cart is empty')]")
    assert empty_cart_message.is_displayed()
    context.driver.quit()