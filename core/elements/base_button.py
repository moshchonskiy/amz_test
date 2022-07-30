from core.elements.base_element import BaseElement


class ButtonElement(BaseElement):

    def __get__(self, obj, cls=None):
        return self

    def click(self):
        self.wait_for_clickable_element()
        element = self.driver.find_element(self.locator.by, self.locator.value)
        element.click()
