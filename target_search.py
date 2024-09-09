from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions=create_session_signin')

#locate element target sign-in page
driver.find_element(By.XPATH, "//span[text()='Sign in']")

driver.find_element(By.XPATH, "//a[@id='accountNav-signIn']")

driver.find_element(By.XPATH, "//h1[contains(text(), 'Sign into your Target account')]")

driver.find_element(By.XPATH, "//button[@id='login']")

print("Test Case Passed: Users can navigate to SignIn page.")

driver.quit()
