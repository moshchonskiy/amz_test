from core.elements.base_element import BaseElement
from core.elements.base_button import ButtonElement
from core.locator import Locator


class Navbar(BaseElement):

    def __int__(self, driver):
        self.driver = driver
        self.locator = Locator.id('navbar')

    @property
    def search_box(self):
        return BaseElement(self.driver, Locator.id('twotabsearchtextbox'))

    @property
    def search_button(self):
        return ButtonElement(self.driver, Locator.id('nav-search-submit-button'))

    @property
    def cart(self):
        return BaseElement(self.driver, Locator.id('nav-cart-count-container'))
