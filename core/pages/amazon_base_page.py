from core.pages.base_page import BasePageObject
from core.pages.amazon_search_results import AmazonSearch
from core.pages.cart_page import CartPage
from core.elements.navbar import Navbar


class AmazonPage(BasePageObject):
    TITLE: str = 'Amazon.es'
    URL: str = 'https://www.amazon.es'

    def search_for(self, query: str):
        self.navbar.search_box.send_keys(query)
        self.navbar.search_button.click()
        return AmazonSearch(self.driver)

    @property
    def navbar(self):
        return Navbar(driver=self.driver)

    def go_to_cart(self):
        self.navbar.cart.click()
        return CartPage(self.driver).wait_at()
