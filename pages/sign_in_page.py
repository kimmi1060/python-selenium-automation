from selenium.webdriver.common.by import By
from pages.base_page import Page

class SignInPage(Page):
    SIGN_IN_FORM = (By.ID, 'signInForm')  # Example selector for Sign In form

    def verify_sign_in_form_displayed(self):
        assert self.find_element(*self.SIGN_IN_FORM).is_displayed(), "Sign In form is not displayed"
