from selenium import webdriver


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
        "enableVNC": True,
        "browserName": browser_type,
        "browserVersion": browser_ver,
        "selenoid:options": {
            "enableVideo": True
        }
    }
    driver = webdriver.Remote(
        command_executor="http://selenoid:4444/wd/hub",
        desired_capabilities=capabilities,
    )

    return driver
