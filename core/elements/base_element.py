from dataclasses import dataclass
from typing import Optional


from selenium.webdriver import Remote
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException

from core.locator import Locator


@dataclass
class BaseElement:
    driver: Remote
    locator: Optional[Locator] = None

    @property
    def name(self):
        return type(self).__name__

    def wait_for_element(self, time_sec: int = 5):
        try:
            return WebDriverWait(self.driver, time_sec).until(
                EC.presence_of_element_located((self.locator.by, self.locator.value)))
        except TimeoutException:
            raise RuntimeError("'{}' with {} '{}' is not present!".format(
                self.name, self.locator.by, self.locator.value))

    def wait_for_elements(self, time_sec: int = 5):
        try:
            return WebDriverWait(self.driver, time_sec).until(
                EC.presence_of_all_elements_located((self.locator.by, self.locator.value)))
        except TimeoutException:
            raise RuntimeError("'{}' with {} '{}' are not present!".format(
                self.name, self.locator.by, self.locator.value))

    def wait_for_clickable_element(self, time_sec: int = 5, raise_exception: bool = True):
        try:
            return WebDriverWait(self.driver, time_sec).until(
                EC.element_to_be_clickable((self.locator.by, self.locator.value)))
        except TimeoutException:
            if raise_exception:
                raise RuntimeError("'{}' with {} '{}' is not clickable!".format(
                    self.name, self.locator.by, self.locator.value))
            else:
                return False

    def send_keys(self, keys_to_send: str):
        element = self.find_element()
        element.send_keys(keys_to_send)

    def find_element(self):
        try:
            self.wait_for_element(time_sec=10)
            return self.driver.find_element(self.locator.by, self.locator.value)
        except NoSuchElementException:
            raise RuntimeError("'{}' not found by {} '{}'".format(self.name, self.locator.by, self.locator.value))

    def find_elements(self):
        self.wait_for_element()
        return self.driver.find_elements(self.locator.by, self.locator.value)

    def click(self):
        self.wait_for_element().click()
