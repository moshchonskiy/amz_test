from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_webdriver(
    browser_type: str = 'firefox',
    browser_ver: str = '101.0'
):
    """
    get remote browser webdriver
    :param browser_type: str
    :param browser_ver: ser
    :return: webdriver
    """

    capabilities = {
        "browserName": browser_type,
        "browserVersion": browser_ver,
        "selenoid:options": {
            "enableVideo": True
        }
    }
    opts = Options()
    opts.add_argument('--disable-blink-features=AutomationControlled')

    driver = webdriver.Remote(
        command_executor="http://localhost:4444/wd/hub",
        desired_capabilities=capabilities,
        options=opts
    )

    return driver
