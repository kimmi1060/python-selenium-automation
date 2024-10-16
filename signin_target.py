from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the WebDriver
driver = webdriver.Chrome()

# Open Target Sign-In Page
driver.get('https://www.target.com/login')

# Enter incorrect email and password
driver.find_element(By.ID, 'username').send_keys('incorrect@example.com')  # Replace with actual element ID
driver.find_element(By.ID, 'password').send_keys('wrongpassword')

# Click the login button
driver.find_element(By.ID, 'login').click()  # Replace with actual element ID for login button

# Verify the error message
error_message = driver.find_element(By.XPATH, "//div[contains(text(), \"We can't find your account.\")]")
assert error_message.is_displayed(), "Error message 'We can't find your account.' not displayed."

# Close the browser
driver.quit()
