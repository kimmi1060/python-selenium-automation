from selenium.webdriver.common.by import By
from pages.base_page import Page

class CartPage(Page):
    CART_ICON = (By.ID, 'cart')
    CART_ITEM = (By.CSS_SELECTOR, ".cart-item")  # Example selector for the item in the cart

    def click_cart_icon(self):
        self.click(*self.CART_ICON)

    def verify_product_in_cart(self):
        assert self.find_element(*self.CART_ITEM).is_displayed(), "Product is not in the cart"
