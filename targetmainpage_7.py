from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.sign_in_button = (By.ID, "account")  # Locator for "Sign In" in header, update if needed

    def click_header_sign_in(self):
        self.driver.find_element(*self.sign_in_button).click()
