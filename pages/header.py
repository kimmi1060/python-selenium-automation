from selenium.webdriver.common.by import By
from time import sleep

from pages.base_page import Page

class Header(Page):
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.XPATH, "//button[@data-test='@web/Search/SearchButton']")

    def search_product(self, item):
        self.input_text(item, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6) # wait for search results page to load
        sleep(8)  # wait for search results page to load

    class Header(Page):
        SIGN_IN_BUTTON = (By.ID, 'account')  # Example selector for Sign In in the header

        def click_sign_in(self):
            self.click(*self.SIGN_IN_BUTTON)

        def search_product(self, product_name):
            self.input_text(product_name, *self.SEARCH_FIELD)
            self.click(*self.SEARCH_BUTTON)