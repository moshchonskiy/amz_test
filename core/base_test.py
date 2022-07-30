import pytest

from core.web_driver_factory import get_webdriver


class BaseTest:

    @pytest.fixture(scope='session')
    def driver(self):
        driver = get_webdriver()
        driver.set_window_size(1920, 1080)
        # driver.fullscreen_window()
        yield driver
        driver.quit()
