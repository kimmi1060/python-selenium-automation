from pages.main_page import MainPage
from pages.header import Header
from pages.right_nav_menu import RightNavMenu
from pages.sign_in_page import SignInPage
from pages.search_results_page import SearchResultsPage
from pages.cart_page import CartPage


class Application:
    def __init__(self, driver):
        self.main_page = MainPage(driver)
        self.header = Header(driver)
        self.right_nav_menu = RightNavMenu(driver)
        self.sign_in_page = SignInPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.cart_page = CartPage(driver)
