from selenium.webdriver import Remote
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


POLL_FREQUENCY = 0.5  # How long to sleep in between calls to the method
IGNORED_EXCEPTIONS = (  # exceptions ignored during calls to the method
    NoSuchElementException,
    StaleElementReferenceException
)
CONDITION_MESSAGE = 'The condition is not True after {} seconds'


class CustomWebDriverWait(WebDriverWait):

    def until_cond(self, condition_function, message: str = ''):
        def cond_method(driver):
            return condition_function()

        return self.until(method=cond_method, message=message)


class BasePageObject:
    TITLE: str = None
    TIMEOUT: float = 10.0
    URL: str = None

    def __init__(self, driver: Remote, **kwargs):
        """
        Creates a new instance of WebDriver or sets the existing one if it is passed as the argument
        :rtype: selenium.webdriver.remote.webdriver.WebDriver
        :param driver: current WebDriver
        """
        self.driver = driver

    @property
    def at(self):
        title_result = True
        if self.TITLE is not None:
            try:
                self.wait_until_title_updated(self.TITLE)
            except AssertionError:
                return False
            title_result = self.TITLE in self.driver.title
        return title_result

    def wait_at(self, timeout=TIMEOUT):
        self.wait_until_condition(lambda: self.at, timeout=timeout)
        return self

    def wait_until_condition(
            self,
            condition,
            timeout: float = TIMEOUT,
            poll_frequency: float = POLL_FREQUENCY,
            message: str = CONDITION_MESSAGE,
            ignore_exceptions: tuple = None
    ):
        """Waits until condition is True"""
        exceptions = IGNORED_EXCEPTIONS if ignore_exceptions is None else ignore_exceptions
        return CustomWebDriverWait(
            self.driver, timeout=timeout, poll_frequency=poll_frequency, ignored_exceptions=exceptions
        ).until_cond(
            condition,
            message=message.format(timeout)
        )

    def wait_until_title_updated(self, title: str, timeout: float = TIMEOUT):
        try:
            WebDriverWait(self.driver, timeout).until(EC.title_contains(title))
        except TimeoutException:
            raise AssertionError(
                'It takes more than {} sec to update a title. Current title is {}'.format(
                    timeout, self.driver.title)
                )

    def go_to(self, url: str = None, new_tab: bool = False):
        if new_tab:
            self.driver.execute_script('open();')
            self.driver.switch_to.window(self.driver.window_handles[1])
        go_to_url = url if url is not None else self.URL
        self.driver.get(go_to_url)
        return self
