import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    options.add_experimental_option(
        "prefs",
        {
            "credentials_enable_service": False,
            "profile.password_manager_leak_detection": False,
            "autofill.profile_enabled": False,
            "notifications": 2,
        }
    )

    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1920, 1080)

    driver.execute_cdp_cmd("Network.enable", {})

    driver.execute_cdp_cmd(
        "Network.setBlockedURLs",
        {
            "urls": [
                "*://*.doubleclick.net/*"
            ]
        }
    )

    yield driver

    driver.quit()