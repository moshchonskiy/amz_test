from selenium.webdriver.common.by import By


class Locator:

    def __init__(self, by, value):
        self.by = by
        self.value = value

    @classmethod
    def id(Locator, value):
        return Locator(By.ID, value)

    @classmethod
    def name(Locator, value):
        return Locator(By.NAME, value)

    @classmethod
    def link_text(Locator, value):
        return Locator(By.LINK_TEXT, value)

    @classmethod
    def css_selector(Locator, value):
        return Locator(By.CSS_SELECTOR, value)

    @classmethod
    def xpath_selector(Locator, value):
        return Locator(By.XPATH, value)

    @classmethod
    def class_name(Locator, value):
        return Locator(By.CLASS_NAME, value)

    @classmethod
    def tag_name(Locator, value):
        return Locator(By.TAG_NAME, value)

    def __str__(self, *args, **kwargs):
        return "{0}:{1}".format(self.by, self.value)
