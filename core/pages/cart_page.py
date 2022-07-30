from core.pages.base_page import BasePageObject
from core.elements.base_element import BaseElement
from core.locator import Locator


class CartPage(BasePageObject):
    TITLE = 'Cesta de compra'  # spanish

    @property
    def cart_item(self):
        return BaseElement(self.driver, Locator.class_name('sc-list-item-content'))

    def get_cart_items(self):
        items = self.cart_item.find_elements()
        return items
