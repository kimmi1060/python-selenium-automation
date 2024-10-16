from selenium.webdriver.common.by import By
from pages.base_page import Page

class RightNavMenu(Page):
    SIGN_IN_BUTTON_MENU = (By.XPATH, "//a[@data-test='sign-in']")  # Example selector for Sign In from side menu

    def click_sign_in_menu(self):
        self.click(*self.SIGN_IN_BUTTON_MENU)
