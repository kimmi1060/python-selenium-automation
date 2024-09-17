from behave import given, when, then
from selenium.webdriver.common.by import By

@when('I add "{product}" to the cart')
def step_impl(context, product):
    search_box = context.driver.find_element(By.ID, "search")
    search_box.send_keys(product)
    search_box.submit()
    context.driver.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]").click()

@then('the cart should contain the product')
def step_impl(context):
    cart = context.driver.find_element(By.ID, "cart")
    assert "laptop" in cart.text  # Modify this based on the product
    context.driver.quit()
