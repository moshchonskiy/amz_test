from assertpy import assert_that

from core.base_test import BaseTest
from core.pages.amazon_base_page import AmazonPage
from utils.writers import csv_writer


class TestAmazonPage(BaseTest):

    def test_item_added_to_cart(self, driver):
        """
        Tests A:
            Open URL: to www.amazon.com
            At the input search box search for “software testing”
            Click the first item
            Add the item to the cart
            Open the cart
            verify:
                the item have being added successfully
        """
        amazon = AmazonPage(driver=driver).go_to()
        amazon.wait_at()
        amazon.accept_cookies()
        amazon_search = amazon.search_for('software testing')
        found_items = amazon_search.get_search_items()
        first_item_index = 0
        expected_item = found_items[first_item_index]
        item_page = amazon_search.go_to_item_page(found_items, index=first_item_index)
        item_page.add_item_to_cart()
        cart = amazon.go_to_cart()
        cart_items = cart.get_cart_items()
        actual_cart_item_titles = [i.text for i in cart_items]
        assert_that(
            actual_cart_item_titles,
            'Cart does not contain expected item!'
        ).contains(amazon_search.get_search_item_text(expected_item))

    def test_testing_books_exist(self, driver):
        """
        Tests B:
            Open URL: to www.amazon.com
            At the input search box search for “software testing”
            For the items (20~ items) in the 3 first pages extract the following values:
                Title
                Date
                Rate
            Save the results over a local CSV file
            verify :
                Item containing the text at the title “Modern CMake” exist
                Item containing the text in its title “Accelerate DevOps“ exist
        """
        amazon = AmazonPage(driver=driver).go_to()
        amazon.wait_at()
        amazon_search = amazon.search_for('software testing')
        # do not travers all pages
        search_results = amazon_search.get_search_page_items_data()
        csv_writer(['Name', 'Asin', 'Rating', 'GlobalRatingsNum'], search_results, 'cart.csv')
        actual_titles = [i[0] for i in search_results]
        assert_that(
            actual_titles,
            'There is no item with "Modern CMake" tile in results!'
        ).contains('Modern CMake')
        assert_that(
            any('Accelerate DevOps' in title for title in actual_titles),
            'There is no title with "Accelerate DevOps" in it!'
        ).is_true()
