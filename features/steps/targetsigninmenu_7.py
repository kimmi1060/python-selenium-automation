from selenium.webdriver.common.by import By

class SignInMenu:
    def __init__(self, driver):
        self.driver = driver
        self.menu_sign_in_link = (By.XPATH, "//a[@href='/signin']")  # Locator for the "Sign In" link in the menu

    def click_menu_sign_in(self):
        self.driver.find_element(*self.menu_sign_in_link).click()
