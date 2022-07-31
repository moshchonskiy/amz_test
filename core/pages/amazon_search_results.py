from selenium.webdriver.remote.webelement import WebElement

from core.pages.base_page import BasePageObject
from core.pages.item_page import ItemPage
from core.elements.base_element import BaseElement
from core.locator import Locator


class AmazonSearch(BasePageObject):

    @property
    def search_item(self):
        return BaseElement(
            driver=self.driver,
            locator=Locator.xpath_selector('//div[contains(@class, "s-result-item s-asin")]')
        )

    def get_search_item_text(self, s_item: WebElement):
        text_locator = Locator.xpath_selector('.//div[contains(@class, "s-title-instructions-style")]/h2')
        return s_item.find_element(text_locator.by).text

    @property
    def name_locator(self):
        return Locator.xpath_selector('.//span[@class="a-size-base-plus a-color-base a-text-normal"]')

    def get_search_items(self):
        self.search_item.wait_for_elements()
        items = self.search_item.find_elements()
        return items

    def go_to_item_page(self, items: list, index: int = None, title: str = None):
        if index is not None:
            items[index].click()
        elif title:
            for item in items:
                name = item.find_element(self.name_locator.by, self.name_locator.value).text
                if name == title:
                    item.click()
        return ItemPage(self.driver)

    def get_search_page_items_data(self):
        items = self.get_search_items()
        results = []
        for item in items:
            name = item.find_element(self.name_locator.by, self.name_locator.value).text
            data_asin = item.get_attribute("data-asin")
            ratings_box_locator = Locator.xpath_selector('.//div[@class="a-row a-size-small"]/span')
            ratings_box = item.find_elements(ratings_box_locator.by, ratings_box_locator.value)
            if ratings_box:
                ratings = ratings_box[0].get_attribute('aria-label')
                ratings_num = ratings_box[1].get_attribute('aria-label')
            else:
                ratings, ratings_num = 0, 0
            results.append((name, data_asin, ratings, ratings_num))
        return results
