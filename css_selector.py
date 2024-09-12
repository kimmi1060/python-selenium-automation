from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# Start Chrome browser:
driver_path = ChromeDriverManager().install()
# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# open the url
driver.get('https://www.amazon.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.com%2Fs%3Fk%3Damazon%2Blog%2Binto%2Bmy%2Baccount%26hvadid%3D694608587694%26hvdev%3Dc%26hvexpln%3D67%26hvlocphy%3D9011130%26hvnetw%3Dg%26hvocijid%3D8645260435005845608--%26hvqmt%3De%26hvrand%3D8645260435005845608%26hvtargid%3Dkwd-305869653030%26hydadcr%3D7662_13469262%26tag%3Dgooghydr-20%26ref%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0')

 # Locate elements using CSS Selectors
    # Amazon logo
    driver.find_element(By.CSS_SELECTOR, "a.a-link-nav-icon")

    # Create account title
    driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

    # Your Name input field
    driver.find_element(By.CSS_SELECTOR, "#ap_customer_name")

    # Email input field
    driver.find_element(By.CSS_SELECTOR, "#ap_email")

    # Password input field
    driver.find_element(By.CSS_SELECTOR, "#ap_password")

    # Re-enter Password input field
    driver.find_element(By.CSS_SELECTOR, "#ap_password_check")

    # Create Your Amazon Account button
    driver.find_element(By.CSS_SELECTOR, "#continue")

    # Conditions of Use link
    driver.find_element(By.CSS_SELECTOR, "a[href*='condition_of_use']"
    # Privacy Notice link
    driver.find_element(By.CSS_SELECTOR, "a[href*='privacy_notice']")

    # Sign in link for existing account
    driver.find_element(By.CSS_SELECTOR, "#signInLink")

print("Test Case Passed: All elements were found successfully.")
driver.quit()
