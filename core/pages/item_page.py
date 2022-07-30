from core.pages.base_page import BasePageObject
from core.elements.base_button import ButtonElement
from core.locator import Locator


class ItemPage(BasePageObject):

    @property
    def cart_button(self):
        return ButtonElement(self.driver, Locator.id('add-to-cart-button'))

    def add_item_to_cart(self):
        self.cart_button.click()
        return self
